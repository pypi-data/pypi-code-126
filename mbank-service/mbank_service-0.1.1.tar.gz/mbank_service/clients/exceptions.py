class ClientAPIException(Exception):
    def __init__(self, code: int, reason: str) -> None:
        self.error_code = code
        self.reason = reason


class ClientNotFoundError(ClientAPIException):
    ...


class ClientBadRequestError(ClientAPIException):
    ...


class ClientServerError(ClientAPIException):
    ...
