from pydantic import Field, BaseModel
from telegram_pydantic.models.user import User
from telegram_pydantic.models.payments.shipping_address import ShippingAddress


class ShippingQuery(BaseModel):
    id: str
    query_from: User = Field(alias="from")
    invoice_payload: str
    shipping_address: ShippingAddress
