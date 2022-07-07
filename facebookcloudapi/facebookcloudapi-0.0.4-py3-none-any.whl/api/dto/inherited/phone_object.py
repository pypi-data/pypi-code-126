from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.api.dto.types.contact_type import ContactType
from facebookcloudapi.utils import clean_dict


@dataclass
class PhoneObject:
    phone: str = None
    phone_type: str = None
    wa_id: str = None

    def to_dict(self):
        d = clean_dict(self.__dict__)
        value = d["phone_type"]
        d["type"] = value
        del d["phone_type"]
        return d
