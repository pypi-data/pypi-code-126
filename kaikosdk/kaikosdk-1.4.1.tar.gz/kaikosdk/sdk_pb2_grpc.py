# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kaikosdk.stream.aggregated_price_v1 import request_pb2 as sdk_dot_stream_dot_aggregated__price__v1_dot_request__pb2
from kaikosdk.stream.aggregated_price_v1 import response_pb2 as sdk_dot_stream_dot_aggregated__price__v1_dot_response__pb2
from kaikosdk.stream.aggregates_direct_exchange_rate_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_request__pb2
from kaikosdk.stream.aggregates_direct_exchange_rate_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_response__pb2
from kaikosdk.stream.aggregates_ohlcv_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_request__pb2
from kaikosdk.stream.aggregates_ohlcv_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_response__pb2
from kaikosdk.stream.aggregates_spot_exchange_rate_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_request__pb2
from kaikosdk.stream.aggregates_spot_exchange_rate_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_response__pb2
from kaikosdk.stream.aggregates_vwap_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__vwap__v1_dot_request__pb2
from kaikosdk.stream.aggregates_vwap_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__vwap__v1_dot_response__pb2
from kaikosdk.stream.derivatives_price_v2 import request_pb2 as sdk_dot_stream_dot_derivatives__price__v2_dot_request__pb2
from kaikosdk.stream.derivatives_price_v2 import response_pb2 as sdk_dot_stream_dot_derivatives__price__v2_dot_response__pb2
from kaikosdk.stream.index_v1 import request_pb2 as sdk_dot_stream_dot_index__v1_dot_request__pb2
from kaikosdk.stream.index_v1 import response_pb2 as sdk_dot_stream_dot_index__v1_dot_response__pb2
from kaikosdk.stream.market_update_v1 import request_pb2 as sdk_dot_stream_dot_market__update__v1_dot_request__pb2
from kaikosdk.stream.market_update_v1 import response_pb2 as sdk_dot_stream_dot_market__update__v1_dot_response__pb2
from kaikosdk.stream.trades_v1 import request_pb2 as sdk_dot_stream_dot_trades__v1_dot_request__pb2
from kaikosdk.stream.trades_v1 import response_pb2 as sdk_dot_stream_dot_trades__v1_dot_response__pb2


class StreamAggregatedPriceServiceV1Stub(object):
    """Service for streaming Aggregated Price V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamAggregatedPriceServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_aggregated__price__v1_dot_request__pb2.StreamAggregatedPriceRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_aggregated__price__v1_dot_response__pb2.StreamAggregatedPriceResponseV1.FromString,
                )


class StreamAggregatedPriceServiceV1Servicer(object):
    """Service for streaming Aggregated Price V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamAggregatedPriceServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_aggregated__price__v1_dot_request__pb2.StreamAggregatedPriceRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_aggregated__price__v1_dot_response__pb2.StreamAggregatedPriceResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamAggregatedPriceServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamAggregatedPriceServiceV1(object):
    """Service for streaming Aggregated Price V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamAggregatedPriceServiceV1/Subscribe',
            sdk_dot_stream_dot_aggregated__price__v1_dot_request__pb2.StreamAggregatedPriceRequestV1.SerializeToString,
            sdk_dot_stream_dot_aggregated__price__v1_dot_response__pb2.StreamAggregatedPriceResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamAggregatesOHLCVServiceV1Stub(object):
    """Service for streaming OHLCV V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamAggregatesOHLCVServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_request__pb2.StreamAggregatesOHLCVRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_response__pb2.StreamAggregatesOHLCVResponseV1.FromString,
                )


class StreamAggregatesOHLCVServiceV1Servicer(object):
    """Service for streaming OHLCV V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamAggregatesOHLCVServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_request__pb2.StreamAggregatesOHLCVRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_response__pb2.StreamAggregatesOHLCVResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamAggregatesOHLCVServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamAggregatesOHLCVServiceV1(object):
    """Service for streaming OHLCV V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamAggregatesOHLCVServiceV1/Subscribe',
            sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_request__pb2.StreamAggregatesOHLCVRequestV1.SerializeToString,
            sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_response__pb2.StreamAggregatesOHLCVResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamAggregatesSpotExchangeRateServiceV1Stub(object):
    """Service for streaming Spot exchange rate V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamAggregatesSpotExchangeRateServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_request__pb2.StreamAggregatesSpotExchangeRateRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_response__pb2.StreamAggregatesSpotExchangeRateResponseV1.FromString,
                )


class StreamAggregatesSpotExchangeRateServiceV1Servicer(object):
    """Service for streaming Spot exchange rate V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamAggregatesSpotExchangeRateServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_request__pb2.StreamAggregatesSpotExchangeRateRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_response__pb2.StreamAggregatesSpotExchangeRateResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamAggregatesSpotExchangeRateServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamAggregatesSpotExchangeRateServiceV1(object):
    """Service for streaming Spot exchange rate V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamAggregatesSpotExchangeRateServiceV1/Subscribe',
            sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_request__pb2.StreamAggregatesSpotExchangeRateRequestV1.SerializeToString,
            sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_response__pb2.StreamAggregatesSpotExchangeRateResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamAggregatesDirectExchangeRateServiceV1Stub(object):
    """Service for streaming market update V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamAggregatesDirectExchangeRateServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_request__pb2.StreamAggregatesDirectExchangeRateRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_response__pb2.StreamAggregatesDirectExchangeRateResponseV1.FromString,
                )


