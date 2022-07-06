# generated by datamodel-codegen:
#   filename:  bridge.json

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class Bridge(BaseModel):
    """
    Bridge
    """

    class Config:
        extra = Extra.allow

    last_updated: dict[str, float] = Field(..., description="Last updated")
