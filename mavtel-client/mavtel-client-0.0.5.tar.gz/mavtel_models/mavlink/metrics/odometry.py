from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel, FLAT_STRUCT_DELIMITER
from mavtel_models.mavlink.primitives.angular_velocity_body import AngularVelocityBody
from mavtel_models.mavlink.primitives.covariance import Covariance
from mavtel_models.mavlink.primitives.mav_frame import MavFrame
from mavtel_models.mavlink.primitives.position_body import PositionBody
from mavtel_models.mavlink.primitives.quaternion import Quaternion
from mavtel_models.mavlink.primitives.velocity_body import VelocityBody


class Odometry(MAVLinkMetricBaseModel):
    time_usec: int
    frame_id: MavFrame
    child_frame_id: MavFrame
    position_body: PositionBody
    q: Quaternion
    velocity_body: VelocityBody
    angular_velocity_body: AngularVelocityBody
    pose_covariance: Covariance
    velocity_covariance: Covariance

    @classmethod
    def from_mavlink(cls, mavlink_object: object):
        # noinspection PyUnresolvedReferences
        return cls(
            time_usec=mavlink_object.time_usec,
            frame_id=MavFrame(mavlink_object.frame_id.value),
            child_frame_id=MavFrame(mavlink_object.child_frame_id.value),
            position_body=mavlink_object.position_body.__dict__,
            q=mavlink_object.q.__dict__,
            velocity_body=mavlink_object.velocity_body.__dict__,
            angular_velocity_body=mavlink_object.angular_velocity_body.__dict__,
            pose_covariance=Covariance(
                covariance_matrix=list(mavlink_object.pose_covariance.covariance_matrix)
            ),
            velocity_covariance=Covariance(
                covariance_matrix=list(mavlink_object.velocity_covariance.covariance_matrix)
            ),
        )

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.Odometry'

    def as_flat_dict(self):
        return dict(
            **{
                FLAT_STRUCT_DELIMITER.join(['position_body', name]): value
                for name, value in self.position_body.dict().items()
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['q', name]): value
                for name, value in self.q.dict().items()
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['velocity_body', name]): value
                for name, value in self.velocity_body.dict().items()
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['angular_velocity_body', name]): value
                for name, value in self.velocity_body.dict().items()
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['pose_covariance', str(i)]): self.pose_covariance.covariance_matrix[i]
                for i in range(len(self.pose_covariance.covariance_matrix))
            },
            **{
                FLAT_STRUCT_DELIMITER.join(['velocity_covariance', str(i)]): self.velocity_covariance.covariance_matrix[
                    i]
                for i in range(len(self.velocity_covariance.covariance_matrix))
            },
            time_usec=self.time_usec,
            frame_id=self.frame_id.value,
            child_frame_id=self.child_frame_id.value,
        )
