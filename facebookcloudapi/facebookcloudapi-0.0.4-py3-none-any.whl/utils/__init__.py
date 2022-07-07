import dataclasses
from enum import Enum


def clean_list(l: list) -> list:
    new_list = []
    for index, value in enumerate(l):
        if value is None:
            continue
        if isinstance(value, Enum):
            value = value.value
        elif dataclasses.is_dataclass(value):
            to_dict = getattr(value, "to_dict")
            if callable(to_dict):
                value = to_dict()
            else:
                value = value.__dict__

        new_list.append(value)

    return new_list


def clean_dict(d: dict) -> dict:
    for key, value in dict(d).items():

        # Key Checkup
        if isinstance(key, Enum):
            del d[key]
            key = key.value

        # Value Checkup
        if value is None:
            del d[key]
        elif isinstance(value, Enum):
            d[key] = value.value
        elif dataclasses.is_dataclass(value):
            to_dict = getattr(value, "to_dict")
            if callable(to_dict):
                value = to_dict()
            else:
                value = value.__dict__
            d[key] = value
        elif isinstance(value, list):
            d[key] = clean_list(value)
    return d
