
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+ibc/applications/transfer/v1/transfer.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto".\n\nDenomTrace\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x12\n\nbase_denom\x18\x02 \x01(\t"l\n\x06Params\x12-\n\x0csend_enabled\x18\x01 \x01(\x08B\x17\xf2\xde\x1f\x13yaml:"send_enabled"\x123\n\x0freceive_enabled\x18\x02 \x01(\x08B\x1a\xf2\xde\x1f\x16yaml:"receive_enabled"B9Z7github.com/cosmos/ibc-go/v3/modules/apps/transfer/typesb\x06proto3')
_DENOMTRACE = DESCRIPTOR.message_types_by_name['DenomTrace']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
DenomTrace = _reflection.GeneratedProtocolMessageType('DenomTrace', (_message.Message,), {'DESCRIPTOR': _DENOMTRACE, '__module__': 'ibc.applications.transfer.v1.transfer_pb2'})
_sym_db.RegisterMessage(DenomTrace)
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'ibc.applications.transfer.v1.transfer_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v3/modules/apps/transfer/types'
    _PARAMS.fields_by_name['send_enabled']._options = None
    _PARAMS.fields_by_name['send_enabled']._serialized_options = b'\xf2\xde\x1f\x13yaml:"send_enabled"'
    _PARAMS.fields_by_name['receive_enabled']._options = None
    _PARAMS.fields_by_name['receive_enabled']._serialized_options = b'\xf2\xde\x1f\x16yaml:"receive_enabled"'
    _DENOMTRACE._serialized_start = 99
    _DENOMTRACE._serialized_end = 145
    _PARAMS._serialized_start = 147
    _PARAMS._serialized_end = 255
