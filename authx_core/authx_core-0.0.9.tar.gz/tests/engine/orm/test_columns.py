import logging
import time
from copy import deepcopy
from typing import TYPE_CHECKING, Iterator, Type

import pytest
import sqlalchemy as sa
from _pytest.logging import LogCaptureFixture
from _pytest.monkeypatch import MonkeyPatch
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_409_CONFLICT

from authx_core._async import (
    authxAsyncContextSession,
    authxAsyncGetEngine,
    authxAsyncGetSession,
)
from authx_core.database import authxSetupDatabase, authxSetupDatabaseMetadata
from authx_core.engine.orm import (
    authxBase,
    authxJson,
    authxPrimaryKey,
    created_at_column,
    updated_at_column,
)
from authx_core.errors import authxRaiseIntegrityError
from authx_core.utils import authxClearCaches

if TYPE_CHECKING:

    class JsonModel(authxBase):
        id1 = authxPrimaryKey()
        id2 = authxPrimaryKey()
        json = authxJson(nullable=False)
        created_at = created_at_column()
        updated_at = updated_at_column()


@pytest.fixture(scope="module")
def monkeypatch_module() -> Iterator[MonkeyPatch]:
    from _pytest.monkeypatch import MonkeyPatch

    m = MonkeyPatch()
    yield m
    m.undo()


@pytest.fixture(scope="module")
def engine(monkeypatch_module: MonkeyPatch) -> sa.engine.Engine:
    sqlalchemy_database_url = "sqlite:///./test.db"
    monkeypatch_module.setenv("DB_SQLALCHEMY_URL", sqlalchemy_database_url)
    monkeypatch_module.setenv("DB_LOG_SQLALCHEMY_SQL_STATEMENTS", "1")

    authxClearCaches()

    return authxAsyncGetEngine()


@pytest.fixture(scope="module")
def json_model(engine: sa.engine.Engine) -> "Type[JsonModel]":
    if TYPE_CHECKING:
        global JsonModel
    if not TYPE_CHECKING:

        class JsonModel(authxBase):
            id1 = authxPrimaryKey()
            id2 = authxPrimaryKey()
            json = authxJson(nullable=False)
            created_at = created_at_column()
            updated_at = updated_at_column()

    authxSetupDatabase(engine)
    authxSetupDatabaseMetadata(authxBase.metadata, engine)
    authxBase.metadata.create_all(bind=engine)
    return JsonModel


def test_columns(json_model: "Type[JsonModel]") -> None:
    db: Session = authxAsyncGetSession()

    json_value = {"hello": "world"}

    instance = json_model(json=json_value)
    db.add(instance)
    db.commit()
    assert instance.json == json_value
    db.close()

    updated_at = deepcopy(instance.updated_at)
    assert instance.created_at == instance.updated_at
    time.sleep(1)

    new_db = authxAsyncGetSession()
    new_db.add(instance)
    instance.json = {"goodbye": "world"}
    new_db.commit()
    assert instance.json != json_value
    assert instance.created_at < instance.updated_at
    assert updated_at < instance.updated_at
    new_db.close()


@pytest.mark.asyncio
@pytest.mark.skip(reason="TODO: fix this test")
def test_sqlalchemy_logging(
    json_model: "Type[JsonModel]", caplog: LogCaptureFixture
) -> None:
    with authxAsyncContextSession() as db:  # pragma: no cover
        json_value = {"hello": "world"}
        instance = json_model(json=json_value)
        db.add(instance)
        assert len(caplog.record_tuples) == 0
        db.commit()
        assert len(caplog.record_tuples) == 4
        db.refresh(instance)
        assert len(caplog.record_tuples) == 7

        for name, level, _message in caplog.record_tuples:
            assert name == "sqlalchemy.engine.Engine"
            assert level == logging.INFO

        id1_str = "".join(str(instance.id1).split("-"))
        id2_str = "".join(str(instance.id2).split("-"))
        assert [x[2] for x in caplog.record_tuples] == [
            "BEGIN (implicit)",
            "INSERT INTO json_model (id1, id2, json) VALUES (?, ?, ?)",
            "('" + f"{id1_str}', '{id2_str}" + '\', \'{"hello": "world"}\')',
            "COMMIT",
            "BEGIN (implicit)",
            "SELECT json_model.id1 AS json_model_id1, json_model.id2 AS json_model_id2, "
            "json_model.json AS json_model_json, json_model.created_at AS "
            "json_model_created_at, json_model.updated_at AS json_model_updated_at \n"
            "FROM json_model \nWHERE json_model.id1 = ? AND json_model.id2 = ?",
            f"('{id1_str}', '{id2_str}' )",
        ]


@pytest.mark.parametrize("raise_error,n_created", [(True, 0), (False, 1)])
def test_raise_integrity_error_rollback(
    json_model: "Type[JsonModel]", raise_error: bool, n_created: int
) -> None:
    with authxAsyncContextSession() as db:
        json_value = {"hello": "world"}
        n_instances = len(db.query(json_model).all())
        instance = json_model(json=json_value)
        db.add(instance)
        if raise_error:
            with pytest.raises(HTTPException) as exc_info:
                authxRaiseIntegrityError(db)
            assert exc_info.value.status_code == HTTP_409_CONFLICT
        db.commit()
        assert len(db.query(json_model).all()) == n_instances + n_created
