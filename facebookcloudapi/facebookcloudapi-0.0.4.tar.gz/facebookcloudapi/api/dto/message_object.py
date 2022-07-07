from __future__ import annotations

from dataclasses import dataclass
from facebookcloudapi.api.dto.types.message_type import MessageType
from facebookcloudapi.utils import clean_dict

@dataclass
class MessageObject:
    message_type: MessageType
    to: str
    recipient_type: str | None = None
    hsm: dict | None = None

    def to_dict(self):
        return clean_dict(self.__dict__)
