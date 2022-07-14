from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class FixedwingMetrics(MAVLinkMetricBaseModel):
    airspeed_m_s: float
    throttle_percentage: float
    climb_rate_m_s: float

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.FixedwingMetrics'
