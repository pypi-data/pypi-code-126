from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.utils import clean_dict
from facebookcloudapi.api.dto.types import ButtonType


@dataclass
class ButtonObject:
    title: str
    button_id: str
    button_type: ButtonObject = ButtonType.REPLY

    def validate(self):
        assert self.button_type == ButtonType.REPLY, "only supported type is reply (for Reply Button)"
        assert len(self.title) > 0 and len(
            self.title) <= 20, "It cannot be an empty string and must be unique within the message. Emojis are supported, markdown is not. Maximum length: 20 characters."

    def to_dict(self):
        self.validate()
        d = clean_dict(self.__dict__)
        d["type"] = d["button_type"]
        del d["button_type"]
        d["id"] = d["button_id"]
        del d["button_id"]
        return d
