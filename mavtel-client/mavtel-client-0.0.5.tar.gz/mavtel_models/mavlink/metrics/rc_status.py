from typing import Any, Optional

from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class RcStatus(MAVLinkMetricBaseModel):
    was_available_once: bool
    is_available: bool
    signal_strength_percent: Optional[float]

    def __init__(self, **data: Any):
        super().__init__(**data)

        if self.signal_strength_percent is None:
            self.signal_strength_percent = float('nan')

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.RcStatus'