class StreamAggregatesDirectExchangeRateServiceV1Servicer(object):
    """Service for streaming market update V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamAggregatesDirectExchangeRateServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_request__pb2.StreamAggregatesDirectExchangeRateRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_response__pb2.StreamAggregatesDirectExchangeRateResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamAggregatesDirectExchangeRateServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamAggregatesDirectExchangeRateServiceV1(object):
    """Service for streaming market update V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamAggregatesDirectExchangeRateServiceV1/Subscribe',
            sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_request__pb2.StreamAggregatesDirectExchangeRateRequestV1.SerializeToString,
            sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_response__pb2.StreamAggregatesDirectExchangeRateResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamTradesServiceV1Stub(object):
    """Service for streaming trades V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamTradesServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_trades__v1_dot_request__pb2.StreamTradesRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_trades__v1_dot_response__pb2.StreamTradesResponseV1.FromString,
                )


class StreamTradesServiceV1Servicer(object):
    """Service for streaming trades V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamTradesServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_trades__v1_dot_request__pb2.StreamTradesRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_trades__v1_dot_response__pb2.StreamTradesResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamTradesServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamTradesServiceV1(object):
    """Service for streaming trades V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamTradesServiceV1/Subscribe',
            sdk_dot_stream_dot_trades__v1_dot_request__pb2.StreamTradesRequestV1.SerializeToString,
            sdk_dot_stream_dot_trades__v1_dot_response__pb2.StreamTradesResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamAggregatesVWAPServiceV1Stub(object):
    """Service for streaming VWAP V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamAggregatesVWAPServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_aggregates__vwap__v1_dot_request__pb2.StreamAggregatesVWAPRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_aggregates__vwap__v1_dot_response__pb2.StreamAggregatesVWAPResponseV1.FromString,
                )


class StreamAggregatesVWAPServiceV1Servicer(object):
    """Service for streaming VWAP V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamAggregatesVWAPServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_aggregates__vwap__v1_dot_request__pb2.StreamAggregatesVWAPRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_aggregates__vwap__v1_dot_response__pb2.StreamAggregatesVWAPResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamAggregatesVWAPServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamAggregatesVWAPServiceV1(object):
    """Service for streaming VWAP V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamAggregatesVWAPServiceV1/Subscribe',
            sdk_dot_stream_dot_aggregates__vwap__v1_dot_request__pb2.StreamAggregatesVWAPRequestV1.SerializeToString,
            sdk_dot_stream_dot_aggregates__vwap__v1_dot_response__pb2.StreamAggregatesVWAPResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamDerivativesPriceServiceV2Stub(object):
    """Service for streaming derivatives price V2
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamDerivativesPriceServiceV2/Subscribe',
                request_serializer=sdk_dot_stream_dot_derivatives__price__v2_dot_request__pb2.StreamDerivativesPriceRequestV2.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_derivatives__price__v2_dot_response__pb2.StreamDerivativesPriceResponseV2.FromString,
                )


class StreamDerivativesPriceServiceV2Servicer(object):
    """Service for streaming derivatives price V2
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamDerivativesPriceServiceV2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_derivatives__price__v2_dot_request__pb2.StreamDerivativesPriceRequestV2.FromString,
                    response_serializer=sdk_dot_stream_dot_derivatives__price__v2_dot_response__pb2.StreamDerivativesPriceResponseV2.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamDerivativesPriceServiceV2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamDerivativesPriceServiceV2(object):
    """Service for streaming derivatives price V2
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamDerivativesPriceServiceV2/Subscribe',
            sdk_dot_stream_dot_derivatives__price__v2_dot_request__pb2.StreamDerivativesPriceRequestV2.SerializeToString,
            sdk_dot_stream_dot_derivatives__price__v2_dot_response__pb2.StreamDerivativesPriceResponseV2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamIndexServiceV1Stub(object):
    """Service for streaming index V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamIndexServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_index__v1_dot_request__pb2.StreamIndexServiceRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_index__v1_dot_response__pb2.StreamIndexServiceResponseV1.FromString,
                )


class StreamIndexServiceV1Servicer(object):
    """Service for streaming index V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamIndexServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_index__v1_dot_request__pb2.StreamIndexServiceRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_index__v1_dot_response__pb2.StreamIndexServiceResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamIndexServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamIndexServiceV1(object):
    """Service for streaming index V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamIndexServiceV1/Subscribe',
            sdk_dot_stream_dot_index__v1_dot_request__pb2.StreamIndexServiceRequestV1.SerializeToString,
            sdk_dot_stream_dot_index__v1_dot_response__pb2.StreamIndexServiceResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StreamMarketUpdateServiceV1Stub(object):
    """Service for streaming market update V1
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/kaikosdk.StreamMarketUpdateServiceV1/Subscribe',
                request_serializer=sdk_dot_stream_dot_market__update__v1_dot_request__pb2.StreamMarketUpdateRequestV1.SerializeToString,
                response_deserializer=sdk_dot_stream_dot_market__update__v1_dot_response__pb2.StreamMarketUpdateResponseV1.FromString,
                )


class StreamMarketUpdateServiceV1Servicer(object):
    """Service for streaming market update V1
    """

    def Subscribe(self, request, context):
        """Subscribe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamMarketUpdateServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=sdk_dot_stream_dot_market__update__v1_dot_request__pb2.StreamMarketUpdateRequestV1.FromString,
                    response_serializer=sdk_dot_stream_dot_market__update__v1_dot_response__pb2.StreamMarketUpdateResponseV1.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kaikosdk.StreamMarketUpdateServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamMarketUpdateServiceV1(object):
    """Service for streaming market update V1
    """

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kaikosdk.StreamMarketUpdateServiceV1/Subscribe',
            sdk_dot_stream_dot_market__update__v1_dot_request__pb2.StreamMarketUpdateRequestV1.SerializeToString,
            sdk_dot_stream_dot_market__update__v1_dot_response__pb2.StreamMarketUpdateResponseV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
