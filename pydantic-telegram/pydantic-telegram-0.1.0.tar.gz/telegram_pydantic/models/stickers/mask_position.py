from pydantic import BaseModel


class MaskPosition(BaseModel):
    x_point: str
    x_shift: float
    y_shift: float
    scale: float
