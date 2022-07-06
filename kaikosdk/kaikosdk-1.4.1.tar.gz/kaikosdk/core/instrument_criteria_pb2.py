# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk/core/instrument_criteria.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk/core/instrument_criteria.proto',
  package='kaikosdk',
  syntax='proto3',
  serialized_options=b'\n\022com.kaiko.sdk.coreP\001Z+github.com/kaikodata/kaiko-go-sdk/core;core\252\002\rKaikoSdk.Core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"sdk/core/instrument_criteria.proto\x12\x08kaikosdk\"N\n\x12InstrumentCriteria\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x18\n\x10instrument_class\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\tBS\n\x12\x63om.kaiko.sdk.coreP\x01Z+github.com/kaikodata/kaiko-go-sdk/core;core\xaa\x02\rKaikoSdk.Coreb\x06proto3'
)




_INSTRUMENTCRITERIA = _descriptor.Descriptor(
  name='InstrumentCriteria',
  full_name='kaikosdk.InstrumentCriteria',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange', full_name='kaikosdk.InstrumentCriteria.exchange', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instrument_class', full_name='kaikosdk.InstrumentCriteria.instrument_class', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='kaikosdk.InstrumentCriteria.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['InstrumentCriteria'] = _INSTRUMENTCRITERIA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstrumentCriteria = _reflection.GeneratedProtocolMessageType('InstrumentCriteria', (_message.Message,), {
  'DESCRIPTOR' : _INSTRUMENTCRITERIA,
  '__module__' : 'sdk.core.instrument_criteria_pb2'
  # @@protoc_insertion_point(class_scope:kaikosdk.InstrumentCriteria)
  })
_sym_db.RegisterMessage(InstrumentCriteria)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
