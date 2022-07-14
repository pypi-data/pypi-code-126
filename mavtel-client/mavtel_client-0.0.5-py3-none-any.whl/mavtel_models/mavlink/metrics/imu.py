from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel, FLAT_STRUCT_DELIMITER
from mavtel_models.mavlink.primitives.acceleration_frd import AccelerationFrd
from mavtel_models.mavlink.primitives.angular_velocity_frd import AngularVelocityFrd
from mavtel_models.mavlink.primitives.magnetic_field_frd import MagneticFieldFrd


class Imu(MAVLinkMetricBaseModel):
    acceleration_frd: AccelerationFrd
    angular_velocity_frd: AngularVelocityFrd
    magnetic_field_frd: MagneticFieldFrd
    temperature_degc: float
    timestamp_us: int

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(
            acceleration_frd=mavlink_object.acceleration_frd.__dict__,
            angular_velocity_frd=mavlink_object.angular_velocity_frd.__dict__,
            magnetic_field_frd=mavlink_object.magnetic_field_frd.__dict__,
            temperature_degc=mavlink_object.temperature_degc,
            timestamp_us=mavlink_object.timestamp_us,
        )

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.Imu'

    def as_flat_dict(self):
        return dict(
            **{
                FLAT_STRUCT_DELIMITER.join(['acceleration_frd', name]): value
                for name, value in self.acceleration_frd.dict().items()
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['angular_velocity_frd', name]): value
                for name, value in self.angular_velocity_frd.dict().items()
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['magnetic_field_frd', name]): value
                for name, value in self.magnetic_field_frd.dict().items()
            },
            temperature_degc=self.temperature_degc,
            timestamp_us=self.timestamp_us,
        )
