# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/tf2xla/tf2xla.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/compiler/tf2xla/tf2xla.proto',
  package='tensorflow.tf2xla',
  syntax='proto3',
  serialized_options=_b('\n\025org.tensorflow.tf2xlaB\014Tf2XlaProtosP\001\370\001\001'),
  serialized_pb=_b('\n\'tensorflow/compiler/tf2xla/tf2xla.proto\x12\x11tensorflow.tf2xla\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"3\n\x08TensorId\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x14\n\x0coutput_index\x18\x02 \x01(\x03\"\x8e\x01\n\x04\x46\x65\x65\x64\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.tensorflow.tf2xla.TensorId\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.tensorflow.DataType\"\x8f\x01\n\x05\x46\x65tch\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.tensorflow.tf2xla.TensorId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.tensorflow.DataType\"\x8e\x01\n\x08Variable\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x10\n\x08readonly\x18\x05 \x01(\x08\"\x87\x01\n\x06\x43onfig\x12%\n\x04\x66\x65\x65\x64\x18\x01 \x03(\x0b\x32\x17.tensorflow.tf2xla.Feed\x12\'\n\x05\x66\x65tch\x18\x02 \x03(\x0b\x32\x18.tensorflow.tf2xla.Fetch\x12-\n\x08variable\x18\x03 \x03(\x0b\x32\x1b.tensorflow.tf2xla.VariableB*\n\x15org.tensorflow.tf2xlaB\x0cTf2XlaProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_TENSORID = _descriptor.Descriptor(
  name='TensorId',
  full_name='tensorflow.tf2xla.TensorId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='tensorflow.tf2xla.TensorId.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_index', full_name='tensorflow.tf2xla.TensorId.output_index', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=147,
  serialized_end=198,
)


_FEED = _descriptor.Descriptor(
  name='Feed',
  full_name='tensorflow.tf2xla.Feed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.tf2xla.Feed.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.tf2xla.Feed.shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.tf2xla.Feed.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.tf2xla.Feed.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=201,
  serialized_end=343,
)


_FETCH = _descriptor.Descriptor(
  name='Fetch',
  full_name='tensorflow.tf2xla.Fetch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.tf2xla.Fetch.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.tf2xla.Fetch.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.tf2xla.Fetch.shape', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.tf2xla.Fetch.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=346,
  serialized_end=489,
)


_VARIABLE = _descriptor.Descriptor(
  name='Variable',
  full_name='tensorflow.tf2xla.Variable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='tensorflow.tf2xla.Variable.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.tf2xla.Variable.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.tf2xla.Variable.shape', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.tf2xla.Variable.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='tensorflow.tf2xla.Variable.readonly', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=492,
  serialized_end=634,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='tensorflow.tf2xla.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feed', full_name='tensorflow.tf2xla.Config.feed', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fetch', full_name='tensorflow.tf2xla.Config.fetch', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variable', full_name='tensorflow.tf2xla.Config.variable', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=637,
  serialized_end=772,
)

_FEED.fields_by_name['id'].message_type = _TENSORID
_FEED.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_FEED.fields_by_name['type'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_FETCH.fields_by_name['id'].message_type = _TENSORID
_FETCH.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_FETCH.fields_by_name['type'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_VARIABLE.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_VARIABLE.fields_by_name['type'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_CONFIG.fields_by_name['feed'].message_type = _FEED
_CONFIG.fields_by_name['fetch'].message_type = _FETCH
_CONFIG.fields_by_name['variable'].message_type = _VARIABLE
DESCRIPTOR.message_types_by_name['TensorId'] = _TENSORID
DESCRIPTOR.message_types_by_name['Feed'] = _FEED
DESCRIPTOR.message_types_by_name['Fetch'] = _FETCH
DESCRIPTOR.message_types_by_name['Variable'] = _VARIABLE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorId = _reflection.GeneratedProtocolMessageType('TensorId', (_message.Message,), {
  'DESCRIPTOR' : _TENSORID,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.TensorId)
  })
_sym_db.RegisterMessage(TensorId)

Feed = _reflection.GeneratedProtocolMessageType('Feed', (_message.Message,), {
  'DESCRIPTOR' : _FEED,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Feed)
  })
_sym_db.RegisterMessage(Feed)

Fetch = _reflection.GeneratedProtocolMessageType('Fetch', (_message.Message,), {
  'DESCRIPTOR' : _FETCH,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Fetch)
  })
_sym_db.RegisterMessage(Fetch)

Variable = _reflection.GeneratedProtocolMessageType('Variable', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLE,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Variable)
  })
_sym_db.RegisterMessage(Variable)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
