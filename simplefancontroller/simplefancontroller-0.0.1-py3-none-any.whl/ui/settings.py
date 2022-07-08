from os import urandom, path
from dataclasses import dataclass

from decouple import config

DEFAULT_CONF_DIR = "config"


@dataclass
class UIConfig:
    CSRF_SESSION_KEY: bytes = urandom(32)
