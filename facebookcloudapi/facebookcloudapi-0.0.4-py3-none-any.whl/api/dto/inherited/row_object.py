from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.api.dto.types.contact_type import ContactType
from facebookcloudapi.utils import clean_dict


@dataclass
class RowObject:
    row_id: str
    row_title: str
    row_description: str = None

    def validate(self):
        assert len(self.row_id) <= 200, 'Maximum length: 200 characters'
        assert len(self.row_title) <= 24, 'Maximum length: 24 characters'
        if self.row_description:
            assert len(self.row_description) <= 72, 'Maximum length: 72 characters'

    def to_dict(self):
        self.validate()
        d = clean_dict(self.__dict__)
        d["id"] = d["row_id"]
        d["title"] = d["row_title"]
        d["description"] = d["row_description"]
        del d["row_id"]
        del d["row_title"]
        del d["row_description"]
        return d
