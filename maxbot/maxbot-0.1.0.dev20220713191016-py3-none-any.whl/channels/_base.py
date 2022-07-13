from dataclasses import dataclass


@dataclass(frozen=True)
class ChannelEvent:

    channel: str
    user_id: int
    message: object
