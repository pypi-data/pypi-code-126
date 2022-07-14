from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.primitives.fix_type import FixType


class GpsInfo(MAVLinkMetricBaseModel):
    num_satellites: int
    fix_type: FixType

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(
            num_satellites=mavlink_object.num_satellites,
            fix_type=FixType(mavlink_object.fix_type.value)
        )

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.GpsInfo'

    def as_flat_dict(self):
        return dict(
            num_satellites=self.num_satellites,
            fix_type=self.fix_type.value,
        )
