from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.flight_mode import FlightMode as _FlightMode


class FlightMode(MAVLinkMetricBaseModel):
    flight_mode: _FlightMode

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(flight_mode=_FlightMode(mavlink_object.value))

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.FlightMode'

    def as_flat_dict(self):
        return dict(
            flight_mode=self.flight_mode.value
        )
