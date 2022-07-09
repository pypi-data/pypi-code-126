from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.user import User


class PollAnswer(BaseModel):
    poll_id: str
    user: User
    option_ids: List[int]
