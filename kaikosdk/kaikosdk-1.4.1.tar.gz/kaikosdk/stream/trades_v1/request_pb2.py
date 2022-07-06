# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk/stream/trades_v1/request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kaikosdk.core import instrument_criteria_pb2 as sdk_dot_core_dot_instrument__criteria__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk/stream/trades_v1/request.proto',
  package='kaikosdk',
  syntax='proto3',
  serialized_options=b'\n\036com.kaiko.sdk.stream.trades_v1P\001Z<github.com/kaikodata/kaiko-go-sdk/stream/trades_v1;trades_v1\252\002\030KaikoSdk.Stream.TradesV1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"sdk/stream/trades_v1/request.proto\x12\x08kaikosdk\x1a\"sdk/core/instrument_criteria.proto\"R\n\x15StreamTradesRequestV1\x12\x39\n\x13instrument_criteria\x18\x01 \x01(\x0b\x32\x1c.kaikosdk.InstrumentCriteriaB{\n\x1e\x63om.kaiko.sdk.stream.trades_v1P\x01Z<github.com/kaikodata/kaiko-go-sdk/stream/trades_v1;trades_v1\xaa\x02\x18KaikoSdk.Stream.TradesV1b\x06proto3'
  ,
  dependencies=[sdk_dot_core_dot_instrument__criteria__pb2.DESCRIPTOR,])




_STREAMTRADESREQUESTV1 = _descriptor.Descriptor(
  name='StreamTradesRequestV1',
  full_name='kaikosdk.StreamTradesRequestV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument_criteria', full_name='kaikosdk.StreamTradesRequestV1.instrument_criteria', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=166,
)

_STREAMTRADESREQUESTV1.fields_by_name['instrument_criteria'].message_type = sdk_dot_core_dot_instrument__criteria__pb2._INSTRUMENTCRITERIA
DESCRIPTOR.message_types_by_name['StreamTradesRequestV1'] = _STREAMTRADESREQUESTV1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamTradesRequestV1 = _reflection.GeneratedProtocolMessageType('StreamTradesRequestV1', (_message.Message,), {
  'DESCRIPTOR' : _STREAMTRADESREQUESTV1,
  '__module__' : 'sdk.stream.trades_v1.request_pb2'
  # @@protoc_insertion_point(class_scope:kaikosdk.StreamTradesRequestV1)
  })
_sym_db.RegisterMessage(StreamTradesRequestV1)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
