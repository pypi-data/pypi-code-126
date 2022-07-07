from __future__ import annotations
from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict


@dataclass
class LocationObject:
    """
    From: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages#interactive-object
    """
    longitude: str
    latitude: str
    name: str = None
    address: str = None

    def to_dict(self):
        d = clean_dict(self.__dict__)
        return d
