from enum import Enum

__all__ = ["HttpRequestMethod"]


class HttpRequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
