from pydantic import BaseModel


class Voice(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str = None
    file_size: int = None
