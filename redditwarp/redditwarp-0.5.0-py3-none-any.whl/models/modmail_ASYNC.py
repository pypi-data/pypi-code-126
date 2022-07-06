
from __future__ import annotations
from typing import TYPE_CHECKING, Mapping, Any
if TYPE_CHECKING:
    from ..client_ASYNC import Client

from .modmail_base import (
    BaseConversation,
    BaseMessage,
    BaseModmailModAction,
    BaseUserDossier,
    GBaseConversationAggregate,
    GBaseUserDossierConversationAggregate,
    GBaseOptionalUserDossierConversationAggregate,
)

class Conversation(BaseConversation):
    def __init__(self, d: Mapping[str, Any], client: Client):
        super().__init__(d)
        self.client: Client = client

    async def reply(self, body: str, *, hidden: bool = False, internal: bool = False) -> ConversationAggregate:
        return await self.client.p.modmail.conversation.reply(self.id, body, hidden=hidden, internal=internal)

    async def mark_read(self) -> None:
        await self.client.p.modmail.conversation.mark_read(self.id)

    async def mark_unread(self) -> None:
        await self.client.p.modmail.conversation.mark_unread(self.id)


class Message(BaseMessage):
    def __init__(self, d: Mapping[str, Any], client: Client):
        super().__init__(d)
        self.client: Client = client

class ModmailModAction(BaseModmailModAction):
    pass

class UserDossier(BaseUserDossier):
    pass


class ConversationAggregate(GBaseConversationAggregate[Conversation, Message, ModmailModAction]):
    pass

class UserDossierConversationAggregate(GBaseUserDossierConversationAggregate[Conversation, Message, ModmailModAction, UserDossier]):
    pass

class OptionalUserDossierConversationAggregate(GBaseOptionalUserDossierConversationAggregate[Conversation, Message, ModmailModAction, UserDossier]):
    pass
