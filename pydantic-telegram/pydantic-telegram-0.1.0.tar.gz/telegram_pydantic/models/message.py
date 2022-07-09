from __future__ import annotations
from typing import List

from pydantic import Field, BaseModel
from telegram_pydantic.models.user import User
from telegram_pydantic.models.venue import Venue
from telegram_pydantic.models.location import Location
from telegram_pydantic.models.chat.chat import Chat
from telegram_pydantic.models.poll.poll import Poll
from telegram_pydantic.models.games.game import Game
from telegram_pydantic.models.media.dice import Dice
from telegram_pydantic.models.photo_size import PhotoSize
from telegram_pydantic.models.media.audio import Audio
from telegram_pydantic.models.media.video import Video
from telegram_pydantic.models.media.voice import Voice
from telegram_pydantic.models.media.contact import Contact
from telegram_pydantic.models.media.document import Document
from telegram_pydantic.models.message_entity import MessageEntity
from telegram_pydantic.models.media.animation import Animation
from telegram_pydantic.models.media.video_note import VideoNote
from telegram_pydantic.models.payments.invoice import Invoice
from telegram_pydantic.models.stickers.sticker import Sticker
from telegram_pydantic.models.passport.passport_data import PassportData
from telegram_pydantic.models.proximity_alert_triggered import ProximityAlertTriggered
from telegram_pydantic.models.payments.successful_payment import SuccessfulPayment
from telegram_pydantic.models.voice_chat.voice_chat_ended import VoiceChatEnded
from telegram_pydantic.models.voice_chat.voice_chat_started import VoiceChatStarted
from telegram_pydantic.models.keyboard.inline_keyboard_markup import InlineKeyboardMarkup
from telegram_pydantic.models.voice_chat.voice_chat_scheduled import VoiceChatScheduled
from telegram_pydantic.models.message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from telegram_pydantic.models.voice_chat.voice_chat_participants_invited import VoiceChatParticipantsInvited


class Message(BaseModel):
    message_id: int
    message_from: User = Field(alias="from", default=None)
    sender_chat: Chat = None
    date: int
    chat: Chat
    forward_from: User = None
    forward_from_chat: Chat = None
    forward_from_message_id: int = None
    forward_signature: str = None
    forward_sender_name: str = None
    forward_date: int = None
    reply_to_message: Message = None
    via_bot: User = None
    edit_date: int = None
    media_group_id: str = None
    author_signature: str = None
    text: str = None
    entities: List[MessageEntity] = None
    animation: Animation = None
    audio: Audio = None
    document: Document = None
    photo: List[PhotoSize] = None
    sticker: Sticker = None
    video: Video = None
    video_note: VideoNote = None
    voice: Voice = None
    caption: str = None
    caption_entities: List[MessageEntity] = None
    contact: Contact = None
    dice: Dice = None
    game: Game = None
    poll: Poll = None
    venue: Venue = None
    location: Location = None
    new_chat_members: List[User] = None
    left_chat_member: User = None
    new_chat_title: str = None
    new_chat_photo: List[PhotoSize] = None
    delete_chat_photo: bool = None
    group_chat_created: bool = None
    supergroup_chat_created: bool = None
    channel_chat_created: bool = None
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged = None
    migrate_to_chat_id: int = None
    migrate_from_chat_id: int = None
    pinned_message: Message = None
    invoice: Invoice = None
    successful_payment: SuccessfulPayment = None
    connected_website: str = None
    passport_data: PassportData = None
    proximity_alert_triggered: ProximityAlertTriggered = None
    voice_chat_scheduled: VoiceChatScheduled = None
    voice_chat_started: VoiceChatStarted = None
    voice_chat_ended: VoiceChatEnded = None
    voice_chat_participants_invited: VoiceChatParticipantsInvited = None
    reply_markup: InlineKeyboardMarkup = None


Message.update_forward_refs()
