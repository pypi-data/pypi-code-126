import copy
from contextlib import contextmanager
from dataclasses import dataclass, fields

from sqlalchemy import (
    JSON,
    Column,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
    engine_from_config,
    select,
)
from sqlalchemy.orm import Session, declarative_base, relationship
from sqlalchemy.pool import StaticPool

Base = declarative_base()


class ChannelUser(Base):
    __tablename__ = "channel_user"

    channel_user_id = Column(Integer, primary_key=True)
    channel = Column(String, nullable=False)
    user_id = Column(String, nullable=False)

    variables = relationship(
        lambda: UserVariable,
        backref="user",
        cascade="all, delete-orphan",
        order_by=lambda: UserVariable.variable_id,
    )

    __table_args__ = (UniqueConstraint("channel", "user_id"),)


class UserVariable(Base):
    __tablename__ = "user_variable"

    variable_id = Column(Integer, primary_key=True)
    channel_user_id = Column(
        Integer, ForeignKey("channel_user.channel_user_id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String, nullable=False)
    value = Column(JSON, nullable=False)

    __table_args__ = (UniqueConstraint("channel_user_id", "name"),)


class SQLAlchemyStore:
    def __init__(self, config=None):
        if config:
            self.engine = engine_from_config(config.__dict__, prefix="", future=True)
        else:
            # by default we create in-memory db that supports multithreading
            self.engine = create_engine(
                "sqlite://",
                future=True,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool,
            )

        Base.metadata.create_all(self.engine, checkfirst=True)

    @contextmanager
    def __call__(self, event):
        with Session(self.engine) as session:
            stmt = (
                select(ChannelUser)
                .where(ChannelUser.channel == event.channel)
                .where(ChannelUser.user_id == str(event.user_id))
                .with_for_update()
            )
            user = session.scalars(stmt).one_or_none()
            if user is None:
                user = ChannelUser(channel=event.channel, user_id=str(event.user_id))
                session.add(user)

            # make a deep copy to allow sqlalchemy track changes by
            # comparing with original values
            kv_pairs = [(v.name, copy.deepcopy(v.value)) for v in user.variables]
            variables = Variables.from_kv_pairs(kv_pairs)
            yield variables
            existing = {v.name: v for v in user.variables}
            for name, value in variables.to_kv_pairs():
                if name in existing:
                    var = existing.pop(name)
                    if value is None:
                        user.variables.remove(var)
                    else:
                        var.value = value
                elif value is not None:
                    var = UserVariable(name=name, value=value)
                    user.variables.append(var)
            # variables that not in kv_pairs anymore must be deleted
            for var in existing.values():
                user.variables.remove(var)
            session.commit()


@dataclass(frozen=True)
class Variables:
    user: dict
    slots: dict
    flow: dict

    @classmethod
    def from_kv_pairs(cls, kv_pairs):
        data = {f.name: {} for f in fields(cls)}
        for name, value in kv_pairs:
            ns, name = name.split(".", 1)
            assert ns in data, f"Unknown ns {ns}"
            data[ns][name] = value
        return cls(**data)

    def to_kv_pairs(self):
        for f in fields(self):
            for name, value in getattr(self, f.name).items():
                name = f"{f.name}.{name}"
                yield name, value
