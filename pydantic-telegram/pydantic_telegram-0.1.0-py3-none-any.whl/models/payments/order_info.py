from pydantic import BaseModel
from telegram_pydantic.models.payments.shipping_address import ShippingAddress


class OrderInfo(BaseModel):
    name: str = None
    phone_number: str = None
    email: str = None
    shipping_address: ShippingAddress = None
