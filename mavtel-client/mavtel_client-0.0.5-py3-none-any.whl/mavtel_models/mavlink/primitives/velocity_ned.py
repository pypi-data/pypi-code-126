from pydantic import BaseModel


class VelocityNed(BaseModel):
    north_m_s: float
    east_m_s: float
    down_m_s: float
