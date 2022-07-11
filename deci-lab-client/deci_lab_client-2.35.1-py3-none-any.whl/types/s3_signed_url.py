from typing import Dict, Any
from deci_common.abstractions.base_model import Schema


class S3SignedUrl(Schema):
    url: str
    fields: Dict[Any, str]
