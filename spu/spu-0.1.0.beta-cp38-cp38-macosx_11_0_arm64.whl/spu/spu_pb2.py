# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spu/spu.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rspu/spu.proto\x12\x03spu\"\x1a\n\nShapeProto\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x03\"\x9a\x01\n\nValueProto\x12 \n\tdata_type\x18\x01 \x01(\x0e\x32\r.spu.DataType\x12#\n\nvisibility\x18\x02 \x01(\x0e\x32\x0f.spu.Visibility\x12\x1e\n\x05shape\x18\x03 \x01(\x0b\x32\x0f.spu.ShapeProto\x12\x14\n\x0cstorage_type\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\x0c\"\xe6\x06\n\rRuntimeConfig\x12#\n\x08protocol\x18\x01 \x01(\x0e\x32\x11.spu.ProtocolKind\x12\x1d\n\x05\x66ield\x18\x02 \x01(\x0e\x32\x0e.spu.FieldType\x12\x19\n\x11\x66xp_fraction_bits\x18\x03 \x01(\x03\x12\x1b\n\x13\x65nable_action_trace\x18\n \x01(\x08\x12\x1b\n\x13\x65nable_type_checker\x18\x0b \x01(\x08\x12\x1a\n\x12\x65nable_pphlo_trace\x18\x0c \x01(\x08\x12\x1d\n\x15\x65nable_processor_dump\x18\r \x01(\x08\x12\x1a\n\x12processor_dump_dir\x18\x0e \x01(\t\x12\x1c\n\x14\x65nable_pphlo_profile\x18\x0f \x01(\x08\x12\x1a\n\x12\x65nable_hal_profile\x18\x10 \x01(\x08\x12\x1f\n\x17reveal_secret_condition\x18\x11 \x01(\x08\x12\x1e\n\x16reveal_secret_indicies\x18\x12 \x01(\x08\x12\x1a\n\x12public_random_seed\x18\x13 \x01(\x04\x12!\n\x19\x66xp_div_goldschmidt_iters\x18\x32 \x01(\x03\x12\x30\n\x0c\x66xp_exp_mode\x18\x33 \x01(\x0e\x32\x1a.spu.RuntimeConfig.ExpMode\x12\x15\n\rfxp_exp_iters\x18\x34 \x01(\x03\x12\x30\n\x0c\x66xp_log_mode\x18\x35 \x01(\x0e\x32\x1a.spu.RuntimeConfig.LogMode\x12\x15\n\rfxp_log_iters\x18\x36 \x01(\x03\x12\x16\n\x0e\x66xp_log_orders\x18\x37 \x01(\x03\x12\x34\n\x0csigmoid_mode\x18\x38 \x01(\x0e\x32\x1e.spu.RuntimeConfig.SigmoidMode\"8\n\x07\x45xpMode\x12\x0f\n\x0b\x45XP_DEFAULT\x10\x00\x12\x0c\n\x08\x45XP_PADE\x10\x01\x12\x0e\n\nEXP_TAYLOR\x10\x02\"8\n\x07LogMode\x12\x0f\n\x0bLOG_DEFAULT\x10\x00\x12\x0c\n\x08LOG_PADE\x10\x01\x12\x0e\n\nLOG_NEWTON\x10\x02\"W\n\x0bSigmoidMode\x12\x13\n\x0fSIGMOID_DEFAULT\x10\x00\x12\x0f\n\x0bSIGMOID_MM1\x10\x01\x12\x10\n\x0cSIGMOID_SEG3\x10\x02\x12\x10\n\x0cSIGMOID_REAL\x10\x03\"*\n\x07XlaMeta\x12\x1f\n\x06inputs\x18\x01 \x03(\x0e\x32\x0f.spu.Visibility\"Q\n\x07IrProto\x12\x1c\n\x07ir_type\x18\x01 \x01(\x0e\x32\x0b.spu.IrType\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x0c\x12\x1a\n\x04meta\x18\x03 \x01(\x0b\x32\x0c.spu.XlaMeta\"X\n\x0f\x45xecutableProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0binput_names\x18\x02 \x03(\t\x12\x14\n\x0coutput_names\x18\x04 \x03(\t\x12\x0c\n\x04\x63ode\x18\x06 \x01(\x0c*\x8f\x01\n\x08\x44\x61taType\x12\x0e\n\nDT_INVALID\x10\x00\x12\t\n\x05\x44T_I1\x10\x01\x12\t\n\x05\x44T_I8\x10\x02\x12\t\n\x05\x44T_U8\x10\x03\x12\n\n\x06\x44T_I16\x10\x04\x12\n\n\x06\x44T_U16\x10\x05\x12\n\n\x06\x44T_I32\x10\x06\x12\n\n\x06\x44T_U32\x10\x07\x12\n\n\x06\x44T_I64\x10\x08\x12\n\n\x06\x44T_U64\x10\t\x12\n\n\x06\x44T_FXP\x10\n*=\n\nVisibility\x12\x0f\n\x0bVIS_INVALID\x10\x00\x12\x0e\n\nVIS_SECRET\x10\x01\x12\x0e\n\nVIS_PUBLIC\x10\x02*\xb5\x01\n\x06PtType\x12\x0e\n\nPT_INVALID\x10\x00\x12\t\n\x05PT_I8\x10\x01\x12\t\n\x05PT_U8\x10\x02\x12\n\n\x06PT_I16\x10\x03\x12\n\n\x06PT_U16\x10\x04\x12\n\n\x06PT_I32\x10\x05\x12\n\n\x06PT_U32\x10\x06\x12\n\n\x06PT_I64\x10\x07\x12\n\n\x06PT_U64\x10\x08\x12\n\n\x06PT_F32\x10\t\x12\n\n\x06PT_F64\x10\n\x12\x0b\n\x07PT_I128\x10\x0b\x12\x0b\n\x07PT_U128\x10\x0c\x12\x0b\n\x07PT_BOOL\x10\r*:\n\tFieldType\x12\x0e\n\nFT_INVALID\x10\x00\x12\x08\n\x04\x46M32\x10\x01\x12\x08\n\x04\x46M64\x10\x02\x12\t\n\x05\x46M128\x10\x03*N\n\x0cProtocolKind\x12\x10\n\x0cPROT_INVALID\x10\x00\x12\t\n\x05REF2K\x10\x01\x12\n\n\x06SEMI2K\x10\x02\x12\x08\n\x04\x41\x42Y3\x10\x03\x12\x0b\n\x07\x43HEETAH\x10\x04*9\n\x06IrType\x12\x0e\n\nIR_INVALID\x10\x00\x12\x0e\n\nIR_XLA_HLO\x10\x01\x12\x0f\n\x0bIR_MLIR_SPU\x10\x02\x62\x06proto3')

