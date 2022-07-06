
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from .....cosmos.base.tendermint.v1beta1 import query_pb2 as cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2

class ServiceStub(object):
    'Service defines the gRPC querier service for tendermint queries.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.GetNodeInfo = channel.unary_unary('/cosmos.base.tendermint.v1beta1.Service/GetNodeInfo', request_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetNodeInfoRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetNodeInfoResponse.FromString)
        self.GetSyncing = channel.unary_unary('/cosmos.base.tendermint.v1beta1.Service/GetSyncing', request_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetSyncingRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetSyncingResponse.FromString)
        self.GetLatestBlock = channel.unary_unary('/cosmos.base.tendermint.v1beta1.Service/GetLatestBlock', request_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestBlockRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestBlockResponse.FromString)
        self.GetBlockByHeight = channel.unary_unary('/cosmos.base.tendermint.v1beta1.Service/GetBlockByHeight', request_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetBlockByHeightRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetBlockByHeightResponse.FromString)
        self.GetLatestValidatorSet = channel.unary_unary('/cosmos.base.tendermint.v1beta1.Service/GetLatestValidatorSet', request_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestValidatorSetRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestValidatorSetResponse.FromString)
        self.GetValidatorSetByHeight = channel.unary_unary('/cosmos.base.tendermint.v1beta1.Service/GetValidatorSetByHeight', request_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetValidatorSetByHeightRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetValidatorSetByHeightResponse.FromString)
        self.ABCIQuery = channel.unary_unary('/cosmos.base.tendermint.v1beta1.Service/ABCIQuery', request_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.ABCIQueryRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.ABCIQueryResponse.FromString)

class ServiceServicer(object):
    'Service defines the gRPC querier service for tendermint queries.\n    '

    def GetNodeInfo(self, request, context):
        'GetNodeInfo queries the current node info.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSyncing(self, request, context):
        'GetSyncing queries node syncing.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestBlock(self, request, context):
        'GetLatestBlock returns the latest block.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockByHeight(self, request, context):
        'GetBlockByHeight queries block for given height.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestValidatorSet(self, request, context):
        'GetLatestValidatorSet queries latest validator-set.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidatorSetByHeight(self, request, context):
        'GetValidatorSetByHeight queries validator-set at a given height.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ABCIQuery(self, request, context):
        'ABCIQuery defines a query handler that supports ABCI queries directly to the\n        application, bypassing Tendermint completely. The ABCI query must contain\n        a valid and supported path, including app, custom, p2p, and store.\n\n        Since: cosmos-sdk 0.46\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetNodeInfo': grpc.unary_unary_rpc_method_handler(servicer.GetNodeInfo, request_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetNodeInfoRequest.FromString, response_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetNodeInfoResponse.SerializeToString), 'GetSyncing': grpc.unary_unary_rpc_method_handler(servicer.GetSyncing, request_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetSyncingRequest.FromString, response_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetSyncingResponse.SerializeToString), 'GetLatestBlock': grpc.unary_unary_rpc_method_handler(servicer.GetLatestBlock, request_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestBlockRequest.FromString, response_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestBlockResponse.SerializeToString), 'GetBlockByHeight': grpc.unary_unary_rpc_method_handler(servicer.GetBlockByHeight, request_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetBlockByHeightRequest.FromString, response_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetBlockByHeightResponse.SerializeToString), 'GetLatestValidatorSet': grpc.unary_unary_rpc_method_handler(servicer.GetLatestValidatorSet, request_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestValidatorSetRequest.FromString, response_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestValidatorSetResponse.SerializeToString), 'GetValidatorSetByHeight': grpc.unary_unary_rpc_method_handler(servicer.GetValidatorSetByHeight, request_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetValidatorSetByHeightRequest.FromString, response_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetValidatorSetByHeightResponse.SerializeToString), 'ABCIQuery': grpc.unary_unary_rpc_method_handler(servicer.ABCIQuery, request_deserializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.ABCIQueryRequest.FromString, response_serializer=cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.ABCIQueryResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.base.tendermint.v1beta1.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Service(object):
    'Service defines the gRPC querier service for tendermint queries.\n    '

    @staticmethod
    def GetNodeInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.tendermint.v1beta1.Service/GetNodeInfo', cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetNodeInfoRequest.SerializeToString, cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetNodeInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSyncing(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.tendermint.v1beta1.Service/GetSyncing', cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetSyncingRequest.SerializeToString, cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetSyncingResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLatestBlock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.tendermint.v1beta1.Service/GetLatestBlock', cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestBlockRequest.SerializeToString, cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestBlockResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockByHeight(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.tendermint.v1beta1.Service/GetBlockByHeight', cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetBlockByHeightRequest.SerializeToString, cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetBlockByHeightResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLatestValidatorSet(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.tendermint.v1beta1.Service/GetLatestValidatorSet', cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestValidatorSetRequest.SerializeToString, cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetLatestValidatorSetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidatorSetByHeight(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.tendermint.v1beta1.Service/GetValidatorSetByHeight', cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetValidatorSetByHeightRequest.SerializeToString, cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.GetValidatorSetByHeightResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ABCIQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.tendermint.v1beta1.Service/ABCIQuery', cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.ABCIQueryRequest.SerializeToString, cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_query__pb2.ABCIQueryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
