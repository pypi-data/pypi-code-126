from typing import Any, Optional

from pydantic import BaseModel, Field

from telegram_pydantic.models.message_entity import MessageEntity


class InputMedia(BaseModel):
    media_type: str = Field(alias="type")
    media: Any
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[MessageEntity]
