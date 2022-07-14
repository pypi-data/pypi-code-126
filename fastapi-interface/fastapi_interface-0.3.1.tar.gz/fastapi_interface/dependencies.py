from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol

from fastapi import Query, Path, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from pydantic import ValidationError

from fastapi_interface.constants import DEFAULT_OFFSET, DEFAULT_LIMIT
from fastapi_interface.schemas.user import User

http_bearer = HTTPBearer()


class SettingsProtocol(Protocol):
    PUBLIC_KEY: str
    ALGORITHM: str


class CurrentUserDependency:
    def __init__(self, settings: SettingsProtocol):
        self.settings = settings

    async def __call__(
        self,
        token: HTTPAuthorizationCredentials = Depends(http_bearer),
    ) -> User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token.credentials,
                self.settings.PUBLIC_KEY,
                algorithms=[self.settings.ALGORITHM],
            )
        except JWTError:
            raise credentials_exception

        user_json: str | None = payload.get("sub")
        if user_json is None:
            raise credentials_exception

        try:
            user = User.parse_raw(user_json)
        except ValidationError:
            raise credentials_exception

        return user


def get_dependency_for_current_active_user(
    current_user_dependency: CurrentUserDependency,
) -> Callable[[User], User]:
    def get_current_active_user(
        current_user: User = Depends(current_user_dependency),
    ) -> User:
        if not current_user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user

    return get_current_active_user


# TODO попробуй dataclass
# class PaginationQueryParams:
#     def __init__(
#         self,
#         offset: int = Query(
#             DEFAULT_OFFSET,
#             ge=0,
#             title="Отступ",
#             description="Для пагинации.
#             Сколько объектов пропустить с начала?",
#         ),
#         limit: int
#         | None = Query(
#             DEFAULT_LIMIT,
#             ge=0,
#             title="Лимит",
#             description="Для пагинации. Сколько объектов выбрать?",
#         ),
#     ):
#         self.offset = offset
#         self.limit = limit


@dataclass
class PaginationQueryParams:
    offset: int = Query(
        DEFAULT_OFFSET,
        ge=0,
        title="Отступ",
        description="Для пагинации. Сколько объектов пропустить с начала?",
    )
    limit: int | None = Query(
        DEFAULT_LIMIT,
        ge=0,
        title="Лимит",
        description="Для пагинации. Сколько объектов выбрать?",
    )


def get_id_query_param(
    id_: int
    | None = Query(
        None,
        alias="id",
        ge=1,
        title="Уникальный идентификатор",
        description="Объект с каким id выбрать?",
    )
):
    return id_


def get_id_path_param(id_: int = Path(..., alias="id", ge=1)):
    return id_
