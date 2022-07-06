# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk/stream/aggregates_vwap_v1/response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk/stream/aggregates_vwap_v1/response.proto',
  package='kaikosdk',
  syntax='proto3',
  serialized_options=b'\n\'com.kaiko.sdk.stream.aggregates_vwap_v1P\001ZNgithub.com/kaikodata/kaiko-go-sdk/stream/aggregates_vwap_v1;aggregates_vwap_v1\252\002 KaikoSdk.Stream.AggregatesVWAPV1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,sdk/stream/aggregates_vwap_v1/response.proto\x12\x08kaikosdk\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc1\x01\n\x1eStreamAggregatesVWAPResponseV1\x12\x11\n\taggregate\x18\x01 \x01(\t\x12\r\n\x05\x63lass\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x10\n\x08\x65xchange\x18\x04 \x01(\t\x12\x13\n\x0bsequence_id\x18\x05 \x01(\t\x12\r\n\x05price\x18\x06 \x01(\x01\x12,\n\x08ts_event\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03uid\x18\x08 \x01(\tB\x9e\x01\n\'com.kaiko.sdk.stream.aggregates_vwap_v1P\x01ZNgithub.com/kaikodata/kaiko-go-sdk/stream/aggregates_vwap_v1;aggregates_vwap_v1\xaa\x02 KaikoSdk.Stream.AggregatesVWAPV1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_STREAMAGGREGATESVWAPRESPONSEV1 = _descriptor.Descriptor(
  name='StreamAggregatesVWAPResponseV1',
  full_name='kaikosdk.StreamAggregatesVWAPResponseV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='aggregate', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.aggregate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.class', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.exchange', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_id', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.sequence_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.price', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts_event', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.ts_event', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='kaikosdk.StreamAggregatesVWAPResponseV1.uid', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=92,
  serialized_end=285,
)

_STREAMAGGREGATESVWAPRESPONSEV1.fields_by_name['ts_event'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['StreamAggregatesVWAPResponseV1'] = _STREAMAGGREGATESVWAPRESPONSEV1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamAggregatesVWAPResponseV1 = _reflection.GeneratedProtocolMessageType('StreamAggregatesVWAPResponseV1', (_message.Message,), {
  'DESCRIPTOR' : _STREAMAGGREGATESVWAPRESPONSEV1,
  '__module__' : 'sdk.stream.aggregates_vwap_v1.response_pb2'
  # @@protoc_insertion_point(class_scope:kaikosdk.StreamAggregatesVWAPResponseV1)
  })
_sym_db.RegisterMessage(StreamAggregatesVWAPResponseV1)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
