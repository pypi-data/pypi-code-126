from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class DistanceSensor(MAVLinkMetricBaseModel):
    minimum_distance_m: float
    maximum_distance_m: float
    current_distance_m: float

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.DistanceSensor'
