from pydantic import BaseModel


class PollOption(BaseModel):
    text: str
    voter_count: int
