from fiopy.enums import BaseEnum

__all__ = ["SessionMethod"]


class SessionMethod(BaseEnum):
    JWT = "jwt"
    PAT = "pat"
