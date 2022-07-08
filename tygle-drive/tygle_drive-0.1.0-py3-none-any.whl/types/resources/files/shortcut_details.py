from typing import ClassVar, Dict, Optional

from pydantic import Field
from tygle.apis.drive.types.enums.files import AnyMimeType
from tygle.base import Resource


class ShortcutDetails(Resource):
    WRITABLE: ClassVar[Dict[str, str]] = {
        "target_id": "targetId",
    }

    target_id: Optional[str] = Field(None, alias="targetId")
    taget_mime_type: Optional[AnyMimeType] = Field(None, alias="targetMimeType")
