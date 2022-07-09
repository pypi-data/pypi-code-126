from pydantic import BaseModel
from telegram_pydantic.models.user import User


class ProximityAlertTriggered(BaseModel):
    traveler: User
    watcher: User
    distance: int
