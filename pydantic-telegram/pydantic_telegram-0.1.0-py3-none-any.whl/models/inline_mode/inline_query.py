from pydantic import Field, BaseModel
from telegram_pydantic.models.user import User
from telegram_pydantic.models.location import Location


class InlineQuery(BaseModel):
    id: str
    query_from: User = Field(alias="from")
    query: str
    offset: str
    chat_type: str = None
    location: Location = None
