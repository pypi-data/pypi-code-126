from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.api.dto.types.contact_type import ContactType
from facebookcloudapi.utils import clean_dict


@dataclass
class FooterObject:
    text: str

    def to_dict(self):
        return clean_dict(self.__dict__)
