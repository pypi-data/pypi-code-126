from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.location import Location


class Position(Location, MAVLinkMetricBaseModel):
    relative_altitude_m: float

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.Position'
