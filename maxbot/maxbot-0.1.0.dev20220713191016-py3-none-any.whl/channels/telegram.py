from typing import Any

from telegram import Bot, Update

from ..schemas import Message
from ._base import ChannelEvent


def TelegramShim(bot):
    def shim(update: Update, telegram_bot: Bot):
        event = create_event(update, telegram_bot)
        if event is not None:
            for command in bot(event):
                command_executor(command, event, telegram_bot)

    return shim


def create_event(update: Update, bot: Bot):
    message = message_factory(update, bot)
    if message is not None:
        return ChannelEvent("telegram", update.effective_user.id, message)


def message_factory(update: Update, bot: Bot):
    if update.message and update.message.text:
        return Message().load({"text": update.message.text})


def command_executor(command: Any, event: ChannelEvent, bot: Bot):
    if command.name == "text":
        bot.send_message(event.user_id, command.text)
    else:
        raise RuntimeError(f"Could not execute {command}")
