# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk/sdk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kaikosdk.stream.aggregated_price_v1 import request_pb2 as sdk_dot_stream_dot_aggregated__price__v1_dot_request__pb2
from kaikosdk.stream.aggregated_price_v1 import response_pb2 as sdk_dot_stream_dot_aggregated__price__v1_dot_response__pb2
from kaikosdk.stream.aggregates_ohlcv_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_request__pb2
from kaikosdk.stream.aggregates_ohlcv_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_response__pb2
from kaikosdk.stream.aggregates_vwap_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__vwap__v1_dot_request__pb2
from kaikosdk.stream.aggregates_vwap_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__vwap__v1_dot_response__pb2
from kaikosdk.stream.aggregates_direct_exchange_rate_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_request__pb2
from kaikosdk.stream.aggregates_direct_exchange_rate_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_response__pb2
from kaikosdk.stream.aggregates_spot_exchange_rate_v1 import request_pb2 as sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_request__pb2
from kaikosdk.stream.aggregates_spot_exchange_rate_v1 import response_pb2 as sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_response__pb2
from kaikosdk.stream.derivatives_price_v2 import request_pb2 as sdk_dot_stream_dot_derivatives__price__v2_dot_request__pb2
from kaikosdk.stream.derivatives_price_v2 import response_pb2 as sdk_dot_stream_dot_derivatives__price__v2_dot_response__pb2
from kaikosdk.stream.index_v1 import request_pb2 as sdk_dot_stream_dot_index__v1_dot_request__pb2
from kaikosdk.stream.index_v1 import response_pb2 as sdk_dot_stream_dot_index__v1_dot_response__pb2
from kaikosdk.stream.market_update_v1 import request_pb2 as sdk_dot_stream_dot_market__update__v1_dot_request__pb2
from kaikosdk.stream.market_update_v1 import response_pb2 as sdk_dot_stream_dot_market__update__v1_dot_response__pb2
from kaikosdk.stream.trades_v1 import request_pb2 as sdk_dot_stream_dot_trades__v1_dot_request__pb2
from kaikosdk.stream.trades_v1 import response_pb2 as sdk_dot_stream_dot_trades__v1_dot_response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk/sdk.proto',
  package='kaikosdk',
  syntax='proto3',
  serialized_options=b'\n\rcom.kaiko.sdkB\010SdkProtoP\001Z*github.com/kaikodata/kaiko-go-sdk;kaikosdk\252\002\010KaikoSdk',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rsdk/sdk.proto\x12\x08kaikosdk\x1a,sdk/stream/aggregated_price_v1/request.proto\x1a-sdk/stream/aggregated_price_v1/response.proto\x1a,sdk/stream/aggregates_ohlcv_v1/request.proto\x1a-sdk/stream/aggregates_ohlcv_v1/response.proto\x1a+sdk/stream/aggregates_vwap_v1/request.proto\x1a,sdk/stream/aggregates_vwap_v1/response.proto\x1a;sdk/stream/aggregates_direct_exchange_rate_v1/request.proto\x1a<sdk/stream/aggregates_direct_exchange_rate_v1/response.proto\x1a\x39sdk/stream/aggregates_spot_exchange_rate_v1/request.proto\x1a:sdk/stream/aggregates_spot_exchange_rate_v1/response.proto\x1a-sdk/stream/derivatives_price_v2/request.proto\x1a.sdk/stream/derivatives_price_v2/response.proto\x1a!sdk/stream/index_v1/request.proto\x1a\"sdk/stream/index_v1/response.proto\x1a)sdk/stream/market_update_v1/request.proto\x1a*sdk/stream/market_update_v1/response.proto\x1a\"sdk/stream/trades_v1/request.proto\x1a#sdk/stream/trades_v1/response.proto2\x86\x01\n\x1eStreamAggregatedPriceServiceV1\x12\x64\n\tSubscribe\x12(.kaikosdk.StreamAggregatedPriceRequestV1\x1a).kaikosdk.StreamAggregatedPriceResponseV1\"\x00\x30\x01\x32\x86\x01\n\x1eStreamAggregatesOHLCVServiceV1\x12\x64\n\tSubscribe\x12(.kaikosdk.StreamAggregatesOHLCVRequestV1\x1a).kaikosdk.StreamAggregatesOHLCVResponseV1\"\x00\x30\x01\x32\xa7\x01\n)StreamAggregatesSpotExchangeRateServiceV1\x12z\n\tSubscribe\x12\x33.kaikosdk.StreamAggregatesSpotExchangeRateRequestV1\x1a\x34.kaikosdk.StreamAggregatesSpotExchangeRateResponseV1\"\x00\x30\x01\x32\xad\x01\n+StreamAggregatesDirectExchangeRateServiceV1\x12~\n\tSubscribe\x12\x35.kaikosdk.StreamAggregatesDirectExchangeRateRequestV1\x1a\x36.kaikosdk.StreamAggregatesDirectExchangeRateResponseV1\"\x00\x30\x01\x32k\n\x15StreamTradesServiceV1\x12R\n\tSubscribe\x12\x1f.kaikosdk.StreamTradesRequestV1\x1a .kaikosdk.StreamTradesResponseV1\"\x00\x30\x01\x32\x83\x01\n\x1dStreamAggregatesVWAPServiceV1\x12\x62\n\tSubscribe\x12\'.kaikosdk.StreamAggregatesVWAPRequestV1\x1a(.kaikosdk.StreamAggregatesVWAPResponseV1\"\x00\x30\x01\x32\x89\x01\n\x1fStreamDerivativesPriceServiceV2\x12\x66\n\tSubscribe\x12).kaikosdk.StreamDerivativesPriceRequestV2\x1a*.kaikosdk.StreamDerivativesPriceResponseV2\"\x00\x30\x01\x32v\n\x14StreamIndexServiceV1\x12^\n\tSubscribe\x12%.kaikosdk.StreamIndexServiceRequestV1\x1a&.kaikosdk.StreamIndexServiceResponseV1\"\x00\x30\x01\x32}\n\x1bStreamMarketUpdateServiceV1\x12^\n\tSubscribe\x12%.kaikosdk.StreamMarketUpdateRequestV1\x1a&.kaikosdk.StreamMarketUpdateResponseV1\"\x00\x30\x01\x42R\n\rcom.kaiko.sdkB\x08SdkProtoP\x01Z*github.com/kaikodata/kaiko-go-sdk;kaikosdk\xaa\x02\x08KaikoSdkb\x06proto3'
  ,
  dependencies=[sdk_dot_stream_dot_aggregated__price__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregated__price__v1_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__vwap__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__vwap__v1_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_derivatives__price__v2_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_derivatives__price__v2_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_index__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_index__v1_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_market__update__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_market__update__v1_dot_response__pb2.DESCRIPTOR,sdk_dot_stream_dot_trades__v1_dot_request__pb2.DESCRIPTOR,sdk_dot_stream_dot_trades__v1_dot_response__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_STREAMAGGREGATEDPRICESERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamAggregatedPriceServiceV1',
  full_name='kaikosdk.StreamAggregatedPriceServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=873,
  serialized_end=1007,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamAggregatedPriceServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_aggregated__price__v1_dot_request__pb2._STREAMAGGREGATEDPRICEREQUESTV1,
    output_type=sdk_dot_stream_dot_aggregated__price__v1_dot_response__pb2._STREAMAGGREGATEDPRICERESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMAGGREGATEDPRICESERVICEV1)

