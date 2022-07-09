from pydantic import BaseModel
from telegram_pydantic.models.photo_size import PhotoSize


class Document(BaseModel):
    file_id: str
    file_unique_id: str
    thumb: PhotoSize = None
    file_name: str = None
    mime_type: str = None
    file_size: int = None
