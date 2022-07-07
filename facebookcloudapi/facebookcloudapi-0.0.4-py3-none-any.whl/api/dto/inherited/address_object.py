from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.api.dto.types.contact_type import ContactType
from facebookcloudapi.utils import clean_dict


@dataclass
class AddressObject:
    street: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    country: str = None
    country_code: str = None
    contact_type: ContactType = None

    def to_dict(self):
        d = clean_dict(self.__dict__)
        value = d["contact_type"]
        d["type"] = value
        del d["contact_type"]
        return d
