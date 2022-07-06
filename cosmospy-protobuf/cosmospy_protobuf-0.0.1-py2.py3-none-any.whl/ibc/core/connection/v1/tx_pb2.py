
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from .....ibc.core.connection.v1 import connection_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fibc/core/connection/v1/tx.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/connection/v1/connection.proto"\xfd\x01\n\x15MsgConnectionOpenInit\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12@\n\x0ccounterparty\x18\x02 \x01(\x0b2$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x120\n\x07version\x18\x03 \x01(\x0b2\x1f.ibc.core.connection.v1.Version\x12-\n\x0cdelay_period\x18\x04 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"delay_period"\x12\x0e\n\x06signer\x18\x05 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1f\n\x1dMsgConnectionOpenInitResponse"\xe9\x05\n\x14MsgConnectionOpenTry\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12A\n\x16previous_connection_id\x18\x02 \x01(\tB!\xf2\xde\x1f\x1dyaml:"previous_connection_id"\x12C\n\x0cclient_state\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state"\x12@\n\x0ccounterparty\x18\x04 \x01(\x0b2$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12-\n\x0cdelay_period\x18\x05 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"delay_period"\x12`\n\x15counterparty_versions\x18\x06 \x03(\x0b2\x1f.ibc.core.connection.v1.VersionB \xf2\xde\x1f\x1cyaml:"counterparty_versions"\x12M\n\x0cproof_height\x18\x07 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:"proof_height"\xc8\xde\x1f\x00\x12)\n\nproof_init\x18\x08 \x01(\x0cB\x15\xf2\xde\x1f\x11yaml:"proof_init"\x12-\n\x0cproof_client\x18\t \x01(\x0cB\x17\xf2\xde\x1f\x13yaml:"proof_client"\x123\n\x0fproof_consensus\x18\n \x01(\x0cB\x1a\xf2\xde\x1f\x16yaml:"proof_consensus"\x12U\n\x10consensus_height\x18\x0b \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1f\xf2\xde\x1f\x17yaml:"consensus_height"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x0c \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1e\n\x1cMsgConnectionOpenTryResponse"\xd6\x04\n\x14MsgConnectionOpenAck\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id"\x12I\n\x1acounterparty_connection_id\x18\x02 \x01(\tB%\xf2\xde\x1f!yaml:"counterparty_connection_id"\x120\n\x07version\x18\x03 \x01(\x0b2\x1f.ibc.core.connection.v1.Version\x12C\n\x0cclient_state\x18\x04 \x01(\x0b2\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state"\x12M\n\x0cproof_height\x18\x05 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:"proof_height"\xc8\xde\x1f\x00\x12\'\n\tproof_try\x18\x06 \x01(\x0cB\x14\xf2\xde\x1f\x10yaml:"proof_try"\x12-\n\x0cproof_client\x18\x07 \x01(\x0cB\x17\xf2\xde\x1f\x13yaml:"proof_client"\x123\n\x0fproof_consensus\x18\x08 \x01(\x0cB\x1a\xf2\xde\x1f\x16yaml:"proof_consensus"\x12U\n\x10consensus_height\x18\t \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1f\xf2\xde\x1f\x17yaml:"consensus_height"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\n \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1e\n\x1cMsgConnectionOpenAckResponse"\xdd\x01\n\x18MsgConnectionOpenConfirm\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id"\x12\'\n\tproof_ack\x18\x02 \x01(\x0cB\x14\xf2\xde\x1f\x10yaml:"proof_ack"\x12M\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:"proof_height"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x04 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00""\n MsgConnectionOpenConfirmResponse2\xf9\x03\n\x03Msg\x12z\n\x12ConnectionOpenInit\x12-.ibc.core.connection.v1.MsgConnectionOpenInit\x1a5.ibc.core.connection.v1.MsgConnectionOpenInitResponse\x12w\n\x11ConnectionOpenTry\x12,.ibc.core.connection.v1.MsgConnectionOpenTry\x1a4.ibc.core.connection.v1.MsgConnectionOpenTryResponse\x12w\n\x11ConnectionOpenAck\x12,.ibc.core.connection.v1.MsgConnectionOpenAck\x1a4.ibc.core.connection.v1.MsgConnectionOpenAckResponse\x12\x83\x01\n\x15ConnectionOpenConfirm\x120.ibc.core.connection.v1.MsgConnectionOpenConfirm\x1a8.ibc.core.connection.v1.MsgConnectionOpenConfirmResponseB>Z<github.com/cosmos/ibc-go/v3/modules/core/03-connection/typesb\x06proto3')
_MSGCONNECTIONOPENINIT = DESCRIPTOR.message_types_by_name['MsgConnectionOpenInit']
_MSGCONNECTIONOPENINITRESPONSE = DESCRIPTOR.message_types_by_name['MsgConnectionOpenInitResponse']
_MSGCONNECTIONOPENTRY = DESCRIPTOR.message_types_by_name['MsgConnectionOpenTry']
_MSGCONNECTIONOPENTRYRESPONSE = DESCRIPTOR.message_types_by_name['MsgConnectionOpenTryResponse']
_MSGCONNECTIONOPENACK = DESCRIPTOR.message_types_by_name['MsgConnectionOpenAck']
_MSGCONNECTIONOPENACKRESPONSE = DESCRIPTOR.message_types_by_name['MsgConnectionOpenAckResponse']
_MSGCONNECTIONOPENCONFIRM = DESCRIPTOR.message_types_by_name['MsgConnectionOpenConfirm']
_MSGCONNECTIONOPENCONFIRMRESPONSE = DESCRIPTOR.message_types_by_name['MsgConnectionOpenConfirmResponse']
MsgConnectionOpenInit = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenInit', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENINIT, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenInit)
MsgConnectionOpenInitResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenInitResponse', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENINITRESPONSE, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenInitResponse)
MsgConnectionOpenTry = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenTry', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENTRY, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenTry)
MsgConnectionOpenTryResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenTryResponse', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENTRYRESPONSE, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenTryResponse)
MsgConnectionOpenAck = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenAck', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENACK, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenAck)
MsgConnectionOpenAckResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenAckResponse', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENACKRESPONSE, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenAckResponse)
MsgConnectionOpenConfirm = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenConfirm', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENCONFIRM, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenConfirm)
MsgConnectionOpenConfirmResponse = _reflection.GeneratedProtocolMessageType('MsgConnectionOpenConfirmResponse', (_message.Message,), {'DESCRIPTOR': _MSGCONNECTIONOPENCONFIRMRESPONSE, '__module__': 'ibc.core.connection.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgConnectionOpenConfirmResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/cosmos/ibc-go/v3/modules/core/03-connection/types'
    _MSGCONNECTIONOPENINIT.fields_by_name['client_id']._options = None
    _MSGCONNECTIONOPENINIT.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _MSGCONNECTIONOPENINIT.fields_by_name['counterparty']._options = None
    _MSGCONNECTIONOPENINIT.fields_by_name['counterparty']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCONNECTIONOPENINIT.fields_by_name['delay_period']._options = None
    _MSGCONNECTIONOPENINIT.fields_by_name['delay_period']._serialized_options = b'\xf2\xde\x1f\x13yaml:"delay_period"'
    _MSGCONNECTIONOPENINIT._options = None
    _MSGCONNECTIONOPENINIT._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGCONNECTIONOPENTRY.fields_by_name['client_id']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _MSGCONNECTIONOPENTRY.fields_by_name['previous_connection_id']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['previous_connection_id']._serialized_options = b'\xf2\xde\x1f\x1dyaml:"previous_connection_id"'
    _MSGCONNECTIONOPENTRY.fields_by_name['client_state']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['client_state']._serialized_options = b'\xf2\xde\x1f\x13yaml:"client_state"'
    _MSGCONNECTIONOPENTRY.fields_by_name['counterparty']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['counterparty']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCONNECTIONOPENTRY.fields_by_name['delay_period']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['delay_period']._serialized_options = b'\xf2\xde\x1f\x13yaml:"delay_period"'
    _MSGCONNECTIONOPENTRY.fields_by_name['counterparty_versions']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['counterparty_versions']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"counterparty_versions"'
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_height']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_height']._serialized_options = b'\xf2\xde\x1f\x13yaml:"proof_height"\xc8\xde\x1f\x00'
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_init']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_init']._serialized_options = b'\xf2\xde\x1f\x11yaml:"proof_init"'
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_client']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_client']._serialized_options = b'\xf2\xde\x1f\x13yaml:"proof_client"'
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_consensus']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['proof_consensus']._serialized_options = b'\xf2\xde\x1f\x16yaml:"proof_consensus"'
    _MSGCONNECTIONOPENTRY.fields_by_name['consensus_height']._options = None
    _MSGCONNECTIONOPENTRY.fields_by_name['consensus_height']._serialized_options = b'\xf2\xde\x1f\x17yaml:"consensus_height"\xc8\xde\x1f\x00'
    _MSGCONNECTIONOPENTRY._options = None
    _MSGCONNECTIONOPENTRY._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGCONNECTIONOPENACK.fields_by_name['connection_id']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _MSGCONNECTIONOPENACK.fields_by_name['counterparty_connection_id']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['counterparty_connection_id']._serialized_options = b'\xf2\xde\x1f!yaml:"counterparty_connection_id"'
    _MSGCONNECTIONOPENACK.fields_by_name['client_state']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['client_state']._serialized_options = b'\xf2\xde\x1f\x13yaml:"client_state"'
    _MSGCONNECTIONOPENACK.fields_by_name['proof_height']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['proof_height']._serialized_options = b'\xf2\xde\x1f\x13yaml:"proof_height"\xc8\xde\x1f\x00'
    _MSGCONNECTIONOPENACK.fields_by_name['proof_try']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['proof_try']._serialized_options = b'\xf2\xde\x1f\x10yaml:"proof_try"'
    _MSGCONNECTIONOPENACK.fields_by_name['proof_client']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['proof_client']._serialized_options = b'\xf2\xde\x1f\x13yaml:"proof_client"'
    _MSGCONNECTIONOPENACK.fields_by_name['proof_consensus']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['proof_consensus']._serialized_options = b'\xf2\xde\x1f\x16yaml:"proof_consensus"'
    _MSGCONNECTIONOPENACK.fields_by_name['consensus_height']._options = None
    _MSGCONNECTIONOPENACK.fields_by_name['consensus_height']._serialized_options = b'\xf2\xde\x1f\x17yaml:"consensus_height"\xc8\xde\x1f\x00'
    _MSGCONNECTIONOPENACK._options = None
    _MSGCONNECTIONOPENACK._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGCONNECTIONOPENCONFIRM.fields_by_name['connection_id']._options = None
    _MSGCONNECTIONOPENCONFIRM.fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _MSGCONNECTIONOPENCONFIRM.fields_by_name['proof_ack']._options = None
    _MSGCONNECTIONOPENCONFIRM.fields_by_name['proof_ack']._serialized_options = b'\xf2\xde\x1f\x10yaml:"proof_ack"'
    _MSGCONNECTIONOPENCONFIRM.fields_by_name['proof_height']._options = None
    _MSGCONNECTIONOPENCONFIRM.fields_by_name['proof_height']._serialized_options = b'\xf2\xde\x1f\x13yaml:"proof_height"\xc8\xde\x1f\x00'
    _MSGCONNECTIONOPENCONFIRM._options = None
    _MSGCONNECTIONOPENCONFIRM._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGCONNECTIONOPENINIT._serialized_start = 183
    _MSGCONNECTIONOPENINIT._serialized_end = 436
    _MSGCONNECTIONOPENINITRESPONSE._serialized_start = 438
    _MSGCONNECTIONOPENINITRESPONSE._serialized_end = 469
    _MSGCONNECTIONOPENTRY._serialized_start = 472
    _MSGCONNECTIONOPENTRY._serialized_end = 1217
    _MSGCONNECTIONOPENTRYRESPONSE._serialized_start = 1219
    _MSGCONNECTIONOPENTRYRESPONSE._serialized_end = 1249
    _MSGCONNECTIONOPENACK._serialized_start = 1252
    _MSGCONNECTIONOPENACK._serialized_end = 1850
    _MSGCONNECTIONOPENACKRESPONSE._serialized_start = 1852
    _MSGCONNECTIONOPENACKRESPONSE._serialized_end = 1882
    _MSGCONNECTIONOPENCONFIRM._serialized_start = 1885
    _MSGCONNECTIONOPENCONFIRM._serialized_end = 2106
    _MSGCONNECTIONOPENCONFIRMRESPONSE._serialized_start = 2108
    _MSGCONNECTIONOPENCONFIRMRESPONSE._serialized_end = 2142
    _MSG._serialized_start = 2145
    _MSG._serialized_end = 2650
