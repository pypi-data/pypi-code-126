from pydantic import BaseModel


class EulerAngles(BaseModel):
    pitch_deg: float
    roll_deg: float
    yaw_deg: float
    timestamp_us: int
