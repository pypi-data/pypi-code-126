# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from spaceone.api.cost_analysis.plugin import cost_pb2 as spaceone_dot_api_dot_cost__analysis_dot_plugin_dot_cost__pb2


class CostStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_data = channel.unary_stream(
                '/spaceone.api.cost_analysis.plugin.Cost/get_data',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_plugin_dot_cost__pb2.GetDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_plugin_dot_cost__pb2.CostsInfo.FromString,
                )


class CostServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_data(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CostServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_data': grpc.unary_stream_rpc_method_handler(
                    servicer.get_data,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_plugin_dot_cost__pb2.GetDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_plugin_dot_cost__pb2.CostsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.cost_analysis.plugin.Cost', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Cost(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spaceone.api.cost_analysis.plugin.Cost/get_data',
            spaceone_dot_api_dot_cost__analysis_dot_plugin_dot_cost__pb2.GetDataRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_plugin_dot_cost__pb2.CostsInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
