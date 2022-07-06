# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import Common_pb2 as Common__pb2
from . import SomeIpNode_pb2 as SomeIpNode__pb2


class SomeIpNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartSomeIpStack = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/StartSomeIpStack',
                request_serializer=Common__pb2.net_info.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.StopSomeIpStack = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/StopSomeIpStack',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.AddSomeIpArxml = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/AddSomeIpArxml',
                request_serializer=Common__pb2.file_path.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.GetSomeIpServiceInfos = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/GetSomeIpServiceInfos',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=SomeIpNode__pb2.someip_info.FromString,
                )
        self.UpdateSomeipServiceConfig = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/UpdateSomeipServiceConfig',
                request_serializer=SomeIpNode__pb2.service_tag.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.Reset = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/Reset',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )
        self.SomeipCallSync = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/SomeipCallSync',
                request_serializer=SomeIpNode__pb2.someip_call_context.SerializeToString,
                response_deserializer=SomeIpNode__pb2.someip_response_context.FromString,
                )
        self.GetSomeipStackStatus = channel.unary_unary(
                '/SomeIpNode.SomeIpNode/GetSomeipStackStatus',
                request_serializer=Common__pb2.empty.SerializeToString,
                response_deserializer=Common__pb2.result.FromString,
                )


class SomeIpNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartSomeIpStack(self, request, context):
        """开启 SomeIp 协议栈
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopSomeIpStack(self, request, context):
        """停止 SomeIp 协议栈
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSomeIpArxml(self, request, context):
        """添加 SomeIpArxml
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSomeIpServiceInfos(self, request, context):
        """获取所有的 Service 信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSomeipServiceConfig(self, request, context):
        """更新 Someip service 的配置信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """复位
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SomeipCallSync(self, request, context):
        """同步发送Someip Call
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSomeipStackStatus(self, request, context):
        """获取 Someip 协议栈状态
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SomeIpNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartSomeIpStack': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSomeIpStack,
                    request_deserializer=Common__pb2.net_info.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'StopSomeIpStack': grpc.unary_unary_rpc_method_handler(
                    servicer.StopSomeIpStack,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'AddSomeIpArxml': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSomeIpArxml,
                    request_deserializer=Common__pb2.file_path.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'GetSomeIpServiceInfos': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSomeIpServiceInfos,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=SomeIpNode__pb2.someip_info.SerializeToString,
            ),
            'UpdateSomeipServiceConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSomeipServiceConfig,
                    request_deserializer=SomeIpNode__pb2.service_tag.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
            'SomeipCallSync': grpc.unary_unary_rpc_method_handler(
                    servicer.SomeipCallSync,
                    request_deserializer=SomeIpNode__pb2.someip_call_context.FromString,
                    response_serializer=SomeIpNode__pb2.someip_response_context.SerializeToString,
            ),
            'GetSomeipStackStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSomeipStackStatus,
                    request_deserializer=Common__pb2.empty.FromString,
                    response_serializer=Common__pb2.result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SomeIpNode.SomeIpNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SomeIpNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartSomeIpStack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/StartSomeIpStack',
            Common__pb2.net_info.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopSomeIpStack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/StopSomeIpStack',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSomeIpArxml(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/AddSomeIpArxml',
            Common__pb2.file_path.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSomeIpServiceInfos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/GetSomeIpServiceInfos',
            Common__pb2.empty.SerializeToString,
            SomeIpNode__pb2.someip_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSomeipServiceConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/UpdateSomeipServiceConfig',
            SomeIpNode__pb2.service_tag.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/Reset',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SomeipCallSync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/SomeipCallSync',
            SomeIpNode__pb2.someip_call_context.SerializeToString,
            SomeIpNode__pb2.someip_response_context.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSomeipStackStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SomeIpNode.SomeIpNode/GetSomeipStackStatus',
            Common__pb2.empty.SerializeToString,
            Common__pb2.result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
