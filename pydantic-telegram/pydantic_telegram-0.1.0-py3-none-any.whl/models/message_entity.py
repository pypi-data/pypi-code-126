from pydantic import BaseModel
from telegram_pydantic.models.user import User


class MessageEntity(BaseModel):
    type: str
    offset: int
    length: int
    url: str = None
    user: User = None
    language: str = None
