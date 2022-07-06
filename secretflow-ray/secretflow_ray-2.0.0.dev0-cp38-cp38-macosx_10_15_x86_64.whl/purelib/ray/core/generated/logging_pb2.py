# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/logging.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/ray/protobuf/logging.proto',
  package='ray.rpc',
  syntax='proto3',
  serialized_options=b'\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1esrc/ray/protobuf/logging.proto\x12\x07ray.rpc\"\xb0\x01\n\x08LogBatch\x12\x0e\n\x02ip\x18\x01 \x01(\tR\x02ip\x12\x10\n\x03pid\x18\x02 \x01(\tR\x03pid\x12\x15\n\x06job_id\x18\x03 \x01(\tR\x05jobId\x12\x19\n\x08is_error\x18\x04 \x01(\x08R\x07isError\x12\x14\n\x05lines\x18\x05 \x03(\tR\x05lines\x12\x1d\n\nactor_name\x18\x06 \x01(\tR\tactorName\x12\x1b\n\ttask_name\x18\x07 \x01(\tR\x08taskNameB\x03\xf8\x01\x01\x62\x06proto3'
)




_LOGBATCH = _descriptor.Descriptor(
  name='LogBatch',
  full_name='ray.rpc.LogBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='ray.rpc.LogBatch.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ip', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='ray.rpc.LogBatch.pid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pid', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='ray.rpc.LogBatch.job_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='jobId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_error', full_name='ray.rpc.LogBatch.is_error', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='isError', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lines', full_name='ray.rpc.LogBatch.lines', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='lines', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actor_name', full_name='ray.rpc.LogBatch.actor_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='actorName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_name', full_name='ray.rpc.LogBatch.task_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='taskName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=44,
  serialized_end=220,
)

DESCRIPTOR.message_types_by_name['LogBatch'] = _LOGBATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogBatch = _reflection.GeneratedProtocolMessageType('LogBatch', (_message.Message,), {
  'DESCRIPTOR' : _LOGBATCH,
  '__module__' : 'src.ray.protobuf.logging_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.LogBatch)
  })
_sym_db.RegisterMessage(LogBatch)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
