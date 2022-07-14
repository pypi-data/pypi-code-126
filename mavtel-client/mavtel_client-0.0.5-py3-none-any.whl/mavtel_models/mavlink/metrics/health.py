from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class Health(MAVLinkMetricBaseModel):
    is_gyrometer_calibration_ok: bool
    is_accelerometer_calibration_ok: bool
    is_magnetometer_calibration_ok: bool
    is_local_position_ok: bool
    is_global_position_ok: bool
    is_home_position_ok: bool
    is_armable: bool

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.Health'
