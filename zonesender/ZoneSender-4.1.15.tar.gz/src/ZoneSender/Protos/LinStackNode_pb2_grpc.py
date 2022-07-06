# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import Common_pb2 as Common__pb2
from . import LinStackNode_pb2 as LinStackNode__pb2


class LinStackNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Reset = channel.unary_unary(
                '/LinStackNode.LinStackNode/Reset',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.SetConfig = channel.unary_unary(
                '/LinStackNode.LinStackNode/SetConfig',
                request_serializer=LinStackNode__pb2.lin_stack_configs.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.StartLinStack = channel.unary_unary(
                '/LinStackNode.LinStackNode/StartLinStack',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.StopLinStack = channel.unary_unary(
                '/LinStackNode.LinStackNode/StopLinStack',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.SetMessageSimulation = channel.unary_unary(
                '/LinStackNode.LinStackNode/SetMessageSimulation',
                request_serializer=LinStackNode__pb2.lin_message_config.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.SetHeaderSimulation = channel.unary_unary(
                '/LinStackNode.LinStackNode/SetHeaderSimulation',
                request_serializer=LinStackNode__pb2.lin_header_config.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/LinStackNode.LinStackNode/GetStatus',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=LinStackNode__pb2.lin_stack_status.FromString,
                )


class LinStackNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Reset(self, request, context):
        """复位 LinStackNode
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfig(self, request, context):
        """设置 LinStack 的配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartLinStack(self, request, context):
        """启动 LinStack
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopLinStack(self, request, context):
        """关闭 LinStack
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMessageSimulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetHeaderSimulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """获取 LinStack 的状态
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LinStackNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=LinStackNode__pb2.lin_stack_configs.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'StartLinStack': grpc.unary_unary_rpc_method_handler(
                    servicer.StartLinStack,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'StopLinStack': grpc.unary_unary_rpc_method_handler(
                    servicer.StopLinStack,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'SetMessageSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMessageSimulation,
                    request_deserializer=LinStackNode__pb2.lin_message_config.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'SetHeaderSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.SetHeaderSimulation,
                    request_deserializer=LinStackNode__pb2.lin_header_config.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=LinStackNode__pb2.lin_stack_status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LinStackNode.LinStackNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LinStackNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LinStackNode.LinStackNode/Reset',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LinStackNode.LinStackNode/SetConfig',
            LinStackNode__pb2.lin_stack_configs.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartLinStack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LinStackNode.LinStackNode/StartLinStack',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopLinStack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LinStackNode.LinStackNode/StopLinStack',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMessageSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LinStackNode.LinStackNode/SetMessageSimulation',
            LinStackNode__pb2.lin_message_config.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetHeaderSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LinStackNode.LinStackNode/SetHeaderSimulation',
            LinStackNode__pb2.lin_header_config.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LinStackNode.LinStackNode/GetStatus',
            Common__pb2.empty.SerializeToString,
            LinStackNode__pb2.lin_stack_status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
