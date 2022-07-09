from pydantic import BaseModel
from telegram_pydantic.models.photo_size import PhotoSize


class Audio(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    performer: str = None
    title: str = None
    file_name: str = None
    mime_type: str = None
    file_size: int = None
    thumb: PhotoSize = None
