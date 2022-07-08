from uuid import uuid4

from pydantic import BaseModel, Field, EmailStr


def _generate_user_id() -> str:
    return str(uuid4())


class User(BaseModel):
    """Model for SFC Users."""

    id: str = Field(default_factory=_generate_user_id)
    enabled: bool = True
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jane.doe@testmail.com",
                "password": "somepassword",
            }
        }


class UserLoginSchema(BaseModel):
    """Model for User login"""

    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {"email": "jane.doe@testmail.com", "password": "somepassword"}
        }


class UserAbstractUpdateSchema(BaseModel):
    """Abstract model for updating a User."""

    password: str = Field(...)


class UserPassUpdateSchema(UserAbstractUpdateSchema):
    new_password: str = Field(...)


class UserUpdateSchema(UserAbstractUpdateSchema):
    new_email: str = Field(...)
