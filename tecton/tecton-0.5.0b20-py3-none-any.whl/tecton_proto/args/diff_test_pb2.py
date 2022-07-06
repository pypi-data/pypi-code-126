# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/diff_test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2
from tecton_proto.args import basic_info_pb2 as tecton__proto_dot_args_dot_basic__info__pb2
from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tecton_proto/args/diff_test.proto',
  package='tecton_proto.args',
  syntax='proto2',
  serialized_options=b'\n\017com.tecton.argsP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!tecton_proto/args/diff_test.proto\x12\x11tecton_proto.args\x1a\x1ctecton_proto/common/id.proto\x1a\"tecton_proto/args/basic_info.proto\x1a$tecton_proto/args/diff_options.proto\"?\n\x0b\x44iffTestFoo\x12\x17\n\x07\x66ield_a\x18\x01 \x01(\tR\x06\x66ieldA\x12\x17\n\x07\x66ield_b\x18\x02 \x01(\tR\x06\x66ieldB\"\xf6\x02\n\x0c\x44iffTestArgs\x12\x39\n\x0ctest_args_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\ntestArgsId\x12\x30\n\x04info\x18\x02 \x01(\x0b\x32\x1c.tecton_proto.args.BasicInfoR\x04info\x12\x42\n\tnew_field\x18\x03 \x01(\x0b\x32\x1e.tecton_proto.args.DiffTestFooB\x05\x92M\x02\x08\x03R\x08newField\x12\x42\n\told_field\x18\x04 \x01(\x0b\x32\x1e.tecton_proto.args.DiffTestFooB\x05\x92M\x02\x08\x04R\x08oldField\x12*\n\rpassive_field\x18\x05 \x01(\tB\x05\x92M\x02\x08\x05R\x0cpassiveField\x12\x45\n\x1brecreate_suppressable_field\x18\x06 \x01(\tB\x05\x92M\x02\x08\x06R\x19recreateSuppressableField\"L\n\x0e\x44iffTestNested\x12:\n\x04\x61rgs\x18\x01 \x01(\x0b\x32\x1f.tecton_proto.args.DiffTestArgsB\x05\x92M\x02\x08\x01R\x04\x61rgsB\x13\n\x0f\x63om.tecton.argsP\x01'
  ,
  dependencies=[tecton__proto_dot_common_dot_id__pb2.DESCRIPTOR,tecton__proto_dot_args_dot_basic__info__pb2.DESCRIPTOR,tecton__proto_dot_args_dot_diff__options__pb2.DESCRIPTOR,])




_DIFFTESTFOO = _descriptor.Descriptor(
  name='DiffTestFoo',
  full_name='tecton_proto.args.DiffTestFoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_a', full_name='tecton_proto.args.DiffTestFoo.field_a', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fieldA', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_b', full_name='tecton_proto.args.DiffTestFoo.field_b', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fieldB', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=223,
)


_DIFFTESTARGS = _descriptor.Descriptor(
  name='DiffTestArgs',
  full_name='tecton_proto.args.DiffTestArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_args_id', full_name='tecton_proto.args.DiffTestArgs.test_args_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='testArgsId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='tecton_proto.args.DiffTestArgs.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='info', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_field', full_name='tecton_proto.args.DiffTestArgs.new_field', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222M\002\010\003', json_name='newField', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='old_field', full_name='tecton_proto.args.DiffTestArgs.old_field', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222M\002\010\004', json_name='oldField', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passive_field', full_name='tecton_proto.args.DiffTestArgs.passive_field', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222M\002\010\005', json_name='passiveField', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recreate_suppressable_field', full_name='tecton_proto.args.DiffTestArgs.recreate_suppressable_field', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222M\002\010\006', json_name='recreateSuppressableField', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=600,
)


_DIFFTESTNESTED = _descriptor.Descriptor(
  name='DiffTestNested',
  full_name='tecton_proto.args.DiffTestNested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='args', full_name='tecton_proto.args.DiffTestNested.args', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222M\002\010\001', json_name='args', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=678,
)

_DIFFTESTARGS.fields_by_name['test_args_id'].message_type = tecton__proto_dot_common_dot_id__pb2._ID
_DIFFTESTARGS.fields_by_name['info'].message_type = tecton__proto_dot_args_dot_basic__info__pb2._BASICINFO
_DIFFTESTARGS.fields_by_name['new_field'].message_type = _DIFFTESTFOO
_DIFFTESTARGS.fields_by_name['old_field'].message_type = _DIFFTESTFOO
_DIFFTESTNESTED.fields_by_name['args'].message_type = _DIFFTESTARGS
DESCRIPTOR.message_types_by_name['DiffTestFoo'] = _DIFFTESTFOO
DESCRIPTOR.message_types_by_name['DiffTestArgs'] = _DIFFTESTARGS
DESCRIPTOR.message_types_by_name['DiffTestNested'] = _DIFFTESTNESTED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiffTestFoo = _reflection.GeneratedProtocolMessageType('DiffTestFoo', (_message.Message,), {
  'DESCRIPTOR' : _DIFFTESTFOO,
  '__module__' : 'tecton_proto.args.diff_test_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.args.DiffTestFoo)
  })
_sym_db.RegisterMessage(DiffTestFoo)

DiffTestArgs = _reflection.GeneratedProtocolMessageType('DiffTestArgs', (_message.Message,), {
  'DESCRIPTOR' : _DIFFTESTARGS,
  '__module__' : 'tecton_proto.args.diff_test_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.args.DiffTestArgs)
  })
_sym_db.RegisterMessage(DiffTestArgs)

DiffTestNested = _reflection.GeneratedProtocolMessageType('DiffTestNested', (_message.Message,), {
  'DESCRIPTOR' : _DIFFTESTNESTED,
  '__module__' : 'tecton_proto.args.diff_test_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.args.DiffTestNested)
  })
_sym_db.RegisterMessage(DiffTestNested)


DESCRIPTOR._options = None
_DIFFTESTARGS.fields_by_name['new_field']._options = None
_DIFFTESTARGS.fields_by_name['old_field']._options = None
_DIFFTESTARGS.fields_by_name['passive_field']._options = None
_DIFFTESTARGS.fields_by_name['recreate_suppressable_field']._options = None
_DIFFTESTNESTED.fields_by_name['args']._options = None
# @@protoc_insertion_point(module_scope)
