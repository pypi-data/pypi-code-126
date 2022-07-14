from typing import List

from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel, FLAT_STRUCT_DELIMITER


class ActuatorOutputStatus(MAVLinkMetricBaseModel):
    active: int
    actuator: List[float]

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(active=mavlink_object.active, actuator=list(mavlink_object.actuator))

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.ActuatorOutputStatus'

    def as_flat_dict(self):
        return dict(
            active=self.active,
            **{
                FLAT_STRUCT_DELIMITER.join(['actuator', str(i)]): self.actuator[i]
                for i in range(len(self.actuator))
            }
        )
