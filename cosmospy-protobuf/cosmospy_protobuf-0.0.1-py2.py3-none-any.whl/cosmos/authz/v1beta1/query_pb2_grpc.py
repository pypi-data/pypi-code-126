
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.authz.v1beta1 import query_pb2 as cosmos_dot_authz_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Grants = channel.unary_unary('/cosmos.authz.v1beta1.Query/Grants', request_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.SerializeToString, response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.FromString)
        self.GranterGrants = channel.unary_unary('/cosmos.authz.v1beta1.Query/GranterGrants', request_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsRequest.SerializeToString, response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsResponse.FromString)
        self.GranteeGrants = channel.unary_unary('/cosmos.authz.v1beta1.Query/GranteeGrants', request_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsRequest.SerializeToString, response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def Grants(self, request, context):
        'Returns list of `Authorization`, granted to the grantee by the granter.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GranterGrants(self, request, context):
        'GranterGrants returns list of `GrantAuthorization`, granted by granter.\n\n        Since: cosmos-sdk 0.46\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GranteeGrants(self, request, context):
        'GranteeGrants returns a list of `GrantAuthorization` by grantee.\n\n        Since: cosmos-sdk 0.46\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Grants': grpc.unary_unary_rpc_method_handler(servicer.Grants, request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.FromString, response_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.SerializeToString), 'GranterGrants': grpc.unary_unary_rpc_method_handler(servicer.GranterGrants, request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsRequest.FromString, response_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsResponse.SerializeToString), 'GranteeGrants': grpc.unary_unary_rpc_method_handler(servicer.GranteeGrants, request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsRequest.FromString, response_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.authz.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def Grants(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.authz.v1beta1.Query/Grants', cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.SerializeToString, cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GranterGrants(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.authz.v1beta1.Query/GranterGrants', cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsRequest.SerializeToString, cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GranteeGrants(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.authz.v1beta1.Query/GranteeGrants', cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsRequest.SerializeToString, cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
