from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.euler_angles import EulerAngles


class AttitudeEuler(EulerAngles, MAVLinkMetricBaseModel):
    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.EulerAngle'
