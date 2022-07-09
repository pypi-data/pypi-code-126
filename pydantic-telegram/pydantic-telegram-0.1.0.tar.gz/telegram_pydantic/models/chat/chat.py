from typing import Any

from pydantic import BaseModel
from telegram_pydantic.models.chat.chat_photo import ChatPhoto
from telegram_pydantic.models.chat.chat_location import ChatLocation
from telegram_pydantic.models.chat.chat_permissions import ChatPermissions


class Chat(BaseModel):
    id: int
    type: str
    title: str = None
    username: str = None
    first_name: str = None
    last_name: str = None
    photo: ChatPhoto = None
    bio: str = None
    description: str = None
    invite_link: str = None
    pinned_message: Any = None
    permissions: ChatPermissions = None
    slow_mode_delay: int = None
    message_auto_delete_time: int = None
    sticker_set_name: str = None
    can_set_sticker_set: bool = None
    linked_chat_id: int = None
    location: ChatLocation = None
