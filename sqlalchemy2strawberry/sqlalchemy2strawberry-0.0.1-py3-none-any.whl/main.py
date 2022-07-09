from typing import Container, Optional, Sequence, Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic_sqlalchemy.main import OrmConfig
from strawberry.experimental.pydantic import type as strawberry_type


def sqlalchemy2strawberry(sql_model: Type, *, exclude: Container[str] = []):
    pydantic_model = sqlalchemy_to_pydantic(sql_model, exclude=exclude)
    return strawberry_type(pydantic_model)
