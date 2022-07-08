from typing import TYPE_CHECKING, ClassVar

from pydantic import BaseModel

if TYPE_CHECKING:
    from tygle.base.rest import REST


class Resource(BaseModel):
    rest: ClassVar["REST"]

    class Config:
        use_enum_values = True
