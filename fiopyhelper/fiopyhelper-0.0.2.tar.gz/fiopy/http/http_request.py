import json
import os
import requests
from fiopy.http.enums.http_request_method import HttpRequestMethod
from fiopy.http.http_response import HttpResponse
from fiopy.exceptions.rate_limited import RateLimitedException


class HttpRequest:
    @staticmethod
    def request(hostname):
        return HttpRequest(hostname)

    def __init__(self, hostname):
        self._hostname = hostname
        self._endpoint = None
        self._method = None
        self._headers = {}
        self._qs_params = {}
        self._body_params = {}
        self._body = None
        self._file_path = None
        self._body_type = None

    def get(self, endpoint):
        self._endpoint = endpoint
        self._method = HttpRequestMethod.GET
        return self

    def post(self, endpoint):
        self._endpoint = endpoint
        self._method = HttpRequestMethod.POST
        return self

    def put(self, endpoint):
        self._endpoint = endpoint
        self._method = HttpRequestMethod.PUT
        return self

    def delete(self, endpoint):
        self._endpoint = endpoint
        self._method = HttpRequestMethod.DELETE
        return self

    def set_header(self, name, value):
        self._headers[name] = value
        return self

    def add_path_param(self, name, value):
        self._endpoint = self._endpoint.replace(f"${{{name}}}", value, 1)
        return self

    def add_qry_param(self, name, value):
        self._qs_params[name] = value
        return self

    def add_body_param(self, name, value):
        self._body_params[name] = value
        return self

    def body(self, payload):
        try:
            self._body = json.dumps(payload.__dict__)
            self.set_header("content-type", "application/json;charset=UTF-8")
        except:
            try:
                self._body = json.dumps(payload)
                self.set_header("content-type", "application/json;charset=UTF-8")
            except:
                self._body = payload

        return self

    def attach(self, payload):
        self._body = payload
        return self

    def upload(self, file_path):
        self._file_path = file_path
        return self

    def send(self):
        res = requests.request(
            self._method.value,
            f"{self._hostname}{self._endpoint}",
            params=self._qs_params,
            data=self._body or self._body_params,
            json=self._body,
            headers=self._headers,
            proxies={"http": os.getenv("FIO_HTTP_PROXY"), "https": os.getenv("FIO_HTTPS_PROXY")},
            verify=False if os.getenv("FIO_DISABLE_CERT_VALIDATION") else True,
        )
        print("Sending Request")
        response = HttpResponse(res)
        HttpRequest._last_response = response

        if res.status_code == 429:
            raise RateLimitedException(rate_limit=response.rate_limit)

        return HttpRequest._last_response

    @staticmethod
    def get_last_response():
        return HttpRequest._last_response
