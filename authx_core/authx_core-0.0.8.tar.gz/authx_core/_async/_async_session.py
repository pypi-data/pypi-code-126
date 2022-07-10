import logging
from contextlib import contextmanager
from functools import lru_cache
from typing import Iterator, Optional

import sqlalchemy as sa
from sqlalchemy.orm import Session

from authx_core.settings._backend import authxBackend
from authx_core.settings._database import get_database_settings as authxDatabaseSettings


@lru_cache()
def get_engine() -> sa.engine.Engine:
    db_settings = authxDatabaseSettings()
    url = db_settings.sqlalchemy_url
    log_sqlalchemy_sql_statements = db_settings.log_sqlalchemy_sql_statements
    database_backend = db_settings.backend
    return get_new_engine(url, log_sqlalchemy_sql_statements, database_backend)


@lru_cache()
def get_sessionmaker() -> sa.orm.sessionmaker:
    return get_sessionmaker_for_engine(get_engine())


def get_new_engine(
    url: str,
    log_sqlalchemy_sql_statements: bool = False,
    database_backend: authxBackend = authxBackend.postgresql,
) -> sa.engine.Engine:
    if log_sqlalchemy_sql_statements:
        logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    else:
        logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)
    kwargs = {}
    if database_backend == authxBackend.sqlite:
        kwargs.update({"connect_args": {"check_same_thread": False}})
    return sa.create_engine(url, pool_pre_ping=True, **kwargs)


def get_sessionmaker_for_engine(engine: sa.engine.Engine) -> sa.orm.sessionmaker:
    return sa.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> sa.orm.Session:
    return get_sessionmaker()()


@contextmanager
def context_session(engine: Optional[sa.engine.Engine] = None) -> Iterator[Session]:
    yield from _get_db(engine)


def get_db() -> Iterator[Session]:
    """
    Intended for use as a FastAPI dependency
    """
    yield from _get_db()


def _get_db(engine: Optional[sa.engine.Engine] = None) -> Iterator[Session]:
    if engine is None:
        session = get_session()
    else:
        session = get_sessionmaker_for_engine(engine)()
    try:
        yield session
        session.commit()
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()
