from typing import List

from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel, FLAT_STRUCT_DELIMITER


class ActuatorControlTarget(MAVLinkMetricBaseModel):
    group: int
    controls: List[float]

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(group=mavlink_object.group, controls=list(mavlink_object.controls))

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.ActuatorControlTarget'

    def as_flat_dict(self):
        return dict(
            active=self.group,
            **{
                FLAT_STRUCT_DELIMITER.join(['controls', str(i)]): self.controls[i]
                for i in range(len(self.controls))
            }
        )
