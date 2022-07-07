from __future__ import annotations
from typing import List
from dataclasses import dataclass
from facebookcloudapi.api.dto.inherited import RowObject
from facebookcloudapi.utils import clean_dict


@dataclass
class SectionObject:
    rows: List[RowObject]
    title: str = None

    def validate(self):
        if self.title:
            assert len(self.title) <= 24, "Maximum length: 24 characters"
        assert len(self.rows) <= 10, "You can have a total of 10 rows across your sections"

    def to_dict(self):
        self.validate()
        return clean_dict(self.__dict__)
