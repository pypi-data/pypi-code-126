from typing import Any, Optional

from telegram_pydantic.models.input_media.input_media import InputMedia


class InputMediaAudio(InputMedia):
    thumb: Optional[Any]
    duration: Optional[int]
    performer: Optional[str]
    title: Optional[str]
