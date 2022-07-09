from typing import Any, Optional

from telegram_pydantic.models.input_media.input_media import InputMedia


class InputMediaVideo(InputMedia):
    thumb: Optional[Any]
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
    supports_streaming: Optional[bool]
