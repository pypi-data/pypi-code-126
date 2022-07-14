from pydantic import BaseModel


class AccelerationFrd(BaseModel):
    forward_m_s2: float
    right_m_s2: float
    down_m_s2: float