_DATATYPE = DESCRIPTOR.enum_types_by_name['DataType']
DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_VISIBILITY = DESCRIPTOR.enum_types_by_name['Visibility']
Visibility = enum_type_wrapper.EnumTypeWrapper(_VISIBILITY)
_PTTYPE = DESCRIPTOR.enum_types_by_name['PtType']
PtType = enum_type_wrapper.EnumTypeWrapper(_PTTYPE)
_FIELDTYPE = DESCRIPTOR.enum_types_by_name['FieldType']
FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
_PROTOCOLKIND = DESCRIPTOR.enum_types_by_name['ProtocolKind']
ProtocolKind = enum_type_wrapper.EnumTypeWrapper(_PROTOCOLKIND)
_IRTYPE = DESCRIPTOR.enum_types_by_name['IrType']
IrType = enum_type_wrapper.EnumTypeWrapper(_IRTYPE)
DT_INVALID = 0
DT_I1 = 1
DT_I8 = 2
DT_U8 = 3
DT_I16 = 4
DT_U16 = 5
DT_I32 = 6
DT_U32 = 7
DT_I64 = 8
DT_U64 = 9
DT_FXP = 10
VIS_INVALID = 0
VIS_SECRET = 1
VIS_PUBLIC = 2
PT_INVALID = 0
PT_I8 = 1
PT_U8 = 2
PT_I16 = 3
PT_U16 = 4
PT_I32 = 5
PT_U32 = 6
PT_I64 = 7
PT_U64 = 8
PT_F32 = 9
PT_F64 = 10
PT_I128 = 11
PT_U128 = 12
PT_BOOL = 13
FT_INVALID = 0
FM32 = 1
FM64 = 2
FM128 = 3
PROT_INVALID = 0
REF2K = 1
SEMI2K = 2
ABY3 = 3
CHEETAH = 4
IR_INVALID = 0
IR_XLA_HLO = 1
IR_MLIR_SPU = 2


