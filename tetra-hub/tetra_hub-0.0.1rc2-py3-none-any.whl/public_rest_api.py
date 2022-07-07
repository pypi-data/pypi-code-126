from __future__ import annotations
import os
import json
from typing import Dict, List, Tuple, Any, Union
from urllib.parse import urljoin
import posixpath
import requests
import configparser
from tqdm import tqdm
from contextlib import nullcontext
from dataclasses import dataclass
from types import SimpleNamespace
from typing import List
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from . import public_api_pb2 as api_pb
from . import api_status_codes
import re
from pathlib import Path
from collections import OrderedDict

UNKNOWN_ERROR = "Unknown error."
API_VERSION = "v1"

# Used for error message feedback
CASUAL_CLASSNAMES = {
    api_pb.ProfileJob: "job",
    api_pb.Model: "model",
    api_pb.User: "user",
}

DEFAULT_CONFIG_PATH = "~/.tetra/client.ini"

Shapes = Union[
    List[Tuple[int, ...]],
    "OrderedDict[str, Tuple[int, ...]]",
    List[Tuple[str, Tuple[int, ...]]],
    Dict[str, Tuple[int, ...]],
]


def get_config_path(expanduser=True):
    path = os.environ.get("TETRA_CLIENT_INI", DEFAULT_CONFIG_PATH)
    if expanduser:
        path = os.path.expanduser(path)
    return path


@dataclass
class Device:
    """
    Represents a target device.

    Attributes
    ----------
    name
        Name of the device, e.g. `"Apple iPhone 13"`.
    os
        Version of the OS, e.g. `"15.0.2"`.

    Examples
    --------
    ::

        import tetra_hub as hub

    Create a target device for iPhone 12 with specifically iOS 14.8::

        device = hub.Device("Apple iPhone 12", "14.8")

    Fetch a list of devices using :py:func:`~tetra_hub.get_devices`::

        devices = hub.get_devices()
    """

    name: str
    os: str = ""


@dataclass
class ClientConfig:
    """
    Configuration information, such as your API token, for use with
    :py:class:`.Client`.

    Parameters
    ----------
    api_url
        URL of the API backend endpoint.
    web_url
        URL of the web interface.
    api_token
        API token. Available through the web interface under the "Account" page.
    """

    api_url: str
    web_url: str
    api_token: str


class APIException(Exception):
    """
    Excpetion for the python REST API.

    Parameters
    ----------
    message : str
        Message of the failure. If None, sets it automatically based on
        `status_code`.
    status_code : int
        API status code (a superset of HTTP status codes).
    """

    def __init__(self, message=None, status_code=None):
        if message is None:
            if status_code is not None:
                # Some common error codes have custom messages
                if status_code == api_status_codes.HTTP_401_UNAUTHORIZED:
                    message = "API authentication failure; please check your API token."
                elif status_code == api_status_codes.HTTP_429_TOO_MANY_REQUESTS:
                    message = "Too Many Requests: please slow down and try again soon."
                elif status_code == api_status_codes.API_CONFIGURATION_MISSING_FIELDS:
                    config_path = get_config_path(expanduser=False)
                    message = f"Required fields are missing from your {config_path}."
                else:
                    message = f"API request returned status code {status_code}."
            else:
                message = UNKNOWN_ERROR

        super().__init__(message)
        self.status_code = status_code


def _response_as_protobuf(
    response: requests.Response, protobuf_class: Any, obj_id: int = None
) -> Any:
    if (
        api_status_codes.is_success(response.status_code)
        and response.headers.get("Content-Type") == "application/x-protobuf"
    ):
        pb = protobuf_class()
        pb.ParseFromString(response.content)
        return pb
    elif (
        response.status_code == api_status_codes.HTTP_404_NOT_FOUND
        and obj_id is not None
    ):
        prefix = ""
        class_name = CASUAL_CLASSNAMES.get(protobuf_class)
        if class_name is not None:
            prefix = class_name.capitalize() + " "

        raise APIException(
            f"{prefix}ID {obj_id} could not be found. It may not exist or you may not have permission to view it.",
            status_code=response.status_code,
        )
    else:
        raise APIException(status_code=response.status_code)


def _prepare_offset_limit_query(offset: int, limit: int | None) -> str:
    extras = []
    if offset > 0:
        extras.append(f"offset={offset}")
    if limit is not None:
        extras.append(f"limit={limit}")
    if extras:
        return "?" + "&".join(extras)
    else:
        return ""


