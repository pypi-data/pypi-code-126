
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/base/store/v1beta1/listening.proto\x12\x19cosmos.base.store.v1beta1"L\n\x0bStoreKVPair\x12\x11\n\tstore_key\x18\x01 \x01(\t\x12\x0e\n\x06delete\x18\x02 \x01(\x08\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\r\n\x05value\x18\x04 \x01(\x0cB*Z(github.com/cosmos/cosmos-sdk/store/typesb\x06proto3')
_STOREKVPAIR = DESCRIPTOR.message_types_by_name['StoreKVPair']
StoreKVPair = _reflection.GeneratedProtocolMessageType('StoreKVPair', (_message.Message,), {'DESCRIPTOR': _STOREKVPAIR, '__module__': 'cosmos.base.store.v1beta1.listening_pb2'})
_sym_db.RegisterMessage(StoreKVPair)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/store/types'
    _STOREKVPAIR._serialized_start = 72
    _STOREKVPAIR._serialized_end = 148
