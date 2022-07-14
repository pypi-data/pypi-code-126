from pydantic import BaseModel


class Location(BaseModel):
    latitude_deg: float
    longitude_deg: float
    absolute_altitude_m: float
