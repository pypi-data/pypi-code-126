from typing import List

from pydantic import BaseModel


class CollectorState(BaseModel):
    is_ready: bool
    is_started: bool
    metrics: List[str]
    events_processed: int
