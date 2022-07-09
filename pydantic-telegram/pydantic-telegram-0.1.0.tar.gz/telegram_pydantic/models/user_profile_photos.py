from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.photo_size import PhotoSize


class UserProfilePhotos(BaseModel):
    total_count: int
    photos: List[PhotoSize]
