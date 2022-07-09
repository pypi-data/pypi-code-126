from pydantic import BaseModel
from telegram_pydantic.models.payments.order_info import OrderInfo


class SuccessfulPayment(BaseModel):
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str = None
    order_info: OrderInfo = None
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
