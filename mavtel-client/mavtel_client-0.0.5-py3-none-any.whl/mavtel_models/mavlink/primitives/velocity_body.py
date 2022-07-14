from pydantic import BaseModel


class VelocityBody(BaseModel):
    x_m_s: float
    y_m_s: float
    z_m_s: float
