from typing import Optional
from urllib.parse import urljoin, urlparse

import httpx
import orjson

from mavtel_models import get_supported_metrics, MAVLinkMetricBaseModel

DEFAULT_TIMEOUT = 50


class MAVTelClientBase:
    def __init__(self, url: str):
        self._url: str = url
        self._api_url = urljoin(self._url, 'api/v1')
        self._supported_metrics = get_supported_metrics()

    @property
    def url(self) -> str:
        return self._url

    def get_metric_url(self, metric_class: MAVLinkMetricBaseModel.__class__) -> str:
        return f'{self._api_url}/metrics/{metric_class.get_metric_name()}'

    def get_metrics_ws_url(self) -> str:
        parsed_url = urlparse(self._url)
        ws_base_url = parsed_url._replace(scheme='ws').geturl()
        return urljoin(ws_base_url, 'api/v1/streams/metrics')

    async def get_metric_by_class(
            self,
            metric_class: MAVLinkMetricBaseModel.__class__
    ) -> Optional[MAVLinkMetricBaseModel]:
        url = self.get_metric_url(metric_class)
        async with httpx.AsyncClient() as client:
            response: httpx.Response = await client.get(url, timeout=DEFAULT_TIMEOUT)
            data = orjson.loads(response.text)
            if data is None:
                return None
            return metric_class(**data)
