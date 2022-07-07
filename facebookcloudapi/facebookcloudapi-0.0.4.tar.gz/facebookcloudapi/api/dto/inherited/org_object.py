from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict


@dataclass
class OrgObject:
    company: str = None
    department: str = None
    title: str = None

    def to_dict(self):
        return clean_dict(self.__dict__)
