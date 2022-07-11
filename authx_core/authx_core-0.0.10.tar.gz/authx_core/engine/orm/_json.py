from typing import Any, Dict, TypeVar
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

from authx_core import authxBackend, authxDatabaseSettings

IdentifierT = TypeVar("IdentifierT", bound=UUID)


def json_column(*, nullable: bool) -> "sa.Column[Dict[str, Any]]":
    using_postgres = authxDatabaseSettings().backend == authxBackend.postgresql
    column_type = JSONB() if using_postgres else sa.JSON()
    return sa.Column(column_type, nullable=nullable)  # type: ignore
