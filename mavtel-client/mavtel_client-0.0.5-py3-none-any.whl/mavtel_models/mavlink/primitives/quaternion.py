from pydantic import BaseModel


class Quaternion(BaseModel):
    w: float
    x: float
    y: float
    z: float
    timestamp_us: int
