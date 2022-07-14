from datetime import datetime
from typing import Protocol, Any, TypeVar, Generic

from pydantic import Field
from pydantic.main import BaseModel


class PageProtocol(Protocol):
    total: int
    offset: int
    limit: int | None
    items: list


B = TypeVar("B", bound="Base")


class Base(BaseModel):
    id: int = Field(
        ...,
        ge=1,
        title="Уникальный идентификатор",
        description="Для однозначного определения объекта",
    )
    created_at: datetime = Field(
        ..., title="Дата создания", description="Когда был создан объект"
    )
    updated_at: datetime = Field(
        ..., title="Дата обновления", description="Когда был обновлен объект"
    )
    is_active: bool = Field(
        ...,
        title="Активность",
        description=(
            "Переключатель активности объекта. Нужно ли его прятать или нет?"
        ),
    )

    class Config:
        orm_mode = True

    @classmethod
    def construct_from_orm(cls: type[B], orm_obj: Any) -> B:
        values = {
            field_name: getattr(orm_obj, field_name)
            for field_name in cls.__fields__.keys()
        }
        return cls.construct(**values)


class BaseUpdate(BaseModel):
    is_active: bool | None = Field(
        None,
        title="Активность",
        description=(
            "Переключатель активности объекта. Нужно ли его прятать или нет?"
        ),
        example=True,
    )


class BasePage(Generic[B], BaseModel):
    total: int = Field(
        ...,
        ge=0,
        title="Всего",
        description=(
            "Количество объектов в базе, подходящих под заданные условия"
        ),
    )
    offset: int = Field(
        ...,
        ge=0,
        title="Отступ",
        description=(
            "Количество объектов в начале списка которые были пропущены"
        ),
    )
    limit: int | None = Field(
        None,
        ge=0,
        title="Лимит",
        description="Количество объектов которое запросили из базы",
    )
    items: list[B]

    @classmethod
    def construct_from_page(cls, page: PageProtocol) -> "BasePage":
        schema: Base = cls.__fields__["items"].type_
        items = [schema.construct_from_orm(item) for item in page.items]
        return cls.construct(
            total=page.total, offset=page.offset, limit=page.limit, items=items
        )
