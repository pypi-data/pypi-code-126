from fiopy.models.base import BaseModel


__all__ = ["PromotionModel"]


class PromotionModel(BaseModel):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self._plan_id = kwargs.get("plan_id")

        self._header_text = kwargs.get("header_text")
        self._header_subtext = kwargs.get("header_subtext")

        self._inserted_at = kwargs.get("inserted_at")
        self._deleted_at = kwargs.get("deleted_at")
        self._expires_at = kwargs.get("expires_at")
        self._updated_at = kwargs.get("updated_at")

        self._is_trial = kwargs.get("is_trial")

        self._autoscaling = kwargs.get("autoscaling")
        self._can_override_limitations = kwargs.get("can_override_limitations")
        self._new_price = kwargs.get("new_price")
        self._no_credit_card = kwargs.get("no_credit_card")
        self._promo_code = kwargs.get("promo_code")
        self._submit_text = kwargs.get("submit_text")
        self._trial_length = kwargs.get("trial_length")

        super().cleanup_values()

    @property
    def plan_id(self):
        return self._plan_id

    @property
    def header_text(self):
        return self._header_text

    @property
    def header_subtext(self):
        return self._header_subtext

    @property
    def inserted_at(self):
        return self._inserted_at

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def expires_at(self):
        return self._expires_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def is_trial(self):
        return self._is_trial

    @property
    def autoscaling(self):
        return self._autoscaling

    @property
    def can_override_limitations(self):
        return self._can_override_limitations

    @property
    def new_price(self):
        return self._new_price

    @property
    def no_credit_card(self):
        return self._no_credit_card

    @property
    def promo_code(self):
        return self._promo_code

    @property
    def submit_text(self):
        return self._submit_text

    @property
    def trial_length(self):
        return self._trial_length

