from __future__ import annotations
from typing import List
from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict
from facebookcloudapi.api.dto.inherited import ButtonObject, SectionObject


@dataclass
class ActionObject:
    button: str = None
    buttons: List[ButtonObject] = None
    sections: List[SectionObject] = None

    def validate(self):
        if self.buttons:
            assert len(self.buttons) <= 3, "You can have up to 3 buttons"
        if self.sections:
            sections_count = len(self.sections)
            assert 1 <= sections_count <= 10, "There is a minimum of 1 and maximum of 10."

    def to_dict(self):
        self.validate()
        d = clean_dict(self.__dict__)
        if "buttons" in d:
            buttons = d["buttons"]
            d["buttons"] = list(map(lambda btn: {
                "type": btn["type"],
                btn["type"]: {
                    "id": btn["id"],
                    "title": btn["title"]
                }
            }, buttons))
        return d
