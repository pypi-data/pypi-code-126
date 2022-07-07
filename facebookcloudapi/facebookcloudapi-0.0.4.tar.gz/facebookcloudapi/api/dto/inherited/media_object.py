from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict


@dataclass
class MediaObject:
    media_id: str = None
    link: str = None
    caption: str = None
    filename: str = None
    provider: str = None

    def to_dict(self):
        d = clean_dict(self.__dict__)
        d["id"] = d["media_id"]
        del d["media_id"]
        return d
