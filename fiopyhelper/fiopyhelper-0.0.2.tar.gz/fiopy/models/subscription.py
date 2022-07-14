import json

from fiopy.models.base import BaseModel
from fiopy.models.plan import PlanModel
from fiopy.models.promotion import PromotionModel

__all__ = ["SubscriptionModel"]


class SubscriptionModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._balance = kwargs.get("balance")

        self._inserted_at = kwargs.get("inserted_at")
        self._deleted_at = kwargs.get("deleted_at")
        self._updated_at = kwargs.get("updated_at")

        self._cancellation_option = kwargs.get("cancellation_option")
        self._cancellation_reason = kwargs.get("cancellation_reason")
        self._cancelled_at = kwargs.get("cancelled_at")
        self._subscription_end_at = kwargs.get("subscription_end_at")

        self._on_trial = kwargs.get("on_trial")
        self._stripe_customer_id = kwargs.get("stripe_customer_id")
        self._stripe_subscription_id = kwargs.get("stripe_subscription_id")
        self._next_bill_at = kwargs.get("next_bill_at")
        self._last_payment_at = kwargs.get("last_payment_at")

        plan = kwargs.get("plan", {})
        while isinstance(plan, str):
            plan = json.loads(plan)
        self._plan = PlanModel(**plan)

        promotion = kwargs.get("promotion", {})
        while isinstance(promotion, str):
            promotion = json.loads(promotion)
        self._promotion = PromotionModel(**promotion)

        super().cleanup_values()

    @property
    def balance(self):
        return self._balance

    @property
    def inserted_at(self):
        return self._inserted_at

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def cancellation_option(self):
        return self._cancellation_option

    @property
    def cancellation_reason(self):
        return self._cancellation_reason

    @property
    def cancelled_at(self):
        return self._cancelled_at

    @property
    def subscription_end_at(self):
        return self._subscription_end_at

    @property
    def on_trial(self):
        return self._on_trial

    @property
    def stripe_customer_id(self):
        return self._stripe_customer_id

    @property
    def stripe_subscription_id(self):
        return self._stripe_subscription_id

    @property
    def next_bill_at(self):
        return self._next_bill_at

    @property
    def last_payment_at(self):
        return self._last_payment_at

    @property
    def plan(self):
        return self._plan

    @property
    def promotion(self):
        return self._promotion

