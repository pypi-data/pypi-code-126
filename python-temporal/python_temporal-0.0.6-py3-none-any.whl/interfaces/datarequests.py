from typing import Dict, Any, Optional
from pydantic import BaseModel


class BaseDataRequest(BaseModel):
    success: bool
    error: Optional[str] = None
    data: Optional[Dict] = None
    infotypes: Optional[Dict] = None


ReadTaskStaticConfigFromFile: BaseDataRequest


class ScanTaskData(BaseDataRequest):
    data: Optional[Any] = None
    success: bool


class RunTask(BaseDataRequest):
    scanTaskID: str
