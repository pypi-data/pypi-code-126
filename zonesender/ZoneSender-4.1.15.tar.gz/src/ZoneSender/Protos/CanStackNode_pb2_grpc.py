# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import CanStackNode_pb2 as CanStackNode__pb2
from . import Common_pb2 as Common__pb2


class CanStackNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVersion = channel.unary_unary(
                '/CanStackNode.CanStackNode/GetVersion',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.version.FromString,
                )
        self.SetConfigs = channel.unary_unary(
                '/CanStackNode.CanStackNode/SetConfigs',
                request_serializer=CanStackNode__pb2.can_channel_configs.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.StartCanStack = channel.unary_unary(
                '/CanStackNode.CanStackNode/StartCanStack',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.StopCanStack = channel.unary_unary(
                '/CanStackNode.CanStackNode/StopCanStack',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.ClearSend = channel.unary_unary(
                '/CanStackNode.CanStackNode/ClearSend',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.ClearSubscribe = channel.unary_unary(
                '/CanStackNode.CanStackNode/ClearSubscribe',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.StartLog = channel.unary_unary(
                '/CanStackNode.CanStackNode/StartLog',
                request_serializer=CanStackNode__pb2.log_start_request.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.StopLog = channel.unary_unary(
                '/CanStackNode.CanStackNode/StopLog',
                request_serializer=CanStackNode__pb2.log_stop_request.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.ClearLogger = channel.unary_unary(
                '/CanStackNode.CanStackNode/ClearLogger',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.SetCrcRcConfig = channel.unary_unary(
                '/CanStackNode.CanStackNode/SetCrcRcConfig',
                request_serializer=CanStackNode__pb2.crc_rc_config.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )


class CanStackNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetVersion(self, request, context):
        """获取版本
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfigs(self, request, context):
        """配置CAN协议栈
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartCanStack(self, request, context):
        """启动CAN协议栈
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopCanStack(self, request, context):
        """停止CAN协议栈
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearSend(self, request, context):
        """清空定时CAN Message 发送列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearSubscribe(self, request, context):
        """清除所有订阅
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartLog(self, request, context):
        """
        创建一个记录任务，任务执行结果：
        0: 执行成功
        1: 未知的记录类型
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopLog(self, request, context):
        """
        停止一个记录任务, 请求结果:
        1: 取消记录成功
        0: 取消记录失败
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearLogger(self, request, context):
        """清除所有的 Logger
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCrcRcConfig(self, request, context):
        """配置 CRC 和 RC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CanStackNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersion,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.version.SerializeToString,
            ),
            'SetConfigs': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigs,
                    request_deserializer=CanStackNode__pb2.can_channel_configs.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'StartCanStack': grpc.unary_unary_rpc_method_handler(
                    servicer.StartCanStack,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'StopCanStack': grpc.unary_unary_rpc_method_handler(
                    servicer.StopCanStack,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'ClearSend': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearSend,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'ClearSubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearSubscribe,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'StartLog': grpc.unary_unary_rpc_method_handler(
                    servicer.StartLog,
                    request_deserializer=CanStackNode__pb2.log_start_request.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'StopLog': grpc.unary_unary_rpc_method_handler(
                    servicer.StopLog,
                    request_deserializer=CanStackNode__pb2.log_stop_request.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'ClearLogger': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearLogger,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'SetCrcRcConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCrcRcConfig,
                    request_deserializer=CanStackNode__pb2.crc_rc_config.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CanStackNode.CanStackNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CanStackNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/GetVersion',
            Common__pb2.empty.SerializeToString,
            Common__pb2.version.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConfigs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/SetConfigs',
            CanStackNode__pb2.can_channel_configs.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartCanStack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/StartCanStack',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopCanStack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/StopCanStack',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearSend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/ClearSend',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearSubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/ClearSubscribe',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/StartLog',
            CanStackNode__pb2.log_start_request.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/StopLog',
            CanStackNode__pb2.log_stop_request.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearLogger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/ClearLogger',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCrcRcConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CanStackNode.CanStackNode/SetCrcRcConfig',
            CanStackNode__pb2.crc_rc_config.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
