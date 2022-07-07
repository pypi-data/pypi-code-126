from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel


class LogisticsStatus(str, Enum):
    pending = "pending"
    in_delivery = "in_delivery"
    delivered = "delivered"
    exception = "exception"

    center_delivered = "center_delivered"
    store_delivered = "store_delivered"


class LogisticTypes(str, Enum):
    HOME = "HOME"
    CVS = "CVS"
    UNKNOWN = "UNKNOWN"


class LogisticsResp(BaseModel):
    order_id: str = ""
    logistics_id: str
    logistics_type: LogisticTypes
    logistics_subtype: str = ""
    logistics_status: LogisticsStatus
    logistics_message: str
    logistics_detail: Dict[str, Any] = {}
