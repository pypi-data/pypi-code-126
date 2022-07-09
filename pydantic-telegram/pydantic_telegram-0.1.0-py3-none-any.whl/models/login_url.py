from pydantic import BaseModel


class LoginUrl(BaseModel):
    url: str
    forward_text: str = None
    bot_username: str = None
    request_write_access: bool = None
