from pydantic import BaseModel


class SessionState(BaseModel):
    session_id: str
    name: str
    start_utc_timestamp: float
