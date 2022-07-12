import uuid
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Tuple

from globus_action_provider_tools import (
    ActionProviderJsonEncoder,
    ActionRequest,
    ActionStatus,
)


class PersistenceJsonEncoder(ActionProviderJsonEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        else:
            return super(PersistenceJsonEncoder, self).default(obj)


ActionProviderPersistenceReturnType = Tuple[
    Optional[ActionStatus], Optional[ActionRequest], Optional[Dict[str, Any]]
]


class ActionProviderPersistence(ABC):
    @abstractmethod
    async def lookup_by_action_id(
        self, action_id: str
    ) -> ActionProviderPersistenceReturnType:
        ...

    @abstractmethod
    async def lookup_by_request_id_and_identity(
        self, request_id: str, user_identity: str
    ) -> ActionProviderPersistenceReturnType:
        ...

    @abstractmethod
    async def store_action(
        self,
        action: ActionStatus,
        request: Optional[ActionRequest] = None,
        creator_id: Optional[str] = None,
        extra_data: Optional[Dict[str, Any]] = None,
    ) -> ActionProviderPersistenceReturnType:
        ...

    @abstractmethod
    async def remove_action(
        self, action_id: str
    ) -> ActionProviderPersistenceReturnType:
        ...
