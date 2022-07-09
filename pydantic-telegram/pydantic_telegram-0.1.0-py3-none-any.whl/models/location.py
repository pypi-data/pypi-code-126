from pydantic import BaseModel


class Location(BaseModel):
    longitude: float
    latitude: float
    horizontal_accuracy: float = None
    live_period: int = None
    heading: int = None
    proximity_alert_radius: int = None
