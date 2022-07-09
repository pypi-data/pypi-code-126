from pydantic import BaseModel
from telegram_pydantic.models.user import User


class ChatInviteLink(BaseModel):
    invite_link: str
    creator: User
    is_primary: bool
    is_revoked: bool
    expire_date: int
    member_limit: int
