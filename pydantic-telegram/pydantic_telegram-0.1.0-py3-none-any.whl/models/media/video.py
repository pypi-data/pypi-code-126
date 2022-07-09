from pydantic import BaseModel
from telegram_pydantic.models.photo_size import PhotoSize


class Video(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize = None
    file_name: str = None
    mime_type: str = None
    file_size: int = None
