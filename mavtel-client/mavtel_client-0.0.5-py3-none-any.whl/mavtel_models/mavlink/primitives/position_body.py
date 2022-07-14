from pydantic import BaseModel


class PositionBody(BaseModel):
    x_m: float
    y_m: float
    z_m: float
