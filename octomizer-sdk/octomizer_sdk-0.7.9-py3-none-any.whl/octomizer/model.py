"""Generic wrapper for Models in the OctoML Platform."""
from __future__ import annotations

import hashlib
import time
import typing

import grpc
import requests
from grpc_status import rpc_status

from octomizer import (
    client,
    model_inputs,
    model_variant,
    package_workflow_group,
    project,
    workflow,
)
from octomizer.logging_ import LOG
from octoml.octomizer.v1 import (
    datarefs_pb2,
    error_pb2,
    hardware_pb2,
    ingest_model_status_pb2,
    model_inputs_pb2,
    models_pb2,
    octomizer_service_pb2,
    workflows_pb2,
)
from octoml.octomizer.v1.ingest_model_status_pb2 import IngestModelStatus as ims

if typing.TYPE_CHECKING:
    from octomizer.project import Project  # Makes mypy happy.

_MODEL_CONTENT_TYPE = "application/octet-stream"

_CHUNK_SIZE = 8388608  # 8MiB chunk size for upload recommended by Google

DEFAULT_JOB_TIMEOUT_SECONDS = 1200
"""The default number of seconds to wait for a job to finish."""

DEFAULT_JOB_POLL_INTERVAL_SECONDS = 5
"""The default number of seconds to wait between polling for job statuses."""


class ModelCreationError(RuntimeError):
    pass


