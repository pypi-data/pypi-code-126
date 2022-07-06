# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serve.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import job_pb2 as job__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bserve.proto\x12\x06\x64\x65ploy\x1a\tjob.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfa\x01\n\x07Serving\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\tauth_info\x18\x03 \x01(\x0b\x32\x11.jobs.NBXAuthInfo\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x04type\x18\x05 \x01(\x0e\x32\x1e.deploy.Serving.DeploymentType\x12 \n\x08resource\x18\x06 \x01(\x0b\x32\x0e.jobs.Resource\"/\n\x0e\x44\x65ploymentType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0cNBOX_SERVING\x10\x01\x42\x34Z2github.com/NimbleBoxAI/jobs-architecture/deploy_pbb\x06proto3')



_SERVING = DESCRIPTOR.message_types_by_name['Serving']
_SERVING_DEPLOYMENTTYPE = _SERVING.enum_types_by_name['DeploymentType']
Serving = _reflection.GeneratedProtocolMessageType('Serving', (_message.Message,), {
  'DESCRIPTOR' : _SERVING,
  '__module__' : 'serve_pb2'
  # @@protoc_insertion_point(class_scope:deploy.Serving)
  })
_sym_db.RegisterMessage(Serving)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/NimbleBoxAI/jobs-architecture/deploy_pb'
  _SERVING._serialized_start=68
  _SERVING._serialized_end=318
  _SERVING_DEPLOYMENTTYPE._serialized_start=271
  _SERVING_DEPLOYMENTTYPE._serialized_end=318
# @@protoc_insertion_point(module_scope)
