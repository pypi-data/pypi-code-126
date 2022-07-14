from pydantic import BaseModel


class APIInfo(BaseModel):
    version: str
    build: str
