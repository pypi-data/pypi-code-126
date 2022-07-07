from __future__ import annotations
from datetime import date
from typing import List
from dataclasses import dataclass
from facebookcloudapi.api.dto.inherited import (
    AddressObject, EmailObject, NameObject, OrgObject, PhoneObject, UrlObject
)

from facebookcloudapi.utils import clean_dict


@dataclass
class ContactObject:
    """
    From: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages#contacts-object
    """
    name: NameObject
    addresses: List[AddressObject] = None
    birthday: date | str = None
    emails: List[EmailObject] = None
    org: OrgObject = None
    phones: List[PhoneObject] = None
    urls: List[UrlObject] = None

    def to_dict(self):
        if self.birthday and isinstance(self.birthday, date):
            self.birthday = self.birthday.strftime('%Y-%m-%d')

        return clean_dict(self.__dict__)
