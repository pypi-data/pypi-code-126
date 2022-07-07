from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict
from facebookcloudapi.api.dto.types import HeaderType
from facebookcloudapi.api.dto.inherited import MediaObject


@dataclass
class HeaderObject:
    header_type: HeaderType
    text: str = None
    video: MediaObject = None
    image: MediaObject = None
    document: MediaObject = None

    def validate(self):
        if self.text:
            assert len(self.text) <= 60, "Maximum length: 60 characters"

    def to_dict(self):
        self.validate()
        d = clean_dict(self.__dict__)
        d["type"] = d["header_type"]
        del d["header_type"]
        return d
