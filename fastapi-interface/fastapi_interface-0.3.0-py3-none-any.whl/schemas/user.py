from pydantic import EmailStr, BaseModel

from fastapi_interface.schemas.base import Base


class BaseUser(BaseModel):
    username: str
    email: EmailStr


class User(BaseUser, Base):
    password: str
