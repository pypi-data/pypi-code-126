from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.vtol_state import VtolState as _VtolState


class VtolState(MAVLinkMetricBaseModel):
    vtol_state: _VtolState

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(vtol_state=_VtolState(mavlink_object.value))

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.VtolState'

    def as_flat_dict(self):
        return dict(
            vtol_state=self.vtol_state.value
        )