def _load_default_api_config(verbose=False) -> ClientConfig:
    """
    Load a default ClientConfig from default locations.

    Parameters
    ----------
    verbose : bool
        Print where config file is loaded from.

    Returns
    -------
    config : ClientConfig
        API authentication configuration.
    """
    # Load from default config path
    config = configparser.ConfigParser()
    # Client config should be in ~/.tetra/client.ini
    tilde_config_path = get_config_path(expanduser=False)
    config_path = os.path.expanduser(tilde_config_path)
    if verbose:
        print(f"Loading Client config from {tilde_config_path} ...")
    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"{tilde_config_path} not found. Please go to the Account page to "
            "find instructions of how to install your API key."
        )
    config.read([config_path])
    try:
        client_config = config["api"]

        api_config = ClientConfig(
            api_url=client_config["api_url"],
            web_url=client_config["web_url"],
            api_token=client_config["api_token"],
        )
    except KeyError:
        raise APIException(
            status_code=api_status_codes.API_CONFIGURATION_MISSING_FIELDS
        )
    return api_config


def _auth_header(
    content_type: str = "application/x-protobuf", config: ClientConfig = None
) -> dict:
    if config is None:
        config = _load_default_api_config()
    header = {
        "Authorization": f"token {config.api_token}",
        "Content-Type": content_type,
    }
    return header


def _api_url(*rel_paths, config: ClientConfig = None) -> str:
    if config is None:
        config = _load_default_api_config()
    return urljoin(config.api_url, posixpath.join("api", API_VERSION, *rel_paths, ""))


def _list_shapes_to_tensor_type_list_pb(
    input_shapes: Shapes,
) -> api_pb.NamedTensorTypeList:
    def _add_to_named_tensor_pb(
        name: str, shape: Tuple[int, ...]
    ) -> api_pb.NamedTensorType:
        named_tensor_type_pb = api_pb.NamedTensorType()
        named_tensor_type_pb.name = name
        for i in shape:
            named_tensor_type_pb.tensor_type.shape.append(i)
        named_tensor_type_pb.tensor_type.dtype = api_pb.TensorDtype.FLOAT32
        return named_tensor_type_pb

    tensor_type_pb_list = []

    if isinstance(input_shapes, dict):
        input_shapes = OrderedDict(sorted(input_shapes.items()))
        if isinstance(input_shapes, OrderedDict):
            for name, shape in input_shapes.items():
                named_tensor_type_pb = _add_to_named_tensor_pb(name, shape)
                tensor_type_pb_list.append(named_tensor_type_pb)
    if isinstance(input_shapes, list):
        if isinstance(input_shapes[0][0], int):
            for index, shape in enumerate(input_shapes):
                named_tensor_type_pb = _add_to_named_tensor_pb(
                    f"input_{index+1}", shape  # type: ignore
                )
                tensor_type_pb_list.append(named_tensor_type_pb)
        else:
            for name_and_shape in input_shapes:
                name, shape = name_and_shape
                named_tensor_type_pb = _add_to_named_tensor_pb(name, shape)  # type: ignore
                tensor_type_pb_list.append(named_tensor_type_pb)

    return api_pb.NamedTensorTypeList(types=tensor_type_pb_list)


def _tensor_type_list_pb_to_list_shapes(
    tensor_type_list_pb: api_pb.NamedTensorTypeList,
) -> Shapes:
    shapes_list = []
    for named_tensor_type in tensor_type_list_pb.types:
        shape = []
        for d in named_tensor_type.tensor_type.shape:
            shape.append(d)
        shapes_list.append((named_tensor_type.name, tuple(shape)))
    return shapes_list


# These helper functions are placed in a utils namespace
# so as not to confuse with core API functions
utils = SimpleNamespace(
    response_as_protobuf=_response_as_protobuf,
    prepare_offset_limit_query=_prepare_offset_limit_query,
    load_default_api_config=_load_default_api_config,
    auth_header=_auth_header,
    api_url=_api_url,
    list_shapes_to_tensor_type_list_pb=_list_shapes_to_tensor_type_list_pb,
    tensor_type_list_pb_to_list_shapes=_tensor_type_list_pb_to_list_shapes,
)


