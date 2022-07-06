
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.upgrade.v1beta1 import query_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC upgrade querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.CurrentPlan = channel.unary_unary('/cosmos.upgrade.v1beta1.Query/CurrentPlan', request_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryCurrentPlanRequest.SerializeToString, response_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryCurrentPlanResponse.FromString)
        self.AppliedPlan = channel.unary_unary('/cosmos.upgrade.v1beta1.Query/AppliedPlan', request_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAppliedPlanRequest.SerializeToString, response_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAppliedPlanResponse.FromString)
        self.UpgradedConsensusState = channel.unary_unary('/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState', request_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryUpgradedConsensusStateRequest.SerializeToString, response_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryUpgradedConsensusStateResponse.FromString)
        self.ModuleVersions = channel.unary_unary('/cosmos.upgrade.v1beta1.Query/ModuleVersions', request_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryModuleVersionsRequest.SerializeToString, response_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryModuleVersionsResponse.FromString)
        self.Authority = channel.unary_unary('/cosmos.upgrade.v1beta1.Query/Authority', request_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAuthorityRequest.SerializeToString, response_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAuthorityResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC upgrade querier service.\n    '

    def CurrentPlan(self, request, context):
        'CurrentPlan queries the current upgrade plan.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppliedPlan(self, request, context):
        'AppliedPlan queries a previously applied upgrade plan by its name.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradedConsensusState(self, request, context):
        'UpgradedConsensusState queries the consensus state that will serve\n        as a trusted kernel for the next version of this chain. It will only be\n        stored at the last height of this chain.\n        UpgradedConsensusState RPC not supported with legacy querier\n        This rpc is deprecated now that IBC has its own replacement\n        (https://github.com/cosmos/ibc-go/blob/2c880a22e9f9cc75f62b527ca94aa75ce1106001/proto/ibc/core/client/v1/query.proto#L54)\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModuleVersions(self, request, context):
        'ModuleVersions queries the list of module versions from state.\n\n        Since: cosmos-sdk 0.43\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authority(self, request, context):
        'Returns the account with authority to conduct upgrades\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'CurrentPlan': grpc.unary_unary_rpc_method_handler(servicer.CurrentPlan, request_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryCurrentPlanRequest.FromString, response_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryCurrentPlanResponse.SerializeToString), 'AppliedPlan': grpc.unary_unary_rpc_method_handler(servicer.AppliedPlan, request_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAppliedPlanRequest.FromString, response_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAppliedPlanResponse.SerializeToString), 'UpgradedConsensusState': grpc.unary_unary_rpc_method_handler(servicer.UpgradedConsensusState, request_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryUpgradedConsensusStateRequest.FromString, response_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryUpgradedConsensusStateResponse.SerializeToString), 'ModuleVersions': grpc.unary_unary_rpc_method_handler(servicer.ModuleVersions, request_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryModuleVersionsRequest.FromString, response_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryModuleVersionsResponse.SerializeToString), 'Authority': grpc.unary_unary_rpc_method_handler(servicer.Authority, request_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAuthorityRequest.FromString, response_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAuthorityResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.upgrade.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC upgrade querier service.\n    '

    @staticmethod
    def CurrentPlan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.upgrade.v1beta1.Query/CurrentPlan', cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryCurrentPlanRequest.SerializeToString, cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryCurrentPlanResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppliedPlan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.upgrade.v1beta1.Query/AppliedPlan', cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAppliedPlanRequest.SerializeToString, cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAppliedPlanResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpgradedConsensusState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState', cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryUpgradedConsensusStateRequest.SerializeToString, cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryUpgradedConsensusStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModuleVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.upgrade.v1beta1.Query/ModuleVersions', cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryModuleVersionsRequest.SerializeToString, cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryModuleVersionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.upgrade.v1beta1.Query/Authority', cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAuthorityRequest.SerializeToString, cosmos_dot_upgrade_dot_v1beta1_dot_query__pb2.QueryAuthorityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
