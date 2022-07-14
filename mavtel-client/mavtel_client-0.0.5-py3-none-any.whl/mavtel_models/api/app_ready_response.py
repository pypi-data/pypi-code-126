from pydantic import BaseModel


class AppReadyResponse(BaseModel):
    is_ready: bool
    is_storage_ready: bool
    is_collector_ready: bool
