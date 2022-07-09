from pydantic import BaseModel
from telegram_pydantic.models.location import Location


class ChatLocation(BaseModel):
    location: Location
    address: str
