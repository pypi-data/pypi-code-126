
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...tendermint.crypto import proof_pb2 as tendermint_dot_crypto_dot_proof__pb2
from ...tendermint.version import types_pb2 as tendermint_dot_version_dot_types__pb2
from ...tendermint.types import validator_pb2 as tendermint_dot_types_dot_validator__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ctendermint/types/types.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dtendermint/crypto/proof.proto\x1a\x1etendermint/version/types.proto\x1a tendermint/types/validator.proto",\n\rPartSetHeader\x12\r\n\x05total\x18\x01 \x01(\r\x12\x0c\n\x04hash\x18\x02 \x01(\x0c"S\n\x04Part\x12\r\n\x05index\x18\x01 \x01(\r\x12\r\n\x05bytes\x18\x02 \x01(\x0c\x12-\n\x05proof\x18\x03 \x01(\x0b2\x18.tendermint.crypto.ProofB\x04\xc8\xde\x1f\x00"W\n\x07BlockID\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12>\n\x0fpart_set_header\x18\x02 \x01(\x0b2\x1f.tendermint.types.PartSetHeaderB\x04\xc8\xde\x1f\x00"\xb3\x03\n\x06Header\x124\n\x07version\x18\x01 \x01(\x0b2\x1d.tendermint.version.ConsensusB\x04\xc8\xde\x1f\x00\x12\x1d\n\x08chain_id\x18\x02 \x01(\tB\x0b\xe2\xde\x1f\x07ChainID\x12\x0e\n\x06height\x18\x03 \x01(\x03\x122\n\x04time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x126\n\rlast_block_id\x18\x05 \x01(\x0b2\x19.tendermint.types.BlockIDB\x04\xc8\xde\x1f\x00\x12\x18\n\x10last_commit_hash\x18\x06 \x01(\x0c\x12\x11\n\tdata_hash\x18\x07 \x01(\x0c\x12\x17\n\x0fvalidators_hash\x18\x08 \x01(\x0c\x12\x1c\n\x14next_validators_hash\x18\t \x01(\x0c\x12\x16\n\x0econsensus_hash\x18\n \x01(\x0c\x12\x10\n\x08app_hash\x18\x0b \x01(\x0c\x12\x19\n\x11last_results_hash\x18\x0c \x01(\x0c\x12\x15\n\revidence_hash\x18\r \x01(\x0c\x12\x18\n\x10proposer_address\x18\x0e \x01(\x0c"\x13\n\x04Data\x12\x0b\n\x03txs\x18\x01 \x03(\x0c"\x92\x02\n\x04Vote\x12-\n\x04type\x18\x01 \x01(\x0e2\x1f.tendermint.types.SignedMsgType\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\r\n\x05round\x18\x03 \x01(\x05\x12<\n\x08block_id\x18\x04 \x01(\x0b2\x19.tendermint.types.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID\x127\n\ttimestamp\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x19\n\x11validator_address\x18\x06 \x01(\x0c\x12\x17\n\x0fvalidator_index\x18\x07 \x01(\x05\x12\x11\n\tsignature\x18\x08 \x01(\x0c"\x9c\x01\n\x06Commit\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12<\n\x08block_id\x18\x03 \x01(\x0b2\x19.tendermint.types.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID\x125\n\nsignatures\x18\x04 \x03(\x0b2\x1b.tendermint.types.CommitSigB\x04\xc8\xde\x1f\x00"\xa8\x01\n\tCommitSig\x124\n\rblock_id_flag\x18\x01 \x01(\x0e2\x1d.tendermint.types.BlockIDFlag\x12\x19\n\x11validator_address\x18\x02 \x01(\x0c\x127\n\ttimestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x11\n\tsignature\x18\x04 \x01(\x0c"\xf5\x01\n\x08Proposal\x12-\n\x04type\x18\x01 \x01(\x0e2\x1f.tendermint.types.SignedMsgType\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\r\n\x05round\x18\x03 \x01(\x05\x12\x11\n\tpol_round\x18\x04 \x01(\x05\x12<\n\x08block_id\x18\x05 \x01(\x0b2\x19.tendermint.types.BlockIDB\x0f\xe2\xde\x1f\x07BlockID\xc8\xde\x1f\x00\x127\n\ttimestamp\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x11\n\tsignature\x18\x07 \x01(\x0c"b\n\x0cSignedHeader\x12(\n\x06header\x18\x01 \x01(\x0b2\x18.tendermint.types.Header\x12(\n\x06commit\x18\x02 \x01(\x0b2\x18.tendermint.types.Commit"z\n\nLightBlock\x125\n\rsigned_header\x18\x01 \x01(\x0b2\x1e.tendermint.types.SignedHeader\x125\n\rvalidator_set\x18\x02 \x01(\x0b2\x1e.tendermint.types.ValidatorSet"\x9e\x01\n\tBlockMeta\x12<\n\x08block_id\x18\x01 \x01(\x0b2\x19.tendermint.types.BlockIDB\x0f\xe2\xde\x1f\x07BlockID\xc8\xde\x1f\x00\x12\x12\n\nblock_size\x18\x02 \x01(\x03\x12.\n\x06header\x18\x03 \x01(\x0b2\x18.tendermint.types.HeaderB\x04\xc8\xde\x1f\x00\x12\x0f\n\x07num_txs\x18\x04 \x01(\x03"S\n\x07TxProof\x12\x11\n\troot_hash\x18\x01 \x01(\x0c\x12\x0c\n\x04data\x18\x02 \x01(\x0c\x12\'\n\x05proof\x18\x03 \x01(\x0b2\x18.tendermint.crypto.Proof*\xd7\x01\n\x0bBlockIDFlag\x121\n\x15BLOCK_ID_FLAG_UNKNOWN\x10\x00\x1a\x16\x8a\x9d \x12BlockIDFlagUnknown\x12/\n\x14BLOCK_ID_FLAG_ABSENT\x10\x01\x1a\x15\x8a\x9d \x11BlockIDFlagAbsent\x12/\n\x14BLOCK_ID_FLAG_COMMIT\x10\x02\x1a\x15\x8a\x9d \x11BlockIDFlagCommit\x12)\n\x11BLOCK_ID_FLAG_NIL\x10\x03\x1a\x12\x8a\x9d \x0eBlockIDFlagNil\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00*\xd7\x01\n\rSignedMsgType\x12,\n\x17SIGNED_MSG_TYPE_UNKNOWN\x10\x00\x1a\x0f\x8a\x9d \x0bUnknownType\x12,\n\x17SIGNED_MSG_TYPE_PREVOTE\x10\x01\x1a\x0f\x8a\x9d \x0bPrevoteType\x120\n\x19SIGNED_MSG_TYPE_PRECOMMIT\x10\x02\x1a\x11\x8a\x9d \rPrecommitType\x12.\n\x18SIGNED_MSG_TYPE_PROPOSAL\x10 \x1a\x10\x8a\x9d \x0cProposalType\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00B9Z7github.com/tendermint/tendermint/proto/tendermint/typesb\x06proto3')
_BLOCKIDFLAG = DESCRIPTOR.enum_types_by_name['BlockIDFlag']
BlockIDFlag = enum_type_wrapper.EnumTypeWrapper(_BLOCKIDFLAG)
_SIGNEDMSGTYPE = DESCRIPTOR.enum_types_by_name['SignedMsgType']
SignedMsgType = enum_type_wrapper.EnumTypeWrapper(_SIGNEDMSGTYPE)
BLOCK_ID_FLAG_UNKNOWN = 0
BLOCK_ID_FLAG_ABSENT = 1
BLOCK_ID_FLAG_COMMIT = 2
BLOCK_ID_FLAG_NIL = 3
SIGNED_MSG_TYPE_UNKNOWN = 0
SIGNED_MSG_TYPE_PREVOTE = 1
SIGNED_MSG_TYPE_PRECOMMIT = 2
SIGNED_MSG_TYPE_PROPOSAL = 32
_PARTSETHEADER = DESCRIPTOR.message_types_by_name['PartSetHeader']
_PART = DESCRIPTOR.message_types_by_name['Part']
_BLOCKID = DESCRIPTOR.message_types_by_name['BlockID']
_HEADER = DESCRIPTOR.message_types_by_name['Header']
_DATA = DESCRIPTOR.message_types_by_name['Data']
_VOTE = DESCRIPTOR.message_types_by_name['Vote']
_COMMIT = DESCRIPTOR.message_types_by_name['Commit']
_COMMITSIG = DESCRIPTOR.message_types_by_name['CommitSig']
_PROPOSAL = DESCRIPTOR.message_types_by_name['Proposal']
_SIGNEDHEADER = DESCRIPTOR.message_types_by_name['SignedHeader']
_LIGHTBLOCK = DESCRIPTOR.message_types_by_name['LightBlock']
_BLOCKMETA = DESCRIPTOR.message_types_by_name['BlockMeta']
_TXPROOF = DESCRIPTOR.message_types_by_name['TxProof']
PartSetHeader = _reflection.GeneratedProtocolMessageType('PartSetHeader', (_message.Message,), {'DESCRIPTOR': _PARTSETHEADER, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(PartSetHeader)
Part = _reflection.GeneratedProtocolMessageType('Part', (_message.Message,), {'DESCRIPTOR': _PART, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(Part)
BlockID = _reflection.GeneratedProtocolMessageType('BlockID', (_message.Message,), {'DESCRIPTOR': _BLOCKID, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(BlockID)
Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {'DESCRIPTOR': _HEADER, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(Header)
Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {'DESCRIPTOR': _DATA, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(Data)
Vote = _reflection.GeneratedProtocolMessageType('Vote', (_message.Message,), {'DESCRIPTOR': _VOTE, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(Vote)
Commit = _reflection.GeneratedProtocolMessageType('Commit', (_message.Message,), {'DESCRIPTOR': _COMMIT, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(Commit)
CommitSig = _reflection.GeneratedProtocolMessageType('CommitSig', (_message.Message,), {'DESCRIPTOR': _COMMITSIG, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(CommitSig)
Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), {'DESCRIPTOR': _PROPOSAL, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(Proposal)
SignedHeader = _reflection.GeneratedProtocolMessageType('SignedHeader', (_message.Message,), {'DESCRIPTOR': _SIGNEDHEADER, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(SignedHeader)
LightBlock = _reflection.GeneratedProtocolMessageType('LightBlock', (_message.Message,), {'DESCRIPTOR': _LIGHTBLOCK, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(LightBlock)
BlockMeta = _reflection.GeneratedProtocolMessageType('BlockMeta', (_message.Message,), {'DESCRIPTOR': _BLOCKMETA, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(BlockMeta)
TxProof = _reflection.GeneratedProtocolMessageType('TxProof', (_message.Message,), {'DESCRIPTOR': _TXPROOF, '__module__': 'tendermint.types.types_pb2'})
_sym_db.RegisterMessage(TxProof)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/tendermint/tendermint/proto/tendermint/types'
    _BLOCKIDFLAG._options = None
    _BLOCKIDFLAG._serialized_options = b'\xa8\xa4\x1e\x01\x88\xa3\x1e\x00'
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_UNKNOWN']._options = None
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_UNKNOWN']._serialized_options = b'\x8a\x9d \x12BlockIDFlagUnknown'
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_ABSENT']._options = None
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_ABSENT']._serialized_options = b'\x8a\x9d \x11BlockIDFlagAbsent'
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_COMMIT']._options = None
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_COMMIT']._serialized_options = b'\x8a\x9d \x11BlockIDFlagCommit'
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_NIL']._options = None
    _BLOCKIDFLAG.values_by_name['BLOCK_ID_FLAG_NIL']._serialized_options = b'\x8a\x9d \x0eBlockIDFlagNil'
    _SIGNEDMSGTYPE._options = None
    _SIGNEDMSGTYPE._serialized_options = b'\xa8\xa4\x1e\x01\x88\xa3\x1e\x00'
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_UNKNOWN']._options = None
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_UNKNOWN']._serialized_options = b'\x8a\x9d \x0bUnknownType'
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_PREVOTE']._options = None
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_PREVOTE']._serialized_options = b'\x8a\x9d \x0bPrevoteType'
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_PRECOMMIT']._options = None
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_PRECOMMIT']._serialized_options = b'\x8a\x9d \rPrecommitType'
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_PROPOSAL']._options = None
    _SIGNEDMSGTYPE.values_by_name['SIGNED_MSG_TYPE_PROPOSAL']._serialized_options = b'\x8a\x9d \x0cProposalType'
    _PART.fields_by_name['proof']._options = None
    _PART.fields_by_name['proof']._serialized_options = b'\xc8\xde\x1f\x00'
    _BLOCKID.fields_by_name['part_set_header']._options = None
    _BLOCKID.fields_by_name['part_set_header']._serialized_options = b'\xc8\xde\x1f\x00'
    _HEADER.fields_by_name['version']._options = None
    _HEADER.fields_by_name['version']._serialized_options = b'\xc8\xde\x1f\x00'
    _HEADER.fields_by_name['chain_id']._options = None
    _HEADER.fields_by_name['chain_id']._serialized_options = b'\xe2\xde\x1f\x07ChainID'
    _HEADER.fields_by_name['time']._options = None
    _HEADER.fields_by_name['time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _HEADER.fields_by_name['last_block_id']._options = None
    _HEADER.fields_by_name['last_block_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _VOTE.fields_by_name['block_id']._options = None
    _VOTE.fields_by_name['block_id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID'
    _VOTE.fields_by_name['timestamp']._options = None
    _VOTE.fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _COMMIT.fields_by_name['block_id']._options = None
    _COMMIT.fields_by_name['block_id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID'
    _COMMIT.fields_by_name['signatures']._options = None
    _COMMIT.fields_by_name['signatures']._serialized_options = b'\xc8\xde\x1f\x00'
    _COMMITSIG.fields_by_name['timestamp']._options = None
    _COMMITSIG.fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _PROPOSAL.fields_by_name['block_id']._options = None
    _PROPOSAL.fields_by_name['block_id']._serialized_options = b'\xe2\xde\x1f\x07BlockID\xc8\xde\x1f\x00'
    _PROPOSAL.fields_by_name['timestamp']._options = None
    _PROPOSAL.fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _BLOCKMETA.fields_by_name['block_id']._options = None
    _BLOCKMETA.fields_by_name['block_id']._serialized_options = b'\xe2\xde\x1f\x07BlockID\xc8\xde\x1f\x00'
    _BLOCKMETA.fields_by_name['header']._options = None
    _BLOCKMETA.fields_by_name['header']._serialized_options = b'\xc8\xde\x1f\x00'
    _BLOCKIDFLAG._serialized_start = 2207
    _BLOCKIDFLAG._serialized_end = 2422
    _SIGNEDMSGTYPE._serialized_start = 2425
    _SIGNEDMSGTYPE._serialized_end = 2640
    _PARTSETHEADER._serialized_start = 202
    _PARTSETHEADER._serialized_end = 246
    _PART._serialized_start = 248
    _PART._serialized_end = 331
    _BLOCKID._serialized_start = 333
    _BLOCKID._serialized_end = 420
    _HEADER._serialized_start = 423
    _HEADER._serialized_end = 858
    _DATA._serialized_start = 860
    _DATA._serialized_end = 879
    _VOTE._serialized_start = 882
    _VOTE._serialized_end = 1156
    _COMMIT._serialized_start = 1159
    _COMMIT._serialized_end = 1315
    _COMMITSIG._serialized_start = 1318
    _COMMITSIG._serialized_end = 1486
    _PROPOSAL._serialized_start = 1489
    _PROPOSAL._serialized_end = 1734
    _SIGNEDHEADER._serialized_start = 1736
    _SIGNEDHEADER._serialized_end = 1834
    _LIGHTBLOCK._serialized_start = 1836
    _LIGHTBLOCK._serialized_end = 1958
    _BLOCKMETA._serialized_start = 1961
    _BLOCKMETA._serialized_end = 2119
    _TXPROOF._serialized_start = 2121
    _TXPROOF._serialized_end = 2204
