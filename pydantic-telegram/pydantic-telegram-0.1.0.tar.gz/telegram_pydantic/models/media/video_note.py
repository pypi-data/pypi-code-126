from pydantic import BaseModel
from telegram_pydantic.models.photo_size import PhotoSize


class VideoNote(BaseModel):
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: PhotoSize = None
    file_size: int = None
