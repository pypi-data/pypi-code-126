from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.photo_size import PhotoSize
from telegram_pydantic.models.message_entity import MessageEntity
from telegram_pydantic.models.media.animation import Animation


class Game(BaseModel):
    title: str
    description: str
    photo: List[PhotoSize]
    text: str
    text_entities: List[MessageEntity]
    animation: Animation
