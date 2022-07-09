from dataclasses import asdict, is_dataclass
from typing import Any, Dict, List, cast

from tabulate import tabulate

from .errors import InvalidDataFormatError

_is_pydantic_installed = True

try:
    from pydantic import BaseModel
except ImportError:
    _is_pydantic_installed = False


def is_dict(obj: Any) -> bool:
    return isinstance(obj, dict)


def is_pydantic(obj: Any) -> bool:
    if not _is_pydantic_installed:
        return False

    return isinstance(obj, BaseModel)


def is_popo(obj: Any) -> bool:
    return hasattr(obj, "__dict__")


def normalize(data: List[Any]) -> List[Dict]:
    normalized: List[Dict] = []

    for obj in data:
        if is_dict(obj):
            obj = cast(dict, obj)
            normalized.append(obj)
            continue

        if is_pydantic(obj):
            obj = cast(BaseModel, obj)
            normalized.append(obj.dict())
            continue

        if is_dataclass(obj):
            normalized.append(asdict(obj))
            continue

        if is_popo(obj):
            normalized.append(vars(obj))
            continue

        raise InvalidDataFormatError(f"Kuromon cannot handle {type(obj)}")

    return normalized


def to_table(data: List[Any], *, index: bool = True, tablefmt="github") -> str:
    """Convert a list of dict, dataclass or Pydantic objects into a string represented table

    Args:
        data (List[Any]): A list of dict, dataclass or Pydantic objects
        index (bool, optional): Whether to show index or not. Defaults to True.
        tablefmt (str, optional): A table format. Defaults to "github".

    Returns:
        str: A string represented table
    """
    if not isinstance(data, list):
        raise InvalidDataFormatError("data should be a list of objects")

    normalized = normalize(data)
    return tabulate(normalized, headers="keys", showindex=index, tablefmt=tablefmt)
