from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.angular_velocity_body import AngularVelocityBody


class AttitudeAngularVelocityBody(AngularVelocityBody, MAVLinkMetricBaseModel):
    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.AngularVelocityBody'
