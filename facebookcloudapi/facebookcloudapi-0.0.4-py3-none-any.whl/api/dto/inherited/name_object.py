from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict


@dataclass
class NameObject:
    formatted_name: str
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    suffix: str = None
    prefix: str = None

    def to_dict(self):
        return clean_dict(self.__dict__)
