from pydantic import BaseModel


class AngularVelocityFrd(BaseModel):
    forward_rad_s: float
    right_rad_s: float
    down_rad_s: float
