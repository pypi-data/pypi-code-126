# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk/core/sort_criteria.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk/core/sort_criteria.proto',
  package='kaikosdk',
  syntax='proto3',
  serialized_options=b'\n\022com.kaiko.sdk.coreP\001Z+github.com/kaikodata/kaiko-go-sdk/core;core\252\002\rKaikoSdk.Core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1csdk/core/sort_criteria.proto\x12\x08kaikosdk*3\n\x0cSortCriteria\x12\x10\n\x0cSORT_UNKNOWN\x10\x00\x12\x07\n\x03\x41SC\x10\x01\x12\x08\n\x04\x44\x45SC\x10\x02\x42S\n\x12\x63om.kaiko.sdk.coreP\x01Z+github.com/kaikodata/kaiko-go-sdk/core;core\xaa\x02\rKaikoSdk.Coreb\x06proto3'
)

_SORTCRITERIA = _descriptor.EnumDescriptor(
  name='SortCriteria',
  full_name='kaikosdk.SortCriteria',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SORT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=42,
  serialized_end=93,
)
_sym_db.RegisterEnumDescriptor(_SORTCRITERIA)

SortCriteria = enum_type_wrapper.EnumTypeWrapper(_SORTCRITERIA)
SORT_UNKNOWN = 0
ASC = 1
DESC = 2


DESCRIPTOR.enum_types_by_name['SortCriteria'] = _SORTCRITERIA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
