from pydantic import BaseModel
from telegram_pydantic.models.user import User


class ChatMember(BaseModel):
    user: User
    status: str
    custom_title: str = None
    is_anonymous: bool = None
    can_be_edited: bool = None
    can_manage_chat: bool = None
    can_post_messages: bool = None
    can_edit_messages: bool = None
    can_delete_messages: bool = None
    can_manage_voice_chats: bool = None
    can_restrict_members: bool = None
    can_promote_members: bool = None
    can_change_info: bool = None
    can_invite_users: bool = None
    can_pin_messages: bool = None
    is_member: bool = None
    can_send_messages: bool = None
    can_send_media_messages: bool = None
    can_send_polls: bool = None
    can_send_other_messages: bool = None
    can_add_web_page_previews: bool = None
    until_date: int = None
