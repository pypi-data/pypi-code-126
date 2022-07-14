from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class Battery(MAVLinkMetricBaseModel):
    id: int
    voltage_v: float
    remaining_percent: float

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.Battery'
