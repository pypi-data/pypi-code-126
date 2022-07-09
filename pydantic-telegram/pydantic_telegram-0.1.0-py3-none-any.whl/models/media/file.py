from pydantic import BaseModel


class File(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int = None
    file_path: str = None
