import asyncio
import datetime
import logging
from contextlib import contextmanager
from inspect import isclass
from typing import Any, Callable, Dict, Iterator, Tuple, Type, Union

from attrs import Attribute
from attrs.validators import (
    ge,
    gt,
    instance_of,
)



SERIALIZERS_BY_TYPE: Dict[Type[Any], Callable[[Any], str]] = {
    bytes: lambda o: o.decode(),
    bool: str,
    datetime.date: lambda dt: dt.isoformat(),
    datetime.datetime: lambda dt: dt.isoformat(sep='T'),
    datetime.time: lambda dt: dt.isoformat(),
    datetime.timedelta: lambda td: f"{td.total_seconds()} seconds",
    float: str,
    int: str
}


def default_logger(logger: Union[logging.Logger, None]) -> logging.Logger:
    return logger or logging.getLogger(__name__)


def default_loop(
    loop: Union[asyncio.AbstractEventLoop, None]
) -> asyncio.AbstractEventLoop:
    return loop or asyncio.get_event_loop()


def ge_or_none(num: Union[int, float]) -> None:
    def _ge_or_none(inst: object, attr: Attribute, value: Any) -> None:
        if value is not None:
            ge(num)(inst, attr, value)
    return _ge_or_none


def gt_or_none(num: Union[int, float]) -> None:
    def _gt_or_none(inst: object, attr: Attribute, value: Any) -> None:
        if value is not None:
            gt(num)(inst, attr, value)
    return _gt_or_none


def instance_of_or_none(types: Union[Any, Tuple[Any]]) -> None:
    def _instance_of_or_none(inst: object, attr: Attribute, value: Any) -> None:
        if value is not None:
            instance_of(types)(inst, attr, value)
    return _instance_of_or_none


def serialize_arbitrary_to_str(value: Any) -> str:
    if isinstance(value, str):
        return value
    for base in value.__class__.__mro__[:-1]:
        try:
            serializer = SERIALIZERS_BY_TYPE[base]
        except KeyError:
            continue
        return serializer(value)
    try:
        return serialize_user_obj_to_str(value)
    except ValueError:
        pass
    raise TypeError(
        f"Unable to serialize obj of type {type(value)} to str"
    )


def serialize_user_obj_to_str(obj: Any) -> str:
    if isclass(obj):
        raise ValueError(f"Uninstantiated type {obj.__name__}")
    try:
        if type(obj).__str__ is not object.__str__:
            return obj.__str__()
    except AttributeError:
        pass
    raise ValueError("Value must have user implemented '__str__' method")


@contextmanager
def toggle_bool(inst: object, attr: str) -> Iterator[None]:
    try:
        if hasattr(inst, attr):
            setattr(inst, attr, False)
        yield
    finally:
        if hasattr(inst, attr):
            setattr(inst, attr, True)