_SHAPEPROTO = DESCRIPTOR.message_types_by_name['ShapeProto']
_VALUEPROTO = DESCRIPTOR.message_types_by_name['ValueProto']
_RUNTIMECONFIG = DESCRIPTOR.message_types_by_name['RuntimeConfig']
_XLAMETA = DESCRIPTOR.message_types_by_name['XlaMeta']
_IRPROTO = DESCRIPTOR.message_types_by_name['IrProto']
_EXECUTABLEPROTO = DESCRIPTOR.message_types_by_name['ExecutableProto']
_RUNTIMECONFIG_EXPMODE = _RUNTIMECONFIG.enum_types_by_name['ExpMode']
_RUNTIMECONFIG_LOGMODE = _RUNTIMECONFIG.enum_types_by_name['LogMode']
_RUNTIMECONFIG_SIGMOIDMODE = _RUNTIMECONFIG.enum_types_by_name['SigmoidMode']
ShapeProto = _reflection.GeneratedProtocolMessageType('ShapeProto', (_message.Message,), {
  'DESCRIPTOR' : _SHAPEPROTO,
  '__module__' : 'spu.spu_pb2'
  # @@protoc_insertion_point(class_scope:spu.ShapeProto)
  })
_sym_db.RegisterMessage(ShapeProto)

ValueProto = _reflection.GeneratedProtocolMessageType('ValueProto', (_message.Message,), {
  'DESCRIPTOR' : _VALUEPROTO,
  '__module__' : 'spu.spu_pb2'
  # @@protoc_insertion_point(class_scope:spu.ValueProto)
  })
_sym_db.RegisterMessage(ValueProto)

RuntimeConfig = _reflection.GeneratedProtocolMessageType('RuntimeConfig', (_message.Message,), {
  'DESCRIPTOR' : _RUNTIMECONFIG,
  '__module__' : 'spu.spu_pb2'
  # @@protoc_insertion_point(class_scope:spu.RuntimeConfig)
  })
_sym_db.RegisterMessage(RuntimeConfig)

XlaMeta = _reflection.GeneratedProtocolMessageType('XlaMeta', (_message.Message,), {
  'DESCRIPTOR' : _XLAMETA,
  '__module__' : 'spu.spu_pb2'
  # @@protoc_insertion_point(class_scope:spu.XlaMeta)
  })
_sym_db.RegisterMessage(XlaMeta)

IrProto = _reflection.GeneratedProtocolMessageType('IrProto', (_message.Message,), {
  'DESCRIPTOR' : _IRPROTO,
  '__module__' : 'spu.spu_pb2'
  # @@protoc_insertion_point(class_scope:spu.IrProto)
  })
_sym_db.RegisterMessage(IrProto)

ExecutableProto = _reflection.GeneratedProtocolMessageType('ExecutableProto', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTABLEPROTO,
  '__module__' : 'spu.spu_pb2'
  # @@protoc_insertion_point(class_scope:spu.ExecutableProto)
  })
_sym_db.RegisterMessage(ExecutableProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATATYPE._serialized_start=1298
  _DATATYPE._serialized_end=1441
  _VISIBILITY._serialized_start=1443
  _VISIBILITY._serialized_end=1504
  _PTTYPE._serialized_start=1507
  _PTTYPE._serialized_end=1688
  _FIELDTYPE._serialized_start=1690
  _FIELDTYPE._serialized_end=1748
  _PROTOCOLKIND._serialized_start=1750
  _PROTOCOLKIND._serialized_end=1828
  _IRTYPE._serialized_start=1830
  _IRTYPE._serialized_end=1887
  _SHAPEPROTO._serialized_start=22
  _SHAPEPROTO._serialized_end=48
  _VALUEPROTO._serialized_start=51
  _VALUEPROTO._serialized_end=205
  _RUNTIMECONFIG._serialized_start=208
  _RUNTIMECONFIG._serialized_end=1078
  _RUNTIMECONFIG_EXPMODE._serialized_start=875
  _RUNTIMECONFIG_EXPMODE._serialized_end=931
  _RUNTIMECONFIG_LOGMODE._serialized_start=933
  _RUNTIMECONFIG_LOGMODE._serialized_end=989
  _RUNTIMECONFIG_SIGMOIDMODE._serialized_start=991
  _RUNTIMECONFIG_SIGMOIDMODE._serialized_end=1078
  _XLAMETA._serialized_start=1080
  _XLAMETA._serialized_end=1122
  _IRPROTO._serialized_start=1124
  _IRPROTO._serialized_end=1205
  _EXECUTABLEPROTO._serialized_start=1207
  _EXECUTABLEPROTO._serialized_end=1295
# @@protoc_insertion_point(module_scope)
