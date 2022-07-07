import abc
from urllib.parse import urljoin, urlencode

import requests

from clients.exceptions import (
    ClientNotFoundError,
    ClientBadRequestError,
    ClientServerError,
    ClientAPIException
)


class BaseClient(abc.ABC):
    def __init__(self, token: str, url: str):
        self._token = token
        self._main_url = url

    @staticmethod
    def _strip_phone(phone):
        return str(phone).strip('+')

    def _build_absolute_url(self, url, data):
        return f'{urljoin(self._main_url, url)}?{urlencode(data)}'

    @staticmethod
    def _checker_response(response: requests.Response):
        status_code = response.status_code
        if (
                status_code == 200 or
                status_code == 201 or
                status_code == 202
        ):
            return

        if status_code == 404:
            raise ClientNotFoundError(response.status_code, response.text)

        if 400 <= status_code < 500:
            raise ClientBadRequestError(response.status_code, response.text)

        if status_code >= 500:
            raise ClientServerError(response.status_code, response.text)
        raise ClientAPIException(response.status_code, response.text)
