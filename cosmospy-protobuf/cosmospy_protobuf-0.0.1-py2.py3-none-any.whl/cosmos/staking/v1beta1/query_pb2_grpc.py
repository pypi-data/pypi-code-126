
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.staking.v1beta1 import query_pb2 as cosmos_dot_staking_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Validators = channel.unary_unary('/cosmos.staking.v1beta1.Query/Validators', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.FromString)
        self.Validator = channel.unary_unary('/cosmos.staking.v1beta1.Query/Validator', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.FromString)
        self.ValidatorDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/ValidatorDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.FromString)
        self.ValidatorUnbondingDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.FromString)
        self.Delegation = channel.unary_unary('/cosmos.staking.v1beta1.Query/Delegation', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.FromString)
        self.UnbondingDelegation = channel.unary_unary('/cosmos.staking.v1beta1.Query/UnbondingDelegation', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.FromString)
        self.DelegatorDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.FromString)
        self.DelegatorUnbondingDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.FromString)
        self.Redelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/Redelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.FromString)
        self.DelegatorValidators = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorValidators', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.FromString)
        self.DelegatorValidator = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorValidator', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.FromString)
        self.HistoricalInfo = channel.unary_unary('/cosmos.staking.v1beta1.Query/HistoricalInfo', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.FromString)
        self.Pool = channel.unary_unary('/cosmos.staking.v1beta1.Query/Pool', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.FromString)
        self.Params = channel.unary_unary('/cosmos.staking.v1beta1.Query/Params', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def Validators(self, request, context):
        'Validators queries all validators that match the given status.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Validator(self, request, context):
        'Validator queries validator info for given validator address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorDelegations(self, request, context):
        'ValidatorDelegations queries delegate info for given validator.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorUnbondingDelegations(self, request, context):
        'ValidatorUnbondingDelegations queries unbonding delegations of a validator.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delegation(self, request, context):
        'Delegation queries delegate info for given validator delegator pair.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnbondingDelegation(self, request, context):
        'UnbondingDelegation queries unbonding info for given validator delegator\n        pair.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorDelegations(self, request, context):
        'DelegatorDelegations queries all delegations of a given delegator address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorUnbondingDelegations(self, request, context):
        'DelegatorUnbondingDelegations queries all unbonding delegations of a given\n        delegator address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Redelegations(self, request, context):
        'Redelegations queries redelegations of given address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorValidators(self, request, context):
        'DelegatorValidators queries all validators info for given delegator\n        address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorValidator(self, request, context):
        'DelegatorValidator queries validator info for given delegator validator\n        pair.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HistoricalInfo(self, request, context):
        'HistoricalInfo queries the historical info for given height.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pool(self, request, context):
        'Pool queries the pool info.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        'Parameters queries the staking parameters.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Validators': grpc.unary_unary_rpc_method_handler(servicer.Validators, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.SerializeToString), 'Validator': grpc.unary_unary_rpc_method_handler(servicer.Validator, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.SerializeToString), 'ValidatorDelegations': grpc.unary_unary_rpc_method_handler(servicer.ValidatorDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.SerializeToString), 'ValidatorUnbondingDelegations': grpc.unary_unary_rpc_method_handler(servicer.ValidatorUnbondingDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.SerializeToString), 'Delegation': grpc.unary_unary_rpc_method_handler(servicer.Delegation, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.SerializeToString), 'UnbondingDelegation': grpc.unary_unary_rpc_method_handler(servicer.UnbondingDelegation, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.SerializeToString), 'DelegatorDelegations': grpc.unary_unary_rpc_method_handler(servicer.DelegatorDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.SerializeToString), 'DelegatorUnbondingDelegations': grpc.unary_unary_rpc_method_handler(servicer.DelegatorUnbondingDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.SerializeToString), 'Redelegations': grpc.unary_unary_rpc_method_handler(servicer.Redelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.SerializeToString), 'DelegatorValidators': grpc.unary_unary_rpc_method_handler(servicer.DelegatorValidators, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.SerializeToString), 'DelegatorValidator': grpc.unary_unary_rpc_method_handler(servicer.DelegatorValidator, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.SerializeToString), 'HistoricalInfo': grpc.unary_unary_rpc_method_handler(servicer.HistoricalInfo, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.SerializeToString), 'Pool': grpc.unary_unary_rpc_method_handler(servicer.Pool, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.staking.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def Validators(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Validators', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Validator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Validator', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/ValidatorDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorUnbondingDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delegation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Delegation', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnbondingDelegation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/UnbondingDelegation', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorUnbondingDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Redelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Redelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorValidators(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorValidators', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorValidator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorValidator', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HistoricalInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/HistoricalInfo', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Pool', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Params', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
