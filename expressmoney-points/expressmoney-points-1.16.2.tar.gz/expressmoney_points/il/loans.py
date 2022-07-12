__all__ = ('LoanPoint', 'LoanObjectPoint', )

from djmoney.contrib.django_rest_framework import MoneyField
from expressmoney.api import *

SERVICE = 'loans'


class LoanCreateContract(Contract):
    id = serializers.IntegerField(min_value=1)
    created = serializers.DateTimeField()
    order = serializers.IntegerField(min_value=1)
    bank_card_id = serializers.IntegerField(min_value=1)
    sign = serializers.IntegerField()
    ip = serializers.IPAddressField()


class LoanReadContract(Contract):
    ISSUING = 'ISSUING'
    OPEN = 'OPEN'  # Customer received money
    OVERDUE = 'OVERDUE'
    STOP_INTERESTS = 'STOP_INTERESTS'
    CLOSED = 'CLOSED'
    CANCELED = 'CANCELED'
    STATUS_CHOICES = {
        (ISSUING, ISSUING),
        (OPEN, OPEN),
        (OVERDUE, OVERDUE),
        (STOP_INTERESTS, STOP_INTERESTS),
        (CLOSED, CLOSED),
        (CANCELED, CANCELED),
    }
    id = serializers.IntegerField(min_value=1)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    order = serializers.IntegerField(min_value=1)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    bank_card_id = serializers.IntegerField(min_value=1)
    sign = serializers.IntegerField()
    interests_limit = serializers.DecimalField(max_digits=3, decimal_places=2)
    ip = serializers.IPAddressField()
    body_issue = MoneyField(max_digits=7, decimal_places=0)
    body_paid = MoneyField(max_digits=7, decimal_places=0)
    body_balance = MoneyField(max_digits=7, decimal_places=0)
    body_debt = MoneyField(max_digits=7, decimal_places=0)
    interests_charges = MoneyField(max_digits=7, decimal_places=0)
    interests_paid = MoneyField(max_digits=7, decimal_places=0)
    interests_balance = MoneyField(max_digits=7, decimal_places=0)


class LoanID(ID):
    _service = SERVICE
    _app = 'loans'
    _view_set = 'loan'


class LoanPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = LoanID()
    _read_contract = LoanReadContract
    _create_contract = LoanCreateContract


class LoanObjectPoint(RetrievePointMixin, ContractObjectPoint):
    _point_id = LoanID()
    _read_contract = LoanReadContract
