from pydantic import Field, BaseModel
from telegram_pydantic.models.user import User
from telegram_pydantic.models.location import Location


class ChosenInlineResult(BaseModel):
    result_id: str
    result_from: User = Field(alias="from")
    location: Location = None
    inline_message_id: str = None
    query: str