def get_auth_user(config: ClientConfig = None) -> api_pb.User:
    """
    Get authenticated user information.

    Parameters
    ----------
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    user_pb : User
        Get authenticated user information.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("users", "auth", "user", config=config)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    # Note, the API returns a JSON right now, but we will translate this to a
    # protobuf
    content = json.loads(response.content)
    if api_status_codes.is_success(response.status_code):
        user_pb = api_pb.User(
            id=content["pk"],
            first_name=content.get("first_name", ""),
            last_name=content.get("last_name", ""),
            email=content["email"],
        )
        return user_pb
    else:
        raise APIException(status_code=response.status_code)


def get_user(user_id: int, config: ClientConfig = None) -> api_pb.User:
    """
    Get user information.

    Parameters
    ----------
    user_id : int
        User ID.
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    user_pb : User
       User information as protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("users", str(user_id), config=config)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.User, obj_id=user_id)


def get_user_list(
    offset: int = 0, limit: int | None = None, config: ClientConfig = None
) -> api_pb.UserList:
    """
    Get user information.

    Parameters
    ----------
    offset : int
        Offset the query.
    limit : int
        Limit query response size.
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    user_list_pb : UserList
       User list as protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("users", config=config)
    url += utils.prepare_offset_limit_query(offset, limit)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.UserList)


def get_device_list(config: ClientConfig = None) -> api_pb.DeviceList:
    """
    Get list of active devices.

    Parameters
    ----------
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    device_list_pb : DeviceList
       Device list as protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("devices", config=config)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.DeviceList)


def create_profile_job(
    job_pb: api_pb.ProfileJob, config: ClientConfig = None
) -> api_pb.CreateUpdateResponse:
    """
    Create new profile job.

    Parameters
    ----------
    job_pb : ProfileJob
        Protobuf object with new profile job.
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    response_pb : CreateUpdateResponse
        Returns a CreateUpdateResponse. If successful, ``id`` will be nonzero.
        If failure, ``id`` will be zero and ``status`` will contain an error.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("profile_jobs", config=config)
    header = utils.auth_header(config=config)
    response = requests.post(
        url,
        data=job_pb.SerializeToString(),
        headers=header,
    )
    return utils.response_as_protobuf(response, api_pb.CreateUpdateResponse)


def get_profile_job(job_id: int, config: ClientConfig = None) -> api_pb.ProfileJob:
    """
    Get profile job information.

    Parameters
    ----------
    job_id : int
        Job ID.
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    job_pb : ProfileJob
        Profile job as protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("profile_jobs", str(job_id), config=config)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.ProfileJob, obj_id=job_id)


def get_profile_job_list(
    offset: int = 0,
    limit: int | None = None,
    config: ClientConfig = None,
    states: List[api_pb.ProfileJobState.ValueType] = None,
) -> api_pb.ProfileJobList:
    """
    Get list of profile jobs visible to the authenticated user.

    Parameters
    ----------
    offset : int
        Offset the query.
    limit : int
        Limit query response size.

    Returns
    -------
    list_pb : ProfileJobList
        List of profile jobs as protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("profile_jobs", config=config)

    # TODO: better API for joining optional query strings.
    offset_limit_query = utils.prepare_offset_limit_query(offset, limit)
    states_query = f"state={','.join([str(x) for x in states])}" if states else ""
    if states_query:
        if offset_limit_query:
            states_query = "&" + states_query
        else:
            states_query = "?" + states_query
    url += offset_limit_query + states_query

    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.ProfileJobList)


def get_profile_job_results(
    job_id: int, config: ClientConfig = None
) -> api_pb.ProfileJobResult:
    """
    Get profile job results, if available.

    Parameters
    ----------
    job_id : int
        Job ID as integer.
    config : ClientConfig
        API authentication configuration.

    Results
    -------
    res_pb : ProfileJobResult
        Result is returned as a protobuf object. Or None if results are not available.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    header = utils.auth_header(config=config)
    url = utils.api_url("profile_jobs", str(job_id), "result", config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.ProfileJobResult, obj_id=job_id)


# Workaround for mypy having trouble with globals https://github.com/python/mypy/issues/5732
last: int


