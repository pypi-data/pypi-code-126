from typing import ClassVar, Dict, Optional

from pydantic import BaseModel, Field
from tygle.apis.drive.types.enums.files import ExportMimeType


class Thumbnail(BaseModel):
    WRITABLE: ClassVar[Dict[str, str]] = {
        "image": "image",
        "mime_type": "mimeType",
    }

    image: Optional[bytes] = Field(None)
    mime_type: Optional[ExportMimeType] = Field(None, alias="mimeType")


class ContentHints(BaseModel):
    WRITABLE: ClassVar[Dict[str, str]] = {
        "indexable_text": "indexableText",
    }

    thumbnail: Optional[Thumbnail] = Field(None)
    indexable_text: Optional[str] = Field(None, alias="indexableText")
