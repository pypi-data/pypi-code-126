from pydantic import BaseModel


class AngularVelocityBody(BaseModel):
    roll_rad_s: float
    pitch_rad_s: float
    yaw_rad_s: float
