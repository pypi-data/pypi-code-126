from pydantic import Field, BaseModel
from telegram_pydantic.models.user import User
from telegram_pydantic.models.chat.chat import Chat
from telegram_pydantic.models.chat.chat_member import ChatMember
from telegram_pydantic.models.chat.chat_invite_link import ChatInviteLink


class ChatMemberUpdated(BaseModel):
    chat: Chat
    update_from: User = Field(alias="from")
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: ChatInviteLink = None
