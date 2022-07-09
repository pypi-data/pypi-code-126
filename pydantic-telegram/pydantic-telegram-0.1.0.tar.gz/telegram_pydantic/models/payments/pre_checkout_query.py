from pydantic import Field, BaseModel
from telegram_pydantic.models.user import User
from telegram_pydantic.models.payments.order_info import OrderInfo


class PreCheckoutQuery(BaseModel):
    id: str
    query_from: User = Field(alias="from")
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str = None
    order_info: OrderInfo = None
