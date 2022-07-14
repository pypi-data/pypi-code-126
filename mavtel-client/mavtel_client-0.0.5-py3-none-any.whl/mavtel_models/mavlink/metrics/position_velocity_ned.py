from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel, FLAT_STRUCT_DELIMITER
from mavtel_models.mavlink.primitives.position_ned import PositionNed
from mavtel_models.mavlink.primitives.velocity_ned import VelocityNed


class PositionVelocityNed(MAVLinkMetricBaseModel):
    position: PositionNed
    velocity: VelocityNed

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(
            position=mavlink_object.position.__dict__,
            velocity=mavlink_object.velocity.__dict__,
        )

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.PositionVelocityNed'

    def as_flat_dict(self):
        return dict(
            **{
                FLAT_STRUCT_DELIMITER.join(['position', name]): value
                for name, value in self.position.dict().items()
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['velocity', name]): value
                for name, value in self.velocity.dict().items()
            },
        )
