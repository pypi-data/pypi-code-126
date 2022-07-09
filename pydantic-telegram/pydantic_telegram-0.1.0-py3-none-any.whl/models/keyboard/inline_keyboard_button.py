from pydantic import BaseModel
from telegram_pydantic.models.login_url import LoginUrl
from telegram_pydantic.models.games.callback_game import CallbackGame


class InlineKeyboardButton(BaseModel):
    text: str
    url: str = None
    login_url: LoginUrl = None
    callback_data: str = None
    switch_inline_query: str = None
    switch_inline_query_current_chat: str = None
    callback_game: CallbackGame = None
    pay: bool = None
