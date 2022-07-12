import datetime
import json
import logging
from contextlib import asynccontextmanager
from typing import Any, Dict, Optional, Set, Type, TypeVar

from globus_action_provider_tools import ActionRequest, ActionStatus, ActionStatusValue
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

from .async_helpers import await_if_needed
from .persistence import (
    ActionProviderPersistence,
    ActionProviderPersistenceReturnType,
    PersistenceJsonEncoder,
)

log = logging.getLogger(__name__)

_action_property_conversions = {
    "status": lambda x: ActionStatusValue[x],
}

T = TypeVar("T", bound=BaseModel)


def _copy_into(
    src_model: BaseModel, dest_model: BaseModel, omits: Optional[Set[str]] = None
) -> BaseModel:
    for k, v in src_model:
        if omits and k not in omits:
            setattr(dest_model, k, v)
    return dest_model


def _json_to_object(json_val: Optional[str], model_class: Type[T]) -> Optional[T]:
    if json_val is None:
        return None
    props = json.loads(json_val)
    for val_to_convert, convert_fn in _action_property_conversions.items():
        model_val = props.get(val_to_convert)
        if model_val is not None:
            props[val_to_convert] = convert_fn(model_val)
    return model_class(**props)


class ActionTableModel(SQLModel, table=True):
    __tablename__ = "GlobusActions"
    action_id: str = Field(primary_key=True)
    request_id: str = Field(index=True)
    creator: str = Field(index=True)
    completion_time: Optional[datetime.datetime]
    action_status_json: str
    request_json: Optional[str]
    extra_data_json: Optional[str]

    def to_persistence_return_type(self) -> ActionProviderPersistenceReturnType:
        action_status = _json_to_object(self.action_status_json, ActionStatus)
        request = _json_to_object(self.request_json, ActionRequest)
        extra_data = _json_to_object(self.extra_data_json, dict)
        return (action_status, request, extra_data)


class SQLModelProviderPersistence(ActionProviderPersistence):
    def __init__(
        self,
        sessionmaker,
        use_async=False,
    ):
        self.sessionmaker = sessionmaker
        self.use_async = use_async

    @classmethod
    def create_engine(cls, db_url: str, create_tables=False, **kwargs):
        engine = create_engine(db_url, **kwargs)
        if create_tables:
            cls.create_tables(engine)
        return engine

    @classmethod
    def create_tables(cls, engine) -> None:
        SQLModel.metadata.create_all(engine)

    @classmethod
    async def async_create_engine(cls, db_url: str, create_tables=False, **kwargs):
        from sqlalchemy.ext.asyncio import create_async_engine

        engine = create_async_engine(db_url, future=True, **kwargs)
        if create_tables:
            await cls.async_create_tables(engine)
        return engine

    @classmethod
    async def async_create_tables(cls, engine) -> None:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    @asynccontextmanager
    async def get_session(self, **kwargs) -> Session:
        session = self.sessionmaker(**kwargs)
        try:
            yield session
            await await_if_needed(session.commit())
        except Exception:
            await await_if_needed(session.rollback())
            raise
        finally:
            session.close()

    async def lookup_by_id(
        self, session: Session, model_class: Type, id_val: Any
    ) -> Any:
        model = session.get(model_class, id_val)
        if isinstance(model, BaseModel) or model is None:
            return model
        return await model

    async def lookup_by_action_id(
        self, action_id: str
    ) -> ActionProviderPersistenceReturnType:
        async with self.get_session(expire_on_commit=False) as session:
            table_model = await self.lookup_by_id(session, ActionTableModel, action_id)
            if table_model is None:
                return (None, None, None)
            else:
                return table_model.to_persistence_return_type()

    async def lookup_by_request_id_and_identity(
        self, request_id: str, user_identity: str
    ) -> ActionProviderPersistenceReturnType:
        async with self.get_session(expire_on_commit=False) as session:
            table_model = (
                await await_if_needed(
                    session.exec(
                        select(ActionTableModel).where(
                            ActionTableModel.request_id == request_id
                            and ActionTableModel.creator == user_identity
                        )
                    )
                )
            ).first()
            if table_model is None:
                return (None, None, None)
            else:
                return table_model.to_persistence_return_type()

    async def store_action(
        self,
        action: ActionStatus,
        request: Optional[ActionRequest] = None,
        creator_id: Optional[str] = None,
        extra_data: Optional[Dict[str, Any]] = None,
    ) -> ActionProviderPersistenceReturnType:
        action_json = json.dumps(action, cls=PersistenceJsonEncoder)

        if request is not None:
            request_json = json.dumps(request, cls=PersistenceJsonEncoder)
            request_id = request.request_id
        else:
            request_json = None
            request_id = None
        if extra_data is not None:
            extra_data_json = json.dumps(extra_data, cls=PersistenceJsonEncoder)
        else:
            extra_data_json = None

        table_model = ActionTableModel(
            action_id=action.action_id,
            action_status_json=action_json,
            request_id=request_id,
            request_json=request_json,
            creator=creator_id,
            completion_time=action.completion_time,
            extra_data_json=extra_data_json,
        )

        rvals: ActionProviderPersistenceReturnType = (None, None, None)
        async with self.get_session() as session:
            current_entry: ActionTableModel = await self.lookup_by_id(
                session, ActionTableModel, action.action_id
            )
            if current_entry is not None:
                # The action, the completion time, and the extra data are the
                # only mutable fields
                current_entry.action_status_json = action_json
                current_entry.completion_time = action.completion_time
                current_entry.extra_data_json = extra_data_json
                session.add(current_entry)
                rvals = current_entry.to_persistence_return_type()
            else:
                session.add(table_model)
                rvals = table_model.to_persistence_return_type()
            session.commit()
        return rvals

    async def remove_action(
        self, action_id: str
    ) -> ActionProviderPersistenceReturnType:
        async with self.get_session(expire_on_commit=False) as session:
            table_model = await self.lookup_by_id(session, ActionTableModel, action_id)
            if table_model is not None:
                await await_if_needed(session.delete(table_model))

                return table_model.to_persistence_return_type()
            else:
                return (None, None, None)
