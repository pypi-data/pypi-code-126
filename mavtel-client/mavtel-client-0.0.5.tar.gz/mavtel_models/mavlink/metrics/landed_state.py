from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.landed_state import LandedState as _LandedState


class LandedState(MAVLinkMetricBaseModel):
    landed_state: _LandedState

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(landed_state=_LandedState(mavlink_object.value))

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.LandedState'

    def as_flat_dict(self):
        return dict(
            landed_state=self.landed_state.value
        )
