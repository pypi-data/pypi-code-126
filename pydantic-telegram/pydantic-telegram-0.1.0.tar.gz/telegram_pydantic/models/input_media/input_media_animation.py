from typing import Any, Optional

from telegram_pydantic.models.input_media.input_media import InputMedia


class InputMediaAnimation(InputMedia):
    thumb: Optional[Any]
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
