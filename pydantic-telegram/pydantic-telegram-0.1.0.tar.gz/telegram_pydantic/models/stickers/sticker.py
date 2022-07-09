from pydantic import BaseModel
from telegram_pydantic.models.photo_size import PhotoSize
from telegram_pydantic.models.stickers.mask_position import MaskPosition


class Sticker(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    thumb: PhotoSize = None
    emoji: str = None
    set_name: str = None
    mask_position: MaskPosition = None
    file_size: int = None
