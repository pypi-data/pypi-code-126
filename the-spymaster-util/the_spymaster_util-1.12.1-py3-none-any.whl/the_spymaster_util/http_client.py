import json
import logging
from typing import Any, Callable, Dict, Optional, Union

import requests
from requests import Response
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from the_spymaster_util import wrap

log = logging.getLogger(__name__)

CONTEXT_HEADER_KEY = "x-spymaster-context"
CONTEXT_ID_HEADER_KEY = "x-spymaster-context-id"

JsonType = Union[str, int, float, bool, list, Dict[str, Any], None]

DEFAULT_RETRY_STRATEGY = Retry(
    raise_on_status=False,
    total=4,
    backoff_factor=0.3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "OPTIONS", "GET", "POST", "PUT", "DELETE"],
)


class BaseHttpClient:
    def __init__(self, base_url: str, retry_strategy: Optional[Retry] = DEFAULT_RETRY_STRATEGY):
        self.base_url = base_url
        self.session = requests.Session()
        self.set_retry_strategy(retry_strategy)

    def set_retry_strategy(self, retry_strategy: Optional[Retry]):
        retry_adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", retry_adapter)
        self.session.mount("https://", retry_adapter)

    def _http_call(self, endpoint: str, method: Callable, parse: bool = True, **kwargs) -> Union[dict, Response]:
        url = f"{self.base_url}/{endpoint}"
        headers = kwargs.pop("headers", None) or {}
        log_context = getattr(log, "context", None)
        if log_context:
            headers[CONTEXT_HEADER_KEY] = json.dumps(log_context)
        log_http_data = kwargs.pop("log_http_data", True)
        method_name = method.__name__.upper()
        _log_request(method=method_name, url=url, data=kwargs.get("data"), headers=headers, log_http_data=log_http_data)
        response = method(url, headers=headers, **kwargs)
        _log_response(method=method_name, url=url, response=response, log_http_data=log_http_data)
        response.raise_for_status()
        if parse:
            return response.json()
        return response

    def _get(self, endpoint: str, data: dict, **kwargs) -> dict:
        return self._http_call(endpoint=endpoint, method=self.session.get, params=data, **kwargs)  # type: ignore

    def _post(self, endpoint: str, data: dict, **kwargs) -> dict:
        return self._http_call(endpoint=endpoint, method=self.session.post, json=data, **kwargs)  # type: ignore


def _log_request(method: str, url: str, data: Optional[dict], headers: Optional[dict], log_http_data: bool = True):
    extra = {"url": url, "data": data, "headers": headers} if log_http_data else {}
    log.debug(f"HTTP {method} to {url}", extra=extra)


def _log_response(method: str, url: str, response: Response, log_http_data: bool = True):
    extra = {}
    if log_http_data:
        try:
            data = response.json()
        except Exception:  # noqa
            data = response.content
        extra["data"] = data
    log.debug(f"HTTP {method} {wrap(response.status_code)} from {url}", extra=extra)
