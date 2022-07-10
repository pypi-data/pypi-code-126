from datetime import datetime, time
from dotenv import load_dotenv
import requests
import json
import os

from .exceptions import (
    ConnectionException,
    DataException,
    RequestException,
    ResponseException,
)

load_dotenv()
DEBUG = os.environ.get("DEBUG")


class APITools:
    METHODS = {
        "post": requests.post,
        "get": requests.get,
        "update": requests.patch,
        "delete": requests.delete,
    }
    DEFAULT_URL = "https://janet-habitat-api.herokuapp.com/api"
    if DEBUG:
        DEFAULT_URL = "http://habitat-api:5000/api"

    def __init__(self, api_url=None):
        self.api_url = api_url
        if self.api_url is None:
            self.api_url = os.environ.get("HABITAT_API_URL", self.DEFAULT_URL)
        self.validate_url(self.api_url)

    @staticmethod
    def validate_url(url):
        try:
            resp = requests.get(f"{url}/reading")
        except Exception:
            raise ConnectionException(
                "Incorrect API URL or API unreachable!", key="APIError"
            ).json()

    def request(self, url, method="get", data=None):
        try:
            resp = self.handle_request(url, method=method, data=data)
        except Exception as e:
            resp = e.json()
        return resp

    def handle_request(self, url, method="get", data=None):
        if data is not None and not isinstance(data, dict):
            raise DataException(
                "Data missing or Dict format invalid!", key="DataError"
            ).json()

        req_method = self.METHODS.get(method)
        if req_method is None:
            raise RequestException(
                "Invalid API request method type", key="DataError"
            ).json()

        try:
            resp = req_method(
                f"{self.api_url}/{url}/",
                json=data,
            )
        except Exception:
            raise ConnectionException("Incorrect API URL or API unreachable!").json()

        if not (200 <= resp.status_code < 300):
            message = resp.json().get("message")
            if message is None:
                message = resp.json().get("status")
            raise ResponseException(message, key="APIError").json()

        try:
            return resp.json()
        except Exception:
            raise DataException(
                "API JSON response format invalid!", key="APIError"
            ).json()

    def add_reading(self, temperature=None, humidity=None):
        return self.request(
            "reading",
            method="post",
            data={"temperature": temperature, "humidity": humidity},
        )

    def get_reading(self):
        return self.request("reading")

    def filter_readings(self, period=None, unit=None, date_from=None, date_to=None):
        data = {}
        if period is not None:
            data.update({"period": period, "unit": unit})
        elif date_from is not None:
            data.update({"date_from": date_from, "date_to": date_to})
        return self.request("readings", data=data)

    def get_config(self):
        return self.request("config")

    def set_config(self, data=None):
        return self.request("config", method="post", data=data)

    def new_config(self):
        return self.request("config/default/")
