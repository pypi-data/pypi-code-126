from http import HTTPStatus
from typing import NamedTuple, final

from .exceptions import _append_exclamation_mark


class _ExtendedResponse(NamedTuple):
    message: str
    status_code: int
    error_key: str


class ExtendedError(Exception):
    def __init__(
        self,
        message: str,
        error_key: str,
        status_code: HTTPStatus = HTTPStatus.BAD_REQUEST,
    ) -> None:
        self._message = message
        self._error_key = error_key
        self._status_code = status_code

    @final
    @property
    def message(self):
        return _append_exclamation_mark(self._message)

    @final
    def response(self) -> _ExtendedResponse:
        return _ExtendedResponse(
            self.message,
            self._status_code,
            self._error_key,
        )
