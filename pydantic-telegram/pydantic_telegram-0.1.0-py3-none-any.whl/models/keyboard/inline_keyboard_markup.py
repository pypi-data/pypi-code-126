from typing import List

from pydantic import BaseModel
from telegram_pydantic.models.keyboard.inline_keyboard_button import InlineKeyboardButton


class InlineKeyboardMarkup(BaseModel):
    inline_keyboard: List[InlineKeyboardButton]
