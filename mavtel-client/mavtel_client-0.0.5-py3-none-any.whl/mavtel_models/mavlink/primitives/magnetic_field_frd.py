from pydantic import BaseModel


class MagneticFieldFrd(BaseModel):
    forward_gauss: float
    right_gauss: float
    down_gauss: float
