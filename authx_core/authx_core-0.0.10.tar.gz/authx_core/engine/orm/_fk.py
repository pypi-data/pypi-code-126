from typing import Optional, TypeVar, Union, overload
from uuid import UUID

import sqlalchemy as sa
from typing_extensions import Literal

from authx_core import GUID

IdentifierT = TypeVar("IdentifierT", bound=UUID)


@overload
def fk_column(
    column: Union[str, "sa.Column[IdentifierT]"],
    nullable: Literal[True],
    index: bool = False,
    primary_key: bool = False,
    unique: bool = False,
) -> "sa.Column[Optional[IdentifierT]]":
    ...


@overload
def fk_column(
    column: Union[str, "sa.Column[IdentifierT]"],
    nullable: Literal[False] = False,
    index: bool = False,
    primary_key: bool = False,
    unique: bool = False,
) -> "sa.Column[IdentifierT]":
    ...


def fk_column(
    column: Union[str, "sa.Column[IdentifierT]"],
    nullable: bool = False,
    index: bool = False,
    primary_key: bool = False,
    unique: bool = False,
) -> "Union[sa.Column[IdentifierT], sa.Column[Optional[IdentifierT]]]":
    return sa.Column(  # type: ignore # pragma: no cover
        GUID,
        sa.ForeignKey(column, ondelete="CASCADE"),
        index=index,
        nullable=nullable,
        primary_key=primary_key,
        unique=unique,
    )
