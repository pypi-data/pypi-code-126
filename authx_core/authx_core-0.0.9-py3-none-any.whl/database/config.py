import sqlalchemy as sa
from fastapi import FastAPI

from authx_core.database.setup import setup_database, setup_database_metadata
from authx_core.engine import authx_engine
from authx_core.engine.orm import authxBase


def initialize_database(engine: sa.engine.Engine) -> None:
    setup_database(engine)  # pragma: no cover


def get_configured_metadata(_app: FastAPI) -> sa.MetaData:
    """
    This function accepts the app instance as an argument purely as a check to ensure that all resources
    the app depends on have been imported.
    In particular, this ensures the sqlalchemy metadata is populated.
    """
    engine = authx_engine()  # type: ignore # pragma: no cover
    setup_database(engine)  # pragma: no cover
    setup_database_metadata(authxBase.metadata, engine)  # pragma: no cover
    return authxBase.metadata  # pragma: no cover
