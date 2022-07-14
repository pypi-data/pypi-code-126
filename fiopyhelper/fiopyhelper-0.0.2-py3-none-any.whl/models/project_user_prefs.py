from fiopy.config import Config
from fiopy.enums import UserRole
from fiopy.models.base import BaseModel
from fiopy.http.http_request import HttpRequest
from fiopy.annotations.autowire import autowire

__all__ = ["ProjectUserPrefsModel"]


class ProjectUserPrefsModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        super().cleanup_values()

