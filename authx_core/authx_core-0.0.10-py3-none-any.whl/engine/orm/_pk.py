from typing import Any, Dict, Optional, Type, TypeVar, Union, overload
from uuid import UUID, uuid4

import sqlalchemy as sa

from authx_core import GUID, authxBackend, authxDatabaseSettings

IdentifierT = TypeVar("IdentifierT", bound=UUID)


@overload
def pk_column(id_type: Type[IdentifierT]) -> "sa.Column[IdentifierT]":
    ...


@overload
def pk_column(id_type: None = None) -> "sa.Column[UUID]":
    ...


def pk_column(
    id_type: Optional[Type[IdentifierT]] = None,
) -> "Union[sa.Column[IdentifierT], sa.Column[UUID]]":
    """
    The server-default value should be updated in the metadata later
    """
    using_postgres = authxDatabaseSettings().backend == authxBackend.postgresql
    default_kwargs: Dict[str, Any] = (
        {"server_default": sa.text("gen_random_uuid()")}
        if using_postgres
        else {"default": uuid4}
    )

    return sa.Column(GUID, primary_key=True, index=True, **default_kwargs)
