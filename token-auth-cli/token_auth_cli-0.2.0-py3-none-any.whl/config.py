import logging
from typing import Optional, Any

from pydantic import (BaseModel,  # pylint: disable=no-name-in-module
                      BaseSettings)

logger = logging.getLogger(__name__)

"""
user config -> directory config -> options
"""


class Settings(BaseSettings):
    """App config."""
    api: str = "http://localhost:8000"
    api_get_token: str = "/api/authtoken/"
    api_get: str = "/api/"
    debug: bool = False
    verbose: bool = False
    show_settings: bool = True
    confirm_settings: bool = True
    store: bool = False

    class Config:
        env_prefix = "TOKEN_AUTH_CLI_SETTINGS_"
        env_file = '.env'
        env_file_encoding = "utf-8"


class App(BaseModel):
    settings: Settings
    config: str
    session: Optional[Any] = None
