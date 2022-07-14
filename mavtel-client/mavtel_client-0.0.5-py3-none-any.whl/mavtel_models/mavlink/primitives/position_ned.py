from pydantic import BaseModel


class PositionNed(BaseModel):
    north_m: float
    east_m: float
    down_m: float
