from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.quaternion import Quaternion


class AttitudeQuaternion(Quaternion, MAVLinkMetricBaseModel):
    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.Quaternion'
