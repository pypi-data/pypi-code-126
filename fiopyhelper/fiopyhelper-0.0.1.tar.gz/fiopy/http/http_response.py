from fiopy.http.rate_limit import RateLimit
from fiopy.models.base import BaseModel
import jmespath
import os


class HttpResponse:
    def __init__(self, res):
        self._status = res.status_code
        self._headers = res.headers
        try:
            self._body = res.json()
        except (ValueError, UnicodeDecodeError):
            self._body = res.text
        self._rate_limit = RateLimit(
            value=res.headers.get("x-ratelimit-limit"),
            remaining=res.headers.get("x-ratelimit-remaining"),
            window=res.headers.get("x-ratelimit-window"),
        )

        if os.getenv("FIO_DEBUG"):
            print(
                "{url}\n\n{status_code}\n{headers}\n\n{body}".format(
                    url=res.url,
                    status_code=res.status_code,
                    headers="\n".join("{}: {}".format(k, v) for k, v in res.headers.items()),
                    body=res.content,
                )
            )

    def status(self):
        self._assertion_value = self._status
        return self

    def body(self):
        self._assertion_value = self._body
        return self

    def header(self, name):
        self._assertion_value = self._headers[name]
        return self

    def to_model(self, *, model_clazz: BaseModel = None, key: str = None, jpath: str = None) -> BaseModel:
        data = self.body().value(key=key, jpath=jpath).get() if key or jpath else self.body().get()
        model = model_clazz(**(data or {}))
        return model

    def to_models(self, *, model_clazz: BaseModel = None, key: str = None, jpath: str = None) -> BaseModel:
        data = self.body().value(key=key, jpath=jpath).get() if key or jpath else self.body().get()

        models = []
        if isinstance(data, list) and data:
            models = list(filter(bool, [model_clazz(**(obj or {})) for obj in data]))
        return models

    @property
    def rate_limit(self):
        return self._rate_limit

    def get(self):
        assertion_result = self._assertion_value
        self._assertion_value = None
        return assertion_result

    def value(self, *, key=None, jpath=None):
        if jpath:
            self._assertion_value = jmespath.search(jpath, self._assertion_value)
        elif key:
            self._assertion_value = self._assertion_value.get(key)
        return self

    def is_equal_to(self, value):
        assertion_result = self._assertion_value == value
        self._assertion_value = None
        return assertion_result

    def is_not_equal_to(self, value):
        assertion_result = self._assertion_value != value
        self._assertion_value = None
        return assertion_result

    def is_of_type(self, type):
        assertion_result = isinstance(self._assertion_value, type)
        self._assertion_value = None
        return assertion_result

    def is_true(self):
        assertion_result = self._assertion_value is True
        self._assertion_value = None
        return assertion_result

    def is_false(self):
        assertion_result = self._assertion_value is False
        self._assertion_value = None
        return assertion_result

    def exists(self):
        assertion_result = self._assertion_value != None
        self._assertion_value = None
        return assertion_result

    def doesnt_exist(self):
        assertion_result = self._assertion_value is None
        self._assertion_value = None
        return assertion_result

    def is_empty(self):
        assertion_result = not bool(self._assertion_value)
        self._assertion_value = None
        return assertion_result

    def is_not_empty(self):
        assertion_result = bool(self._assertion_value)
        self._assertion_value = None
        return assertion_result

    def has_length(self, length):
        assertion_result = len(self._assertion_value) is length
        self._assertion_value = None
        return assertion_result

    def has_length_less_than(self, length):
        assertion_result = len(self._assertion_value) < length
        self._assertion_value = None
        return assertion_result

    def has_length_less_than_or_equal_to(self, length):
        assertion_result = len(self._assertion_value) <= length
        self._assertion_value = None
        return assertion_result

    def has_length_greater_than(self, length):
        assertion_result = len(self._assertion_value) > length
        self._assertion_value = None
        return assertion_result

    def has_length_greater_than_or_equal_to(self, length):
        assertion_result = len(self._assertion_value) >= length
        self._assertion_value = None
        return assertion_result