DESCRIPTOR.services_by_name['StreamAggregatedPriceServiceV1'] = _STREAMAGGREGATEDPRICESERVICEV1


_STREAMAGGREGATESOHLCVSERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamAggregatesOHLCVServiceV1',
  full_name='kaikosdk.StreamAggregatesOHLCVServiceV1',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1010,
  serialized_end=1144,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamAggregatesOHLCVServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_request__pb2._STREAMAGGREGATESOHLCVREQUESTV1,
    output_type=sdk_dot_stream_dot_aggregates__ohlcv__v1_dot_response__pb2._STREAMAGGREGATESOHLCVRESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMAGGREGATESOHLCVSERVICEV1)

DESCRIPTOR.services_by_name['StreamAggregatesOHLCVServiceV1'] = _STREAMAGGREGATESOHLCVSERVICEV1


_STREAMAGGREGATESSPOTEXCHANGERATESERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamAggregatesSpotExchangeRateServiceV1',
  full_name='kaikosdk.StreamAggregatesSpotExchangeRateServiceV1',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1147,
  serialized_end=1314,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamAggregatesSpotExchangeRateServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_request__pb2._STREAMAGGREGATESSPOTEXCHANGERATEREQUESTV1,
    output_type=sdk_dot_stream_dot_aggregates__spot__exchange__rate__v1_dot_response__pb2._STREAMAGGREGATESSPOTEXCHANGERATERESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMAGGREGATESSPOTEXCHANGERATESERVICEV1)

DESCRIPTOR.services_by_name['StreamAggregatesSpotExchangeRateServiceV1'] = _STREAMAGGREGATESSPOTEXCHANGERATESERVICEV1


