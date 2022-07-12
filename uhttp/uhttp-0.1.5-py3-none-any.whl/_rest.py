import copy
import functools
import inspect
import re
from inspect import Parameter
from typing import (
    Any,
    Callable,
    Dict,
    List,
    OrderedDict,
    Set,
    Tuple,
    Type
)

from attrs import define, field
from attrs.validators import instance_of
from attrs import NOTHING as UseExisting

from ._enums import HttpMethod
from ._exceptions import QueryParamConversionError
from ._models import URL
from ._util import serialize_arbitrary_to_str



def normalize_path(path: str) -> str:
    if not isinstance(path, str):
        return path
    splits = path.split('/')
    normalized = '/' + '/'.join([split for split in splits if split])
    return normalized


def builder(
    func: Callable[[Any], Any],
    merged_path: str,
    merged_cast: Dict[str, Type["QueryParam"]],
    default_query_type: Type["QueryParam"]
) -> Tuple[URL, HttpMethod]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> URL:
        func(*args, **kwargs)
        target = parse_endpoint_func_parameters(
            func,
            merged_path,
            merged_cast,
            default_query_type,
            args,
            kwargs
        )
        return URL(target)
    return wrapper


def parse_endpoint_func_parameters(
    func: Callable[[Any], Any],
    merged_path: str,
    merged_cast: Dict[str, Type["QueryParam"]],
    default_query_type: Type["QueryParam"],
    args: Tuple[Any],
    kwargs: Dict[str, Any] 
) -> str:
    args = list(args)
    path_params = set(re.findall(r"\{(.[^${}]*)}", merged_path))
    func_params = inspect.signature(func).parameters
    interpolated_path = interpolate_path_params(
        merged_path,
        path_params,
        func_params,
        args,
        kwargs
    )
    query_params = get_query_params(path_params, func_params, args, kwargs)
    casted = cast_query_params(query_params, merged_cast, default_query_type, kwargs)
    try:
        stringified = [param.to_str() for param in casted]
    except Exception as err:
        raise QueryParamConversionError(err)
    query_str = '&'.join(stringified)
    if query_str:
        target = interpolated_path + '?' + query_str
    else:
        target = interpolated_path
    return target


def interpolate_path_params(
    path: str,
    path_params: Set[str],
    func_params: OrderedDict[str, Parameter],
    args: List[Any],
    kwargs: Dict[str, Any]
) -> str:
    matched_params = {}
    path_params_copy = copy.copy(path_params)
    for i, (name, param) in enumerate(func_params.items()):
        if name in path_params_copy:
            if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
                raise ValueError(
                    "Path parameters cannot be variable positional or "
                    "variable keyword arguments"
                )
            path_params_copy.remove(name)
            if param.kind in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD):
                try:
                    path_param_val = args.pop(i)
                except IndexError:
                    if name in kwargs:
                        path_param_val = kwargs.pop(name)
                    else:
                        path_param_val = param.default
            else:
                if name in kwargs:
                    path_param_val = kwargs.pop(name)
                else:
                    path_param_val = param.default
            matched_params[name] = serialize_arbitrary_to_str(path_param_val)
    if path_params_copy:
        raise ValueError(f"Unmatched path params: {', '.join(path_params_copy)}")
    interpolated_path = path
    for path_param, val in matched_params.items():
        key = '{' + path_param + '}'
        interpolated_path = interpolated_path.replace(key, val)
    return interpolated_path


def get_query_params(
    path_params: Set[str],
    func_params: OrderedDict[str, Parameter],
    args: List[Any],
    kwargs: Dict[str, Any]
) -> List[str]:
    query_params = []
    for _, (name, param) in enumerate(func_params.items()):
        if name.lower() == 'self' or name.lower() == 'cls':
            continue
        elif name in path_params:
            continue
        elif param.kind == param.VAR_POSITIONAL:
            continue
        elif param.kind == param.VAR_KEYWORD:
            return query_params
        elif param.kind in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD):
            try:
                kwargs.update({name: args.pop(0)})
            except IndexError:
                if name not in kwargs:
                    kwargs.update({name: param.default})
            query_params.append(name)
        else:
            if name not in kwargs:
                kwargs.update({name: param.default})
            query_params.append(name)
    return query_params

def cast_query_params(
    query_params: List[str],
    cast: Dict[str, Type["QueryParam"]],
    default_query_type: Type["QueryParam"],
    kwargs: Dict[str, Any]
) -> List["QueryParam"]:
    casted = []
    for param in query_params:
        val = kwargs.pop(param)
        if val is not None:
            query_type = cast.pop(param, None)
            query_type = query_type or default_query_type
            casted.append(query_type(param, val))
    return casted


@define
class Endpoint:
    path: str = field(
        default='/', converter=normalize_path, validator=instance_of(str)
    )
    cast: Dict[str, Type["QueryParam"]] = field(
        factory=dict, validator=instance_of(dict)
    )

    def merge(self, endpoint: "Endpoint") -> None:
        root_path = endpoint.path
        merged_path = root_path + self.path
        self.path = merged_path
        self.cast.update(endpoint.cast)


@define(slots=False)
class QueryParam:
    """
    Container defining the key-value pair of a query parameter. Sub class this
    and implement the `to_str` method to change how the output is formatted

    Parameters
    - key (str): the key in the key-value pair for a query param
    - val (Any): the value in the key-value pair for a query param. This class
    will attempt to convert the value to a string during formatting
    """
    key: str = field(validator=instance_of(str))
    val: Any = field()

    def to_str(self):
        return f"{self.key}={serialize_arbitrary_to_str(self.val)}"


@define
class RestApi:
    """
    Helper class for defining endpoints as first class functions

    Any method can be decorated with any of HTTP method decorators. The decorated
    method defines path and/or query parameters as positional or keyword
    arguments

    Parameters
    - base_path (str): the path of url. Variable path parameters in the method
    defintion can be added as path parameters by using {<var>} in the path
    string where <var> is the name of the variable in the method definition
    - always_cast (Dict[str, Type[QueryParam]]): a dictionary specifying method
    arguments to be casted to a specific query parameter type. By default all
    query parameters are casted to the `default_query_type`
    - default_query_type (Type[QueryParam]): the default query type for all
    parameters not specified in cast
    """
    base_path: str = field(
        default='/', converter=normalize_path, validator=instance_of(str)
    )
    always_cast: Dict[str, Type[QueryParam]] = field(
        factory=dict, validator=instance_of(dict)
    )
    default_query_type: Type[QueryParam] = field(default=QueryParam)
    _base_endpoint: Endpoint = field(default=None, init=False)

    def __attrs_post_init__(self) -> None:
        self._base_endpoint = Endpoint(self.base_path, self.always_cast)

    @default_query_type.validator
    def _subclasses_query_param(self, _, query_type: Type[QueryParam]) -> None:
        if not issubclass(query_type, QueryParam):
            raise TypeError("`default_query_type` must subclass `QueryParam`")
    
    def endpoint(
        self,
        path: str = '/',
        cast: Dict[str, Type[QueryParam]] = {},
        default_query_type: Type[QueryParam] = UseExisting
    ) -> URL:
        model = Endpoint(path, cast)
        model.merge(self._base_endpoint)
        if default_query_type is UseExisting:
            default_query_type = self.default_query_type
        def wrapper(func: Callable[[Any], None]) -> URL:
            return builder(
                func,
                model.path,
                model.cast,
                default_query_type
            )
        return wrapper