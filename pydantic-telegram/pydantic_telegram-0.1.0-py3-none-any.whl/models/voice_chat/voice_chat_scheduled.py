from pydantic import BaseModel


class VoiceChatScheduled(BaseModel):
    start_date: int
