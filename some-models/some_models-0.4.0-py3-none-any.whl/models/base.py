from dataclasses import dataclass
from typing import Any, TypeVar, Generic

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    DateTime,
    MetaData,
    delete,
    update,
    select,
)
from sqlalchemy.orm import Session, as_declarative
from sqlalchemy.sql import func, Select
from sqlalchemy_utils import force_auto_coercion

from some_models.constants import naming_convention
from some_models.exceptions import ObjectNotFoundInDBError

force_auto_coercion()

B = TypeVar("B", bound="Base")

metadata = MetaData(naming_convention=naming_convention)


@dataclass(frozen=True, slots=True)
class Page(Generic[B]):
    total: int
    offset: int
    limit: int | None
    items: list[B]


@as_declarative(metadata=metadata)
class Base:
    id = Column(
        Integer,
        primary_key=True,
        doc="Уникальный идентификатор",
    )
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        doc="Время создания",
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        server_onupdate=func.now(),
        doc="Время обновления",
    )
    is_active = Column(Boolean, nullable=False, default=True, doc="Активна?")

    # __table_args__ = {"schema": "some_schema"}

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self) -> str:
        fields = ", ".join(
            f"{k}={v!r}"
            for k, v in self.__dict__.items()
            if not k.startswith("_")
        )
        return f"{self.__class__.__name__}({fields})"

    @classmethod
    def _get_select_with_where(cls, **kwargs: Any) -> Select:
        """Добавляет все фильтры к запросу в базу данных"""
        stmt = select(cls)
        for field_name, value_for_filter in kwargs.items():
            class_field = getattr(cls, field_name, False)
            if class_field:
                stmt = stmt.where(class_field == value_for_filter)
        return stmt

    @classmethod
    def _get_objects_with_offset_limit(
        cls: type[B],
        session: Session,
        stmt: Select,
        offset: int = 0,
        limit: int | None = 50,
    ) -> list[B]:
        """Для получения объектов с пагинацией"""
        return session.scalars(stmt.offset(offset).limit(limit)).all()

    @classmethod
    def get_list(cls: type[B], session: Session, **kwargs: Any) -> list[B]:
        """Для фильтрации без пагинации"""
        stmt = cls._get_select_with_where(**kwargs)
        return cls._get_objects_with_offset_limit(session, stmt, 0, None)

    @classmethod
    def get_page(
        cls: type[B],
        session: Session,
        offset: int = 0,
        limit: int | None = 50,
        **kwargs: Any,
    ) -> Page[B]:
        """Для фильтрации с пагинацией"""

        stmt = cls._get_select_with_where(**kwargs)
        total = session.scalar(select(func.count()).where(stmt.whereclause))
        items = cls._get_objects_with_offset_limit(
            session, stmt, offset, limit
        )
        return Page(total, offset, limit, items)

    @classmethod
    def create(cls: type[B], session: Session, data: dict) -> B:
        """Для сохранения объекта в базу"""
        item = cls(**data)
        with session.begin():
            session.add(item)
        return item

    @classmethod
    def update(cls: type[B], session: Session, id_: int, data: dict) -> B:
        """Для обновления объекта в базе"""
        stmt = update(cls).where(cls.id == id_).values(**data).returning(cls)
        orm_stmt = (
            select(cls)
            .from_statement(stmt)
            .execution_options(populate_existing=True)
        )
        return session.execute(orm_stmt).scalar_one()

    @classmethod
    def delete(cls, session: Session, id_: int) -> None:
        """Для удаления объекта из базы"""
        if session.execute(delete(cls).where(cls.id == id_)).rowcount < 1:
            raise ObjectNotFoundInDBError(f"Объект с {id_ = } не найден")
