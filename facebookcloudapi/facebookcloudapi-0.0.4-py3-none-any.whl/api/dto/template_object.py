from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict


@dataclass
class TemplateObject:
    name: str
    language: dict
    namespace: str = None
    components: list = None

    def to_dict(self):
        return clean_dict(self.__dict__)
