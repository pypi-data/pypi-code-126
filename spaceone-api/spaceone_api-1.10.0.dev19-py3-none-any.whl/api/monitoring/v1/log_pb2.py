# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/monitoring/v1/log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$spaceone/api/monitoring/v1/log.proto\x12\x1aspaceone.api.monitoring.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\"\xaf\x01\n\nLogRequest\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12\x0f\n\x07keyword\x18\x03 \x01(\t\x12\r\n\x05start\x18\n \x01(\t\x12\x0b\n\x03\x65nd\x18\x0b \x01(\t\x12%\n\x04sort\x18\x0f \x01(\x0b\x32\x17.google.protobuf.Struct\x12\r\n\x05limit\x18\x10 \x01(\x05\x12\x11\n\tdomain_id\x18\x14 \x01(\t\"J\n\x0bLogDataInfo\x12(\n\x04logs\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\x99\x01\n\x03Log\x12\x91\x01\n\x04list\x12&.spaceone.api.monitoring.v1.LogRequest\x1a\'.spaceone.api.monitoring.v1.LogDataInfo\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/monitoring/v1/data-source/{data_source_id}/logsb\x06proto3')



_LOGREQUEST = DESCRIPTOR.message_types_by_name['LogRequest']
_LOGDATAINFO = DESCRIPTOR.message_types_by_name['LogDataInfo']
LogRequest = _reflection.GeneratedProtocolMessageType('LogRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGREQUEST,
  '__module__' : 'spaceone.api.monitoring.v1.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.v1.LogRequest)
  })
_sym_db.RegisterMessage(LogRequest)

LogDataInfo = _reflection.GeneratedProtocolMessageType('LogDataInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOGDATAINFO,
  '__module__' : 'spaceone.api.monitoring.v1.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.v1.LogDataInfo)
  })
_sym_db.RegisterMessage(LogDataInfo)

_LOG = DESCRIPTOR.services_by_name['Log']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOG.methods_by_name['list']._options = None
  _LOG.methods_by_name['list']._serialized_options = b'\202\323\344\223\0022\0220/monitoring/v1/data-source/{data_source_id}/logs'
  _LOGREQUEST._serialized_start=129
  _LOGREQUEST._serialized_end=304
  _LOGDATAINFO._serialized_start=306
  _LOGDATAINFO._serialized_end=380
  _LOG._serialized_start=383
  _LOG._serialized_end=536
# @@protoc_insertion_point(module_scope)
