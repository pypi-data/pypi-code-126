from pydantic import BaseModel


class ChatPermissions(BaseModel):
    can_send_messages: bool = None
    can_send_media_messages: bool = None
    can_send_polls: bool = None
    can_send_other_messages: bool = None
    can_add_web_page_previews: bool = None
    can_change_info: bool = None
    can_invite_users: bool = None
    can_pin_messages: bool = None
