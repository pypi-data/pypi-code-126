from enum import Enum


class WebsocketEventType(Enum):
    METRIC_UPDATE = 'METRIC_UPDATE'
    HEARTBEAT = 'HEARTBEAT'
