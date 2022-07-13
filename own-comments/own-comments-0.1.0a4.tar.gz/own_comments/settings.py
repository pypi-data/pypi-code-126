import os
import warnings
from typing import Optional
from tempfile import gettempdir

from pydantic import BaseSettings, validator
from pydantic.fields import ModelField


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = f"sqlite:///{gettempdir()}/own_comments.db"
    """
    A URL
    """
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASS: str = "pass"

    AUTO_APPROVE_NEW_THREADS: bool = True

    ALLOW_ORIGIN_REGEX: str = ".*"

    URL_PREFIX = ""

    SMTP_SERVER: Optional[str] = None
    SMTP_PORT: Optional[str] = None
    SMTP_LOGIN: Optional[str] = None
    SMTP_PASS: Optional[str] = None
    SMTP_FROM: Optional[str] = None
    SMTP_TO: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URL", "ADMIN_USERNAME", "ADMIN_PASS")
    def warn_default_value(cls, v: str, field: ModelField):
        if v == field.default:
            warnings.warn(
                f"Using default value '{v}' for '{field.name}'. Do not do that in production!"
            )
        return v

    class Config:
        env_file = os.getenv("OWN_COMMENTS_ENV", ".env")


settings = Settings()
