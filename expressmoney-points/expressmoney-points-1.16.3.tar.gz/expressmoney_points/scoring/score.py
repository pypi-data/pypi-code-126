__all__ = ('ProfileScorePoint', 'OrderScorePoint', 'ILScorePoint')

from expressmoney.api import *


SERVICE = 'scoring'
APP = 'score'


class ProfileScoreCreateContract(Contract):
    pass


class ProfileScoreReadContract(Contract):
    created = serializers.DateTimeField()
    score = serializers.DecimalField(max_digits=3, decimal_places=2)


class ProfileScoreResponseContract(ProfileScoreReadContract):
    pass


class OrderScoreCreateContract(Contract):
    order_id = serializers.IntegerField(min_value=1)


class ILScoreCreateContract(OrderScoreCreateContract):
    pass


class OrderScoreResponseContract(Contract):
    created = serializers.DateTimeField()
    score = serializers.DecimalField(max_digits=3, decimal_places=2)
    order_id = serializers.IntegerField(min_value=1)


class ILScoreResponseContract(OrderScoreResponseContract):
    pass


class OrderScoreReadContract(OrderScoreResponseContract):
    pass


class ILScoreReadContract(OrderScoreResponseContract):
    pass


class ProfileScoreID(ID):
    _service = SERVICE
    _app = APP
    _view_set = 'profile_score'


class OrderScoreID(ID):
    _service = SERVICE
    _app = APP
    _view_set = 'order_score'


class ILScoreID(ID):
    _service = SERVICE
    _app = APP
    _view_set = 'il_score'


class ProfileScorePoint(ListPointMixin, ResponseMixin, CreatePointMixin, ContractPoint):
    _point_id = ProfileScoreID()
    _create_contract = ProfileScoreCreateContract
    _response_contract = ProfileScoreResponseContract
    _read_contract = ProfileScoreReadContract
    _sort_by = 'created'


class OrderScorePoint(ListPointMixin, ResponseMixin, CreatePointMixin, ContractPoint):
    _point_id = OrderScoreID()
    _read_contract = OrderScoreReadContract
    _create_contract = OrderScoreCreateContract
    _response_contract = OrderScoreResponseContract
    _sort_by = 'created'


class ILScorePoint(ListPointMixin, ResponseMixin, CreatePointMixin, ContractPoint):
    _point_id = ILScoreID()
    _read_contract = ILScoreReadContract
    _create_contract = ILScoreCreateContract
    _response_contract = ILScoreResponseContract
    _sort_by = 'created'
