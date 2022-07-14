from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class VelocityNed(MAVLinkMetricBaseModel):
    north_m_s: float
    east_m_s: float
    down_m_s: float

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.VelocityNed'
