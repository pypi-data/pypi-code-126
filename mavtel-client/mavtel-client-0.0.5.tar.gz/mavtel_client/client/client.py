import json
import logging
from urllib.parse import urljoin

import httpx
import websockets
from websockets.exceptions import ConnectionClosed

from mavtel_client.client.base import MAVTelClientBase
from mavtel_client.client.mixins.metrics_mixin import MetricsMixin
from mavtel_client.client.mixins.services_mixin import ServicesMixin
from mavtel_models import MAVLinkMetricBaseModel, WebsocketEventType


class MAVTelClient(MAVTelClientBase, MetricsMixin, ServicesMixin):
    async def healthcheck(self) -> bool:
        url = urljoin(self._url, 'health/check')
        async with httpx.AsyncClient() as client:
            try:
                response: httpx.Response = await client.get(url)
                return response.status_code == 200 and response.text == 'OK'
            except httpx.ConnectError:
                return False

    async def metric_updates(self):
        async with websockets.connect(self.get_metrics_ws_url()) as websocket:
            while True:
                try:
                    raw_message = await websocket.recv()
                    message = json.loads(raw_message)

                    if message['event'] != WebsocketEventType.METRIC_UPDATE.value:
                        continue

                    metric_class: MAVLinkMetricBaseModel.__class__ = self._supported_metrics[message['metric_name']]

                    yield metric_class(**message['data'])
                except json.decoder.JSONDecodeError as json_error:
                    logging.error(f"Error decoding metrics message: {json_error}. Message: '{raw_message}'")
                except ConnectionClosed:
                    print('ConnectionClosed')
                    break
