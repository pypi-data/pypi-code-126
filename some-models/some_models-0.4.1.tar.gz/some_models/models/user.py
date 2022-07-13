from sqlalchemy import Column, String, Boolean, select
from sqlalchemy.orm import relationship, Session
from sqlalchemy_utils import EmailType, PasswordType

from some_models.models.base import Base


class User(Base):
    __tablename__ = "user"

    username = Column(String, nullable=False, unique=True)
    password = Column(
        PasswordType(schemes=["bcrypt"]), nullable=False, unique=True
    )
    email = Column(EmailType, nullable=False, unique=True)
    is_superuser = Column(Boolean, nullable=False, default=False)

    purchases = relationship("Purchase", back_populates="user")

    @classmethod
    def get_by_username(cls, session: Session, username: str) -> "User":
        return session.execute(
            select(cls).where(cls.username == username)
        ).scalar_one()
