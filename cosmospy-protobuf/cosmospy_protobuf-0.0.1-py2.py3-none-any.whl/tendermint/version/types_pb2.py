
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etendermint/version/types.proto\x12\x12tendermint.version\x1a\x14gogoproto/gogo.proto")\n\x03App\x12\x10\n\x08protocol\x18\x01 \x01(\x04\x12\x10\n\x08software\x18\x02 \x01(\t"-\n\tConsensus\x12\r\n\x05block\x18\x01 \x01(\x04\x12\x0b\n\x03app\x18\x02 \x01(\x04:\x04\xe8\xa0\x1f\x01B;Z9github.com/tendermint/tendermint/proto/tendermint/versionb\x06proto3')
_APP = DESCRIPTOR.message_types_by_name['App']
_CONSENSUS = DESCRIPTOR.message_types_by_name['Consensus']
App = _reflection.GeneratedProtocolMessageType('App', (_message.Message,), {'DESCRIPTOR': _APP, '__module__': 'tendermint.version.types_pb2'})
_sym_db.RegisterMessage(App)
Consensus = _reflection.GeneratedProtocolMessageType('Consensus', (_message.Message,), {'DESCRIPTOR': _CONSENSUS, '__module__': 'tendermint.version.types_pb2'})
_sym_db.RegisterMessage(Consensus)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/tendermint/tendermint/proto/tendermint/version'
    _CONSENSUS._options = None
    _CONSENSUS._serialized_options = b'\xe8\xa0\x1f\x01'
    _APP._serialized_start = 76
    _APP._serialized_end = 117
    _CONSENSUS._serialized_start = 119
    _CONSENSUS._serialized_end = 164
