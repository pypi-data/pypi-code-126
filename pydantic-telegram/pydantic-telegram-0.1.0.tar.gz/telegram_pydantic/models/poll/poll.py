from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.poll.poll_option import PollOption
from telegram_pydantic.models.message_entity import MessageEntity


class Poll(BaseModel):
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: str
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int = None
    explanation: str = None
    explanation_entities: List[MessageEntity] = None
    open_period: int = None
    close_date: int = None
