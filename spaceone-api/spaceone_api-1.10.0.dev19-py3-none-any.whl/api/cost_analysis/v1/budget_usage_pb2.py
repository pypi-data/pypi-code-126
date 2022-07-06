# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/cost_analysis/v1/budget_usage.proto
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
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0spaceone/api/cost_analysis/v1/budget_usage.proto\x12\x1dspaceone.api.cost_analysis.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\x80\x01\n\x10\x42udgetUsageQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x11\n\tbudget_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\xb5\x01\n\x0f\x42udgetUsageInfo\x12\x11\n\tbudget_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x10\n\x08usd_cost\x18\x05 \x01(\x02\x12\r\n\x05limit\x18\x06 \x01(\x02\x12+\n\ncost_types\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x0b \x01(\t\x12\x12\n\nupdated_at\x18\x15 \x01(\t\"h\n\x10\x42udgetUsagesInfo\x12?\n\x07results\x18\x01 \x03(\x0b\x32..spaceone.api.cost_analysis.v1.BudgetUsageInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"_\n\x14\x42udgetUsageStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xf1\x02\n\x0b\x42udgetUsage\x12\xd1\x01\n\x04list\x12/.spaceone.api.cost_analysis.v1.BudgetUsageQuery\x1a/.spaceone.api.cost_analysis.v1.BudgetUsagesInfo\"g\x82\xd3\xe4\x93\x02\x61\x12*/cost-analysis/v1/budget/{budget_id}/usageZ3\"1/cost-analysis/v1/budget/{budget_id}/usage/search\x12\x8d\x01\n\x04stat\x12\x33.spaceone.api.cost_analysis.v1.BudgetUsageStatQuery\x1a\x17.google.protobuf.Struct\"7\x82\xd3\xe4\x93\x02\x31\"//cost-analysis/v1/budget/{budget_id}/usage/statb\x06proto3')



_BUDGETUSAGEQUERY = DESCRIPTOR.message_types_by_name['BudgetUsageQuery']
_BUDGETUSAGEINFO = DESCRIPTOR.message_types_by_name['BudgetUsageInfo']
_BUDGETUSAGESINFO = DESCRIPTOR.message_types_by_name['BudgetUsagesInfo']
_BUDGETUSAGESTATQUERY = DESCRIPTOR.message_types_by_name['BudgetUsageStatQuery']
BudgetUsageQuery = _reflection.GeneratedProtocolMessageType('BudgetUsageQuery', (_message.Message,), {
  'DESCRIPTOR' : _BUDGETUSAGEQUERY,
  '__module__' : 'spaceone.api.cost_analysis.v1.budget_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_analysis.v1.BudgetUsageQuery)
  })
_sym_db.RegisterMessage(BudgetUsageQuery)

BudgetUsageInfo = _reflection.GeneratedProtocolMessageType('BudgetUsageInfo', (_message.Message,), {
  'DESCRIPTOR' : _BUDGETUSAGEINFO,
  '__module__' : 'spaceone.api.cost_analysis.v1.budget_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_analysis.v1.BudgetUsageInfo)
  })
_sym_db.RegisterMessage(BudgetUsageInfo)

BudgetUsagesInfo = _reflection.GeneratedProtocolMessageType('BudgetUsagesInfo', (_message.Message,), {
  'DESCRIPTOR' : _BUDGETUSAGESINFO,
  '__module__' : 'spaceone.api.cost_analysis.v1.budget_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_analysis.v1.BudgetUsagesInfo)
  })
_sym_db.RegisterMessage(BudgetUsagesInfo)

BudgetUsageStatQuery = _reflection.GeneratedProtocolMessageType('BudgetUsageStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _BUDGETUSAGESTATQUERY,
  '__module__' : 'spaceone.api.cost_analysis.v1.budget_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_analysis.v1.BudgetUsageStatQuery)
  })
_sym_db.RegisterMessage(BudgetUsageStatQuery)

_BUDGETUSAGE = DESCRIPTOR.services_by_name['BudgetUsage']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUDGETUSAGE.methods_by_name['list']._options = None
  _BUDGETUSAGE.methods_by_name['list']._serialized_options = b'\202\323\344\223\002a\022*/cost-analysis/v1/budget/{budget_id}/usageZ3\"1/cost-analysis/v1/budget/{budget_id}/usage/search'
  _BUDGETUSAGE.methods_by_name['stat']._options = None
  _BUDGETUSAGE.methods_by_name['stat']._serialized_options = b'\202\323\344\223\0021\"//cost-analysis/v1/budget/{budget_id}/usage/stat'
  _BUDGETUSAGEQUERY._serialized_start=178
  _BUDGETUSAGEQUERY._serialized_end=306
  _BUDGETUSAGEINFO._serialized_start=309
  _BUDGETUSAGEINFO._serialized_end=490
  _BUDGETUSAGESINFO._serialized_start=492
  _BUDGETUSAGESINFO._serialized_end=596
  _BUDGETUSAGESTATQUERY._serialized_start=598
  _BUDGETUSAGESTATQUERY._serialized_end=693
  _BUDGETUSAGE._serialized_start=696
  _BUDGETUSAGE._serialized_end=1065
# @@protoc_insertion_point(module_scope)
