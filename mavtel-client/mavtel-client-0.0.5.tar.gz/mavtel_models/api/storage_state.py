from typing import Dict

from pydantic import BaseModel

from mavtel_models.typing import BackendConfigType


class StorageBackendState(BaseModel):
    is_started: bool
    is_ready: bool
    backend_type: str
    config: BackendConfigType


class StorageState(BaseModel):
    is_ready: bool
    is_started: bool
    backends: Dict[str, StorageBackendState]
