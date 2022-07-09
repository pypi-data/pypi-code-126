from pydantic import BaseModel
from telegram_pydantic.models.message import Message
from telegram_pydantic.models.poll.poll import Poll
from telegram_pydantic.models.callback_query import CallbackQuery
from telegram_pydantic.models.poll.poll_answer import PollAnswer
from telegram_pydantic.models.payments.shipping_query import ShippingQuery
from telegram_pydantic.models.chat.chat_member_updated import ChatMemberUpdated
from telegram_pydantic.models.inline_mode.inline_query import InlineQuery
from telegram_pydantic.models.payments.pre_checkout_query import PreCheckoutQuery
from telegram_pydantic.models.inline_mode.chosen_inline_result import ChosenInlineResult


class MessageUpdate(BaseModel):
    update_id: int
    message: Message = None
    edited_message: Message = None
    channel_post: Message = None
    edited_channel_post: Message = None
    inline_query: InlineQuery = None
    chosen_inline_result: ChosenInlineResult = None
    callback_query: CallbackQuery = None
    shipping_query: ShippingQuery = None
    pre_checkout_query: PreCheckoutQuery = None
    poll: Poll = None
    poll_answer: PollAnswer = None
    my_chat_member: ChatMemberUpdated = None
    chat_member: ChatMemberUpdated = None
