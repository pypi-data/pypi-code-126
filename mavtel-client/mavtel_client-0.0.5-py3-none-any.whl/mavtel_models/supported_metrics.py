from typing import Dict

from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel
from mavtel_models.mavlink.metrics import *


def get_supported_metrics() -> Dict[str, MAVLinkMetricBaseModel.__class__]:
    return dict(
        actuator_control_target=ActuatorControlTarget,
        actuator_output_status=ActuatorOutputStatus,
        attitude_angular_velocity_body=AttitudeAngularVelocityBody,
        attitude_euler=AttitudeEuler,
        attitude_quaternion=AttitudeQuaternion,
        armed=Armed,
        battery=Battery,
        camera_attitude_euler=CameraAttitudeEuler,
        camera_attitude_quaternion=CameraAttitudeQuaternion,
        distance_sensor=DistanceSensor,
        fixedwing_metrics=FixedwingMetrics,
        flight_mode=FlightMode,
        gps_info=GpsInfo,
        ground_truth=GroundTruth,
        heading=Heading,
        health=Health,
        health_all_ok=HealthAllOk,
        home=Home,
        imu=Imu,
        in_air=InAir,
        landed_state=LandedState,
        odometry=Odometry,
        position=Position,
        position_velocity_ned=PositionVelocityNed,
        raw_gps=RawGps,
        raw_imu=RawImu,
        rc_status=RcStatus,
        unix_epoch_time=UnixEpochTime,
        velocity_ned=VelocityNed,
        vtol_state=VtolState,
    )
