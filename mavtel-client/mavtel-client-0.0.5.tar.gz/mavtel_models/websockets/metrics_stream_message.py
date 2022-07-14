from typing import Optional

from pydantic import BaseModel

from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.websockets.event_type import WebsocketEventType


class MetricsSteamMessage(BaseModel):
    event: WebsocketEventType
    metric_name: Optional[str]
    data: Optional[MAVLinkMetricBaseModel]
