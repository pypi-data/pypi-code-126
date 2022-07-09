from pydantic import BaseModel
from telegram_pydantic.models.location import Location


class Venue(BaseModel):
    location: Location
    title: str
    address: str
    foursquare_id: str = None
    foursquare_type: str = None
    google_place_id: str = None
    google_place_type: str = None
