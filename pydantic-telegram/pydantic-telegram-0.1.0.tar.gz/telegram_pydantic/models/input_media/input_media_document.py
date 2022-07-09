from typing import Any, Optional

from telegram_pydantic.models.input_media.input_media import InputMedia


class InputMediaDocument(InputMedia):
    thumb: Optional[Any]
    disable_content_type_detection: Optional[bool]
