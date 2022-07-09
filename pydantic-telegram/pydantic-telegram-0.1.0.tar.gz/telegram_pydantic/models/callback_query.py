from pydantic import Field, BaseModel
from telegram_pydantic.models.user import User
from telegram_pydantic.models.message import Message


class CallbackQuery(BaseModel):
    id: str
    query_from: User = Field(alias="from")
    message: Message = None
    inline_message_id: str = None
    chat_instance: str = None
    data: str = None
    game_short_name: str = None