def upload_model(
    path: str | Path,
    name: str = None,
    model_type: api_pb.ModelType.ValueType = api_pb.ModelType.UNDEFINED_MODEL_TYPE,
    verbose: bool = True,
    config: ClientConfig = None,
) -> api_pb.CreateUpdateResponse:
    """
    Upload a model

    Parameters
    ----------
    path : str or Path
        Local path to neural network file.
    name : str
        Name of the model. If None, uses basename of path.
    model_type : api_pb.ModelType
        Type of the model.
    verbose : bool
        If true, will show progress bar in standard output.
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    res_pb : CreateUpdateResponse
        Returns a CreateUpdateResponse protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    total_size = os.path.getsize(path)

    e = MultipartEncoder(
        fields={
            "data": ("filename", open(path, "rb"), "application/octet-stream"),
            "model_type": api_pb.ModelType.Name(model_type),
            "name": name or os.path.basename(path),
        }
    )

    global last
    last = 0
    if verbose:
        tqdm_context = tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            colour="magenta",
        )

        def update_progress(monitor):
            global last
            # Your callback function
            pbar.update(monitor.bytes_read - last)
            last = monitor.bytes_read

    else:
        tqdm_context = nullcontext()

        def update_progress(monitor):
            pass

    upload_url = utils.api_url("models", config=config)

    with tqdm_context as pbar:
        m = MultipartEncoderMonitor(e, update_progress)
        header = utils.auth_header(content_type=m.content_type, config=config)
        response = requests.post(upload_url, data=m, headers=header)

        update_progress(SimpleNamespace(bytes_read=total_size))

    response_pb = api_pb.CreateUpdateResponse()
    if api_status_codes.is_success(response.status_code):
        response_pb.ParseFromString(response.content)
        return response_pb
    elif response.headers["Content-Type"] == "application/json":
        if response.status_code == api_status_codes.HTTP_401_UNAUTHORIZED:
            # Use the default description for 401
            raise APIException(status_code=response.status_code)
        else:
            raise APIException(response.content, status_code=response.status_code)
    else:
        if response.status_code == api_status_codes.HTTP_413_REQUEST_ENTITY_TOO_LARGE:
            raise APIException(
                "The model is too large. Please contact us for workarounds."
            )
        raise APIException("Unexpected HTTP content type on failure response.")


def get_model(model_id: int, config: ClientConfig = None) -> api_pb.Model:
    """
    Get info about an uploaded model.

    Parameters
    ----------
    model_id : int
        Model ID.
    config : ClientConfig
        API authentication configuration.

    Returns
    -------
    model_pb : Model
        Model info as protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("models", str(model_id), config=config)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.Model, obj_id=model_id)


def get_model_list(
    offset: int = 0, limit: int | None = None, config: ClientConfig = None
) -> api_pb.ModelList:
    """
    Get list of models visible to the authenticated user.


    Parameters
    ----------
    offset : int
        Offset the query.
    limit : int
        Limit query response size.

    Returns
    -------
    list_pb : ModelList
        Model list as protobuf object.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("models", config=config)
    url += utils.prepare_offset_limit_query(offset, limit)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    return utils.response_as_protobuf(response, api_pb.ModelList)


def download_model(model_id: int, file: str, config: ClientConfig = None) -> None:
    """
    Download a previously uploaded model.

    Parameters
    ----------
    model_id : int
        Model ID.
    file : str
        file location to store model to
    config : ClientConfig
        API authentication configuration.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    url = utils.api_url("models", str(model_id), "download", config=config)
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    if api_status_codes.is_success(response.status_code):
        with open(file, "wb") as fn:
            fn.write(response.content)
    else:
        raise APIException(status_code=response.status_code)


def download_artifacts(job_id: int, dir_name: str, config: ClientConfig = None) -> None:
    """
    Download all job artifacts to directory.

    Parameters
    ----------
    job_id : int
        Job ID.
    dir_name : str
        file location to store artifact to
    config : ClientConfig
        API authentication configuration.

    Raises
    ------
    APIException
        Raised if request has failed.
    """
    if config is None:
        config = utils.load_default_api_config()
    dir_name = os.path.abspath(dir_name)
    # fetch compiled model
    url = utils.api_url(
        "profile_jobs", str(job_id), "download_compiled_model", config=config
    )
    header = utils.auth_header(config=config)
    response = requests.get(url, headers=header)
    if api_status_codes.is_success(response.status_code):
        cd = response.headers["content-disposition"]
        base_name = re.findall('filename="(.+)"', cd)[0]
        with open(os.path.join(dir_name, base_name), "wb") as fn:
            fn.write(response.content)
    else:
        raise APIException(status_code=response.status_code)


__all__ = [
    "utils",
    "APIException",
    "ClientConfig",
    "Device",
    "Shapes",
    "get_auth_user",
    "get_user",
    "get_user_list",
    "get_device_list",
    "create_profile_job",
    "get_profile_job",
    "get_profile_job_list",
    "get_profile_job_results",
    "upload_model",
    "download_model",
    "download_artifacts",
    "get_model",
    "get_model_list",
]
