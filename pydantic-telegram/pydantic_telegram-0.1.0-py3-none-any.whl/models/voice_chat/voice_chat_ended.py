from pydantic import BaseModel


class VoiceChatEnded(BaseModel):
    duration: int
