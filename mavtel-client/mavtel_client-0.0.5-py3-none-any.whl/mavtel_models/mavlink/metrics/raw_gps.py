from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class RawGps(MAVLinkMetricBaseModel):
    timestamp_us: int
    latitude_deg: float
    longitude_deg: float
    absolute_altitude_m: float
    hdop: float
    vdop: float
    velocity_m_s: float
    cog_deg: float
    altitude_ellipsoid_m: float
    horizontal_uncertainty_m: float
    vertical_uncertainty_m: float
    velocity_uncertainty_m_s: float
    heading_uncertainty_deg: float
    yaw_deg: float

    def get_mavlink_data_class_name(self) -> object:
        return 'mavsdk.telemetry.RawGps'
