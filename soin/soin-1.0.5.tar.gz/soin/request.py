from typing import Dict
import time
from uuid import uuid4
import requests
import logging


class Request:
    def __init__(
        self,
        url,
        method,
        headers,
        preset_body=None,
        preset_params=None,
        timeout=10,
    ):
        self.id = uuid4().hex
        self.url = url
        self.method = method
        self.headers = headers
        self.timeout = timeout
        self.preset_body = preset_body or {}
        self.preset_params = preset_params or {}

    def __str__(self):
        return f"url: {self.url} - method: {self.method}"

    __repr__ = __str__

    def make(self, data: Dict = None, params: Dict = None) -> requests.Response:
        logging.debug(f"make request {self} with data: {data}, params: {params}")
        response: requests.Response = None
        data = data or {}
        params = params or {}

        data = {**self.preset_body, **data}
        params = {**self.preset_params, **params}

        try:
            response = requests.request(
                self.method,
                self.url,
                headers=self.headers,
                params=params,
                json=data,
                timeout=self.timeout,
            )
        except Exception as e:
            logging.warn(
                f"error while making request {self}, exception is {e}"
            )
            return None

        return response