class Model:
    """Represents a generic Model in the OctoML Platform."""

    _TERMINAL_STATES = {
        ims.Status.COMPLETED,
        ims.Status.FAILED,
    }

    _SUPPORTED_FORMATS = [
        "ONNX",
        "TFLITE",
        "TF_GRAPH_DEF",
        "TF_SAVED_MODEL",
        "TORCHSCRIPT",
    ]

    def __init__(
        self,
        client: client.OctomizerClient,
        name: typing.Optional[str] = None,
        model: typing.Optional[typing.Union[bytes, str]] = None,
        description: typing.Optional[str] = None,
        labels: typing.List[str] = None,
        uuid: typing.Optional[str] = None,
        proto: typing.Optional[models_pb2.Model] = None,
        model_format: typing.Optional[str] = None,
        model_input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        model_input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[project.Project] = None,
        timeout: int = DEFAULT_JOB_TIMEOUT_SECONDS,
        relaxed_ingest: bool = False,
    ):
        """Creates a new Model.

        There are three ways to use this constructor:
          (1) The client passes in a model object, name, description,
              and labels. A new model is created on the service with the given parameters.
          (2) The client passes in a model UUID. An existing model with the given UUID is
              fetched from the service.
          (3) The client provides a fully-populated `models_pb2.Model` protobuf message.

        :param client: an instance of the OctoML client. Required.
        :param name: the name of the model. Required.
        :param model: The model data in the appropriate format, or the name of
            a file containing the model.
        :param description: a description of the model.
        :param labels: tags for the Model.
        :param uuid: UUID of a Model already existing in the OctoML Platform. If provided,
            no other values other than `client` should be specified.
        :param proto: the underyling protobuf object wrapped by this Model. If provided,
            no other values other than `client` should be specified.
        :param model_format: the type of the underlying model. Supported formats:
            onnx, tflite, tf_graph_def (tensorflow graph def), tf_saved_model (includes keras saved model).
        :param model_input_shapes: The model's input shapes in key, value format.
            e.g. {"input0": [1, 3, 224, 224]}.
        :param model_input_dtypes: The model's input dtypes in key, value format.
            e.g. {"input0": "float32"}
        :param project: the Project this model belongs to. Must be `octomizer.project.Project` or None,
            and None when providing the UUID.
        """
        self._client = client
        self._error_message: typing.Optional[str] = None
        if proto is not None:
            # Proto supplied by client.
            assert model is None
            assert name is None
            assert description is None
            assert labels is None
            assert uuid is None
            assert model_format is None
            assert project is None or project.uuid == proto.project_uuid
            self._status = ims.Status.COMPLETED
            self._proto = proto
            if project is not None:
                self._project = project  # type: typing.Optional[Project]
            elif hasattr(self._proto, "project_uuid"):
                self._project = self._get_model_project(self._proto.project_uuid)
            else:
                self._project = None
        elif uuid is not None:
            # We are fetching an existing model from the service.
            assert name is None
            assert description is None
            assert labels is None
            assert proto is None
            assert model_format is None
            assert project is None
            self._status = ims.Status.COMPLETED
            self._proto = self._get_model_by_uuid(uuid)
            self._project = self._get_model_project(self._proto.project_uuid)
        else:
            # We are creating a new Model with the given data.
            assert name is not None
            assert model is not None
            assert model_format is not None
            model_format_proto = self._model_format_to_proto(model_format)
            model_bytes = self._get_model_bytes(model)

            model_input_proto = None
            if model_input_shapes or model_input_dtypes:
                model_input_validation_error = model_inputs.inputs_are_valid(
                    model_input_shapes, model_input_dtypes
                )
                if model_input_validation_error:
                    raise ModelCreationError(model_input_validation_error)
                model_input_proto = model_inputs.inputs_to_input_proto(
                    model_input_shapes, model_input_dtypes
                )

            self._job_uuid = self._upload(
                name,
                model_bytes,
                model_format_proto,
                description,
                labels,
                project.uuid if project is not None else None,
                model_input_proto,
                relaxed_ingest,
            )
            self.wait_for_ingestion(timeout)

            if self.status == ims.Status.FAILED:
                reason = self._error_message or "Unknown"
                msg = f'Model creation failed, job_uuid={self._job_uuid}, reason="{reason}".'
                raise ModelCreationError(msg)
            elif (
                self.status == ims.Status.PENDING
                or self.status == ims.Status.RUNNING
                or self.status == ims.Status.UNKNOWN
            ):
                LOG.error(
                    "Model creation timed out waiting for backend. You can resume waiting by calling model.wait_for_ingestion().",
                )

            self._project = project

    def __str__(self) -> str:
        return str(self._proto)

    def _get_model_by_uuid(self, uuid: str) -> models_pb2.Model:
        """Get the model proto for the given UUID from the OctoML Platform.

        :param uuid: the model UUID to retrieve.
        """
        request = octomizer_service_pb2.GetModelRequest(model_uuid=uuid)
        return self._client.stub.GetModel(request)

    @property
    def proto(self) -> models_pb2.Model:
        """Return the underlying protobuf describing this Model."""
        return self._proto

    @property
    def uuid(self) -> str:
        """Return the UUID for this Model."""
        return self._proto.uuid

    @property
    def project(self) -> typing.Optional[project.Project]:
        """Return the Project this Model belongs to."""
        return self._project

    @property
    def inputs(
        self,
    ) -> typing.Tuple[typing.Dict[str, typing.List[int]], typing.Dict[str, str]]:
        """Return the input shapes and dtypes for this Model. Shapes are
        expected to be positive but -1 can be used as a sentinel when the
        dim is unknown and the user is expected to clarify.
        """
        inputs = self._proto.inputs.input_fields
        input_shapes = {i.input_name: list(i.input_shape) for i in inputs}
        input_dtypes = {i.input_name: i.input_dtype for i in inputs}
        return input_shapes, input_dtypes

    @property
    def status(self) -> ingest_model_status_pb2.IngestModelStatus.Status:
        """Return the status of the IngestModel job."""
        return self._status

    def wait_for_ingestion(
        self, timeout: int = DEFAULT_JOB_TIMEOUT_SECONDS
    ) -> ingest_model_status_pb2.IngestModelStatus:
        try:
            return self._wait(timeout)
        except grpc.RpcError as rpc_error:
            status = rpc_status.from_call(rpc_error)
            for detail in status.details:
                if detail.Is(error_pb2.ErrorDetails.DESCRIPTOR):
                    info = error_pb2.ErrorDetails()
                    detail.Unpack(info)
                    raise ModelCreationError(
                        f"failed model creation: {status.message} {info}"
                    )
            raise rpc_error

    def _wait(
        self, timeout: int = DEFAULT_JOB_TIMEOUT_SECONDS
    ) -> ingest_model_status_pb2.IngestModelStatus:
        resp = self._poll_until_completed(timeout)
        self._status = resp.status
        if self.status == ims.Status.COMPLETED:
            self._proto = self._get_model_by_uuid(resp.model_uuid)
        elif self.status == ims.Status.FAILED and resp.error_details.error_message:
            self._error_message = resp.error_details.error_message
        return resp

    def _upload(
        self,
        name: str,
        model_bytes: bytes,
        model_format: models_pb2.ModelFormat,
        description: typing.Optional[str] = None,
        labels: typing.List[str] = None,
        project_uuid: typing.Optional[str] = None,
        model_inputs: typing.Optional[model_inputs_pb2.ModelInputs] = None,
        relaxed_ingest: typing.Optional[bool] = False,
    ):
        dataref = self.upload_data(self._client, model_bytes, filename=name)

        model_upload_pb = models_pb2.ModelUpload(
            name=name,
            description=description,
            labels=labels,
            source_dataref_uuid=dataref.uuid,
            source_model_format=model_format,
            project_uuid=project_uuid,
            inputs=model_inputs,
        )

        request = octomizer_service_pb2.CreateIngestModelRequest(
            model_upload=model_upload_pb, relaxed_ingest=relaxed_ingest
        )

        try:
            proto = self._client.stub.CreateIngestModel(request)
            return proto.uuid
        except grpc.RpcError as rpc_error:
            status = rpc_status.from_call(rpc_error)
            for detail in status.details:
                if detail.Is(error_pb2.ErrorDetails.DESCRIPTOR):
                    info = error_pb2.ErrorDetails()
                    detail.Unpack(info)
                    raise ModelCreationError(
                        f"failed model upload: {status.message} {info}"
                    )
            raise rpc_error

    def _get_status(self) -> ingest_model_status_pb2.IngestModelStatus:
        req = octomizer_service_pb2.GetIngestModelStatusRequest(uuid=self._job_uuid)
        return self._client.stub.GetIngestModelStatus(req)

    def _poll_until_completed(  # type: ignore
        self,
        timeout: int = DEFAULT_JOB_TIMEOUT_SECONDS,
        poll_interval: int = DEFAULT_JOB_POLL_INTERVAL_SECONDS,
    ) -> ingest_model_status_pb2.IngestModelStatus:
        """Waits until this Job has finished or the given timeout has elapsed.

        :param uuid: uuid of the Job we are polling
        :param timeout: the number of seconds to wait for this Job.
        :param poll_interval: the number of seconds to wait between polling for the
            status of this job.
        :return: the terminal state of this job.
        """
        status = ingest_model_status_pb2.IngestModelStatus(
            uuid=self._job_uuid,
            status=ingest_model_status_pb2.IngestModelStatus.Status.UNKNOWN,
        )
        start_time = time.time()

        while status.status not in self._TERMINAL_STATES:
            if time.time() - start_time > timeout:
                break
            status = self._get_status()
            time.sleep(poll_interval)

        return status

    def get_model_variant(self, uuid: str) -> model_variant.ModelVariant:
        """Retrieves the ModelVariant with the given id associated with this Model.

        :param uuid: the id of the ModelVariant to retrieve.
        :return: the ModelVariant associated with this Model that has the given id.
        """
        request = octomizer_service_pb2.GetModelVariantRequest(
            model_variant_uuid=uuid,
        )
        response = self._client.stub.GetModelVariant(request)
        return model_variant.ModelVariant(
            client=self._client,
            uuid=response.uuid,
            model=self,
            proto=response,
        )

    def get_uploaded_model_variant(self) -> model_variant.ModelVariant:
        """Returns the original, uploaded ModelVariant for this Model."""
        assert self._proto is not None
        return self.get_model_variant(self._proto.uploaded_model_variant_uuid)

    def list_model_variants(self) -> typing.Iterator[model_variant.ModelVariant]:
        """Retrieves all ModelVariants associated with this Model.

        :return: all ModelVariants associated with this Model.
        """
        page_token = None
        while True:
            request = octomizer_service_pb2.ListModelVariantsRequest(
                model_uuid=self.uuid,
                page_size=self._client._PAGE_SIZE,
                page_token=page_token,
            )
            response = self._client.stub.ListModelVariants(request)

            for model_variant_proto in response.model_variants:
                yield model_variant.ModelVariant(
                    client=self._client,
                    uuid=model_variant_proto.uuid,
                    model=self,
                    proto=model_variant_proto,
                )

            page_token = response.next_page_token
            if not page_token:
                break

    def get_workflow(self, uuid: str) -> workflow.Workflow:
        """Deprecated. Retrieves the Workflow with the given id associated with this Model.

        :param uuid: the id of the Workflow to retrieve.
        :return: the Workflow associated with this Model that has the given id.
        """
        LOG.warn(
            "This method will be deprecated. Please use the `OctomizerClient.get_workflow` instead."
        )
        return self._client.get_workflow(uuid)

    def list_workflows(self) -> typing.Iterator[workflow.Workflow]:
        """Retrieves all Workflows associated with this Model.

        :return: all Workflows associated with this Model.
        """
        page_token = None
        while True:
            request = octomizer_service_pb2.ListWorkflowsRequest(
                model_uuid=self.uuid,
                page_size=self._client._PAGE_SIZE,
                page_token=page_token,
            )
            response = self._client.stub.ListWorkflows(request)

            for workflow_proto in response.workflows:
                yield workflow.Workflow(client=self._client, proto=workflow_proto)

            page_token = response.next_page_token
            if not page_token:
                break

    def _model_format_to_proto(self, model_format: str) -> models_pb2.ModelFormat:
        model_format = model_format.upper()
        if model_format not in self._SUPPORTED_FORMATS:
            formats = ",".join([x.lower() for x in self._SUPPORTED_FORMATS])
            msg = (
                f"Unsupported model format: {model_format}."
                f"Supported formats are: {formats}."
            )
            raise ModelCreationError(msg)
        return models_pb2.ModelFormat.Value(model_format)

    def _get_model_bytes(self, model: typing.Union[bytes, str]) -> bytes:
        if isinstance(model, str):
            with open(model, "rb") as f:
                model_bytes = f.read()
                return model_bytes
        else:
            return model

    def _get_model_project(
        self, project_uuid: typing.Optional[str] = None
    ) -> typing.Optional[Project]:
        if not project_uuid:
            return None

        return project.Project(self._client, uuid=project_uuid)

    def create_package_workflow_group(
        self, package_workflow_group_spec: workflows_pb2.PackageWorkflowGroup
    ) -> package_workflow_group.PackageWorkflowGroup:
        """Creates a new PackageWorkflowGroup for this Model.

        :param package_workflow_group_spec: the specification for the PackageWorkflowGroup to be created.
        :return: the new PackageWorkflowGroup.
        """
        request = octomizer_service_pb2.CreatePackageWorkflowGroupRequest(
            package_workflow_group=package_workflow_group_spec
        )
        response = self._client.stub.CreatePackageWorkflowGroup(request)
        LOG.warning(
            f"started package_workflow_group: {response.uuid}. You'll be emailed when all Workflows have finished."
        )
        return package_workflow_group.PackageWorkflowGroup(self._client, proto=response)

    def create_packages(
        self,
        platform: str,
        acceleration_mode: workflows_pb2.AccelerationMode = workflows_pb2.AccelerationMode.AUTO,
        input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
        package_name: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, str]] = None,
    ) -> package_workflow_group.PackageWorkflowGroup:
        """Create packages for this Model. This is a convenience function that creates a
        PackageWorkflowGroup with Workflows created from available tuners and runtimes.

        :param platform: The hardware platform to target. Available platforms can be queried
            via the `get_hardware_targets` method on an OctomizerClient. If you would like to
            benchmark on other hardware platforms, please submit a feature request
            `here <https://octoml.atlassian.net/servicedesk/customer/portal/6>`_.
        :param acceleration_mode: The acceleration mode to use for the PackageWorkflowGroup.
            There are currently two modes:
             - AUTO (default): Default settings search
             - EXPRESS: Non-exhaustive search
        :param input_shapes: dict mapping input name to shape. Must be provided if
            input_dtypes is provided.
        :param input_dtypes: dict mapping input name to dtype. Must be provied if
            input_shapes is provided.
        :param package_name: The name of the package. If unset or empty, will default
            to the name of the model. Note: Non-alphanumeric characters in the name will
            be replaced with underscores ('_') and trailing/leading underscores will be
            stripped. Valid package names must only contain lower case letters, numbers,
            and single (non leading/trailing) underscores ('_').
        :param metadata: Metadata tagged onto PackageWorkflowGroup and its Workflows.
        """
        model_inputs_proto = model_variant.ModelVariant._get_model_inputs_proto(
            input_shapes, input_dtypes
        )

        if package_name:
            model_variant.ModelVariant._validate_package_name(package_name)

        proto = workflows_pb2.PackageWorkflowGroup(
            model_uuid=self.uuid,
            model_variant_uuid=self._proto.uploaded_model_variant_uuid,
            acceleration_mode=acceleration_mode,
            model_inputs=model_inputs_proto,
            hardware=hardware_pb2.HardwareSpec(
                platform=platform,
            ),
            package_name=package_name,
            metadata=metadata,
        )
        return self.create_package_workflow_group(proto)

    @staticmethod
    def _upload_to_url(url: str, data: bytes, sha256: str):
        """Puts the given data to the given url.

        :param url: the url where the data should be put.
        :param data: the data put to the given url.
        :param sha256: the sha256 hash of the data.
        :raise: requests.HTTPError if the request fails.
        """
        # TODO OCTO-394: URL and required headers should be expressed in proto,
        # to allow more than just GCS as a blob storage option.

        # First initiate the upload session
        response = requests.post(url=url, headers={"x-goog-resumable": "start"})
        response.raise_for_status()

        if "Location" in response.headers:
            session_url = response.headers["Location"]
        else:
            raise KeyError(
                "'Location' header missing in GCS session initiation response!"
            )

        # Now do the actual upload in multiple chunks
        iter_start = 0
        data_size = len(data)
        remaining = data_size
        while remaining > 0:
            iter_total = iter_start + _CHUNK_SIZE
            iter_end = iter_total if iter_total < data_size else data_size
            iter_size = iter_end - iter_start
            chunk = data[iter_start:iter_end]
            response = requests.put(
                url=session_url,
                data=chunk,
                headers={
                    "Content-Length": str(iter_size),
                    "Content-Range": "bytes {}-{}/{}".format(
                        iter_start, iter_end - 1, data_size
                    ),
                },
            )

            if response.status_code == requests.codes.resume_incomplete:
                remaining = remaining - iter_size
                iter_start = iter_start + iter_size
                # compare to what the Google thinks
                rrange = response.headers["range"]
                last_loaded = int(rrange.split("-")[1]) + 1
                assert last_loaded == iter_start
            elif response.ok:
                # finished
                break
            else:
                # error
                response.raise_for_status()

    @staticmethod
    def upload_data(
        client: client.OctomizerClient,
        model_bytes: bytes,
        filename: str = "",
    ):
        # Calc the sha256 hash of the given bytes representing a model.
        sha256 = hashlib.sha256()
        sha256.update(model_bytes)
        model_sha256 = sha256.hexdigest()

        dataref_request = octomizer_service_pb2.CreateDataRefRequest(
            dataref=datarefs_pb2.DataRef(
                content_type=_MODEL_CONTENT_TYPE,
                sha256=model_sha256,
                size=len(model_bytes),
                filename=filename,
            )
        )
        response = client.stub.CreateDataRef(dataref_request)
        dataref = response.dataref

        # Upload the model's contents to the location tracked by the dataref.
        Model._upload_to_url(response.upload_url, model_bytes, model_sha256)

        return dataref