_STREAMAGGREGATESDIRECTEXCHANGERATESERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamAggregatesDirectExchangeRateServiceV1',
  full_name='kaikosdk.StreamAggregatesDirectExchangeRateServiceV1',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1317,
  serialized_end=1490,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamAggregatesDirectExchangeRateServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_request__pb2._STREAMAGGREGATESDIRECTEXCHANGERATEREQUESTV1,
    output_type=sdk_dot_stream_dot_aggregates__direct__exchange__rate__v1_dot_response__pb2._STREAMAGGREGATESDIRECTEXCHANGERATERESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMAGGREGATESDIRECTEXCHANGERATESERVICEV1)

DESCRIPTOR.services_by_name['StreamAggregatesDirectExchangeRateServiceV1'] = _STREAMAGGREGATESDIRECTEXCHANGERATESERVICEV1


_STREAMTRADESSERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamTradesServiceV1',
  full_name='kaikosdk.StreamTradesServiceV1',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1492,
  serialized_end=1599,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamTradesServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_trades__v1_dot_request__pb2._STREAMTRADESREQUESTV1,
    output_type=sdk_dot_stream_dot_trades__v1_dot_response__pb2._STREAMTRADESRESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMTRADESSERVICEV1)

DESCRIPTOR.services_by_name['StreamTradesServiceV1'] = _STREAMTRADESSERVICEV1


_STREAMAGGREGATESVWAPSERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamAggregatesVWAPServiceV1',
  full_name='kaikosdk.StreamAggregatesVWAPServiceV1',
  file=DESCRIPTOR,
  index=5,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1602,
  serialized_end=1733,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamAggregatesVWAPServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_aggregates__vwap__v1_dot_request__pb2._STREAMAGGREGATESVWAPREQUESTV1,
    output_type=sdk_dot_stream_dot_aggregates__vwap__v1_dot_response__pb2._STREAMAGGREGATESVWAPRESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMAGGREGATESVWAPSERVICEV1)

DESCRIPTOR.services_by_name['StreamAggregatesVWAPServiceV1'] = _STREAMAGGREGATESVWAPSERVICEV1


_STREAMDERIVATIVESPRICESERVICEV2 = _descriptor.ServiceDescriptor(
  name='StreamDerivativesPriceServiceV2',
  full_name='kaikosdk.StreamDerivativesPriceServiceV2',
  file=DESCRIPTOR,
  index=6,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1736,
  serialized_end=1873,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamDerivativesPriceServiceV2.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_derivatives__price__v2_dot_request__pb2._STREAMDERIVATIVESPRICEREQUESTV2,
    output_type=sdk_dot_stream_dot_derivatives__price__v2_dot_response__pb2._STREAMDERIVATIVESPRICERESPONSEV2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMDERIVATIVESPRICESERVICEV2)

DESCRIPTOR.services_by_name['StreamDerivativesPriceServiceV2'] = _STREAMDERIVATIVESPRICESERVICEV2


_STREAMINDEXSERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamIndexServiceV1',
  full_name='kaikosdk.StreamIndexServiceV1',
  file=DESCRIPTOR,
  index=7,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1875,
  serialized_end=1993,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamIndexServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_index__v1_dot_request__pb2._STREAMINDEXSERVICEREQUESTV1,
    output_type=sdk_dot_stream_dot_index__v1_dot_response__pb2._STREAMINDEXSERVICERESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMINDEXSERVICEV1)

DESCRIPTOR.services_by_name['StreamIndexServiceV1'] = _STREAMINDEXSERVICEV1


_STREAMMARKETUPDATESERVICEV1 = _descriptor.ServiceDescriptor(
  name='StreamMarketUpdateServiceV1',
  full_name='kaikosdk.StreamMarketUpdateServiceV1',
  file=DESCRIPTOR,
  index=8,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1995,
  serialized_end=2120,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='kaikosdk.StreamMarketUpdateServiceV1.Subscribe',
    index=0,
    containing_service=None,
    input_type=sdk_dot_stream_dot_market__update__v1_dot_request__pb2._STREAMMARKETUPDATEREQUESTV1,
    output_type=sdk_dot_stream_dot_market__update__v1_dot_response__pb2._STREAMMARKETUPDATERESPONSEV1,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMMARKETUPDATESERVICEV1)

DESCRIPTOR.services_by_name['StreamMarketUpdateServiceV1'] = _STREAMMARKETUPDATESERVICEV1

# @@protoc_insertion_point(module_scope)
