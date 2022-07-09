from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.user import User


class VoiceChatParticipantsInvited(BaseModel):
    users: List[User]
