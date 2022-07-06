
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.nft.v1beta1 import nft_pb2 as cosmos_dot_nft_dot_v1beta1_dot_nft__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/nft/v1beta1/query.proto\x12\x12cosmos.nft.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ccosmos/nft/v1beta1/nft.proto"6\n\x13QueryBalanceRequest\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t"&\n\x14QueryBalanceResponse\x12\x0e\n\x06amount\x18\x01 \x01(\x04"1\n\x11QueryOwnerRequest\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t"#\n\x12QueryOwnerResponse\x12\r\n\x05owner\x18\x01 \x01(\t"&\n\x12QuerySupplyRequest\x12\x10\n\x08class_id\x18\x01 \x01(\t"%\n\x13QuerySupplyResponse\x12\x0e\n\x06amount\x18\x01 \x01(\x04"o\n\x10QueryNFTsRequest\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"w\n\x11QueryNFTsResponse\x12%\n\x04nfts\x18\x01 \x03(\x0b2\x17.cosmos.nft.v1beta1.NFT\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"/\n\x0fQueryNFTRequest\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t"8\n\x10QueryNFTResponse\x12$\n\x03nft\x18\x01 \x01(\x0b2\x17.cosmos.nft.v1beta1.NFT"%\n\x11QueryClassRequest\x12\x10\n\x08class_id\x18\x01 \x01(\t">\n\x12QueryClassResponse\x12(\n\x05class\x18\x01 \x01(\x0b2\x19.cosmos.nft.v1beta1.Class"Q\n\x13QueryClassesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x7f\n\x14QueryClassesResponse\x12*\n\x07classes\x18\x01 \x03(\x0b2\x19.cosmos.nft.v1beta1.Class\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\xbe\x07\n\x05Query\x12\x94\x01\n\x07Balance\x12\'.cosmos.nft.v1beta1.QueryBalanceRequest\x1a(.cosmos.nft.v1beta1.QueryBalanceResponse"6\x82\xd3\xe4\x93\x020\x12./cosmos/nft/v1beta1/balance/{owner}/{class_id}\x12\x89\x01\n\x05Owner\x12%.cosmos.nft.v1beta1.QueryOwnerRequest\x1a&.cosmos.nft.v1beta1.QueryOwnerResponse"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/nft/v1beta1/owner/{class_id}/{id}\x12\x88\x01\n\x06Supply\x12&.cosmos.nft.v1beta1.QuerySupplyRequest\x1a\'.cosmos.nft.v1beta1.QuerySupplyResponse"-\x82\xd3\xe4\x93\x02\'\x12%/cosmos/nft/v1beta1/supply/{class_id}\x12u\n\x04NFTs\x12$.cosmos.nft.v1beta1.QueryNFTsRequest\x1a%.cosmos.nft.v1beta1.QueryNFTsResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/cosmos/nft/v1beta1/nfts\x12\x82\x01\n\x03NFT\x12#.cosmos.nft.v1beta1.QueryNFTRequest\x1a$.cosmos.nft.v1beta1.QueryNFTResponse"0\x82\xd3\xe4\x93\x02*\x12(/cosmos/nft/v1beta1/nfts/{class_id}/{id}\x12\x86\x01\n\x05Class\x12%.cosmos.nft.v1beta1.QueryClassRequest\x1a&.cosmos.nft.v1beta1.QueryClassResponse".\x82\xd3\xe4\x93\x02(\x12&/cosmos/nft/v1beta1/classes/{class_id}\x12\x81\x01\n\x07Classes\x12\'.cosmos.nft.v1beta1.QueryClassesRequest\x1a(.cosmos.nft.v1beta1.QueryClassesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/nft/v1beta1/classesB$Z"github.com/cosmos/cosmos-sdk/x/nftb\x06proto3')
_QUERYBALANCEREQUEST = DESCRIPTOR.message_types_by_name['QueryBalanceRequest']
_QUERYBALANCERESPONSE = DESCRIPTOR.message_types_by_name['QueryBalanceResponse']
_QUERYOWNERREQUEST = DESCRIPTOR.message_types_by_name['QueryOwnerRequest']
_QUERYOWNERRESPONSE = DESCRIPTOR.message_types_by_name['QueryOwnerResponse']
_QUERYSUPPLYREQUEST = DESCRIPTOR.message_types_by_name['QuerySupplyRequest']
_QUERYSUPPLYRESPONSE = DESCRIPTOR.message_types_by_name['QuerySupplyResponse']
_QUERYNFTSREQUEST = DESCRIPTOR.message_types_by_name['QueryNFTsRequest']
_QUERYNFTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryNFTsResponse']
_QUERYNFTREQUEST = DESCRIPTOR.message_types_by_name['QueryNFTRequest']
_QUERYNFTRESPONSE = DESCRIPTOR.message_types_by_name['QueryNFTResponse']
_QUERYCLASSREQUEST = DESCRIPTOR.message_types_by_name['QueryClassRequest']
_QUERYCLASSRESPONSE = DESCRIPTOR.message_types_by_name['QueryClassResponse']
_QUERYCLASSESREQUEST = DESCRIPTOR.message_types_by_name['QueryClassesRequest']
_QUERYCLASSESRESPONSE = DESCRIPTOR.message_types_by_name['QueryClassesResponse']
QueryBalanceRequest = _reflection.GeneratedProtocolMessageType('QueryBalanceRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBALANCEREQUEST, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBalanceRequest)
QueryBalanceResponse = _reflection.GeneratedProtocolMessageType('QueryBalanceResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBALANCERESPONSE, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBalanceResponse)
QueryOwnerRequest = _reflection.GeneratedProtocolMessageType('QueryOwnerRequest', (_message.Message,), {'DESCRIPTOR': _QUERYOWNERREQUEST, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryOwnerRequest)
QueryOwnerResponse = _reflection.GeneratedProtocolMessageType('QueryOwnerResponse', (_message.Message,), {'DESCRIPTOR': _QUERYOWNERRESPONSE, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryOwnerResponse)
QuerySupplyRequest = _reflection.GeneratedProtocolMessageType('QuerySupplyRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSUPPLYREQUEST, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySupplyRequest)
QuerySupplyResponse = _reflection.GeneratedProtocolMessageType('QuerySupplyResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSUPPLYRESPONSE, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySupplyResponse)
QueryNFTsRequest = _reflection.GeneratedProtocolMessageType('QueryNFTsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYNFTSREQUEST, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryNFTsRequest)
QueryNFTsResponse = _reflection.GeneratedProtocolMessageType('QueryNFTsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYNFTSRESPONSE, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryNFTsResponse)
QueryNFTRequest = _reflection.GeneratedProtocolMessageType('QueryNFTRequest', (_message.Message,), {'DESCRIPTOR': _QUERYNFTREQUEST, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryNFTRequest)
QueryNFTResponse = _reflection.GeneratedProtocolMessageType('QueryNFTResponse', (_message.Message,), {'DESCRIPTOR': _QUERYNFTRESPONSE, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryNFTResponse)
QueryClassRequest = _reflection.GeneratedProtocolMessageType('QueryClassRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCLASSREQUEST, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryClassRequest)
QueryClassResponse = _reflection.GeneratedProtocolMessageType('QueryClassResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCLASSRESPONSE, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryClassResponse)
QueryClassesRequest = _reflection.GeneratedProtocolMessageType('QueryClassesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCLASSESREQUEST, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryClassesRequest)
QueryClassesResponse = _reflection.GeneratedProtocolMessageType('QueryClassesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCLASSESRESPONSE, '__module__': 'cosmos.nft.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryClassesResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/x/nft'
    _QUERY.methods_by_name['Balance']._options = None
    _QUERY.methods_by_name['Balance']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./cosmos/nft/v1beta1/balance/{owner}/{class_id}'
    _QUERY.methods_by_name['Owner']._options = None
    _QUERY.methods_by_name['Owner']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/cosmos/nft/v1beta1/owner/{class_id}/{id}'
    _QUERY.methods_by_name['Supply']._options = None
    _QUERY.methods_by_name['Supply']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/cosmos/nft/v1beta1/supply/{class_id}"
    _QUERY.methods_by_name['NFTs']._options = None
    _QUERY.methods_by_name['NFTs']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/cosmos/nft/v1beta1/nfts'
    _QUERY.methods_by_name['NFT']._options = None
    _QUERY.methods_by_name['NFT']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/cosmos/nft/v1beta1/nfts/{class_id}/{id}'
    _QUERY.methods_by_name['Class']._options = None
    _QUERY.methods_by_name['Class']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/cosmos/nft/v1beta1/classes/{class_id}'
    _QUERY.methods_by_name['Classes']._options = None
    _QUERY.methods_by_name['Classes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/nft/v1beta1/classes'
    _QUERYBALANCEREQUEST._serialized_start = 158
    _QUERYBALANCEREQUEST._serialized_end = 212
    _QUERYBALANCERESPONSE._serialized_start = 214
    _QUERYBALANCERESPONSE._serialized_end = 252
    _QUERYOWNERREQUEST._serialized_start = 254
    _QUERYOWNERREQUEST._serialized_end = 303
    _QUERYOWNERRESPONSE._serialized_start = 305
    _QUERYOWNERRESPONSE._serialized_end = 340
    _QUERYSUPPLYREQUEST._serialized_start = 342
    _QUERYSUPPLYREQUEST._serialized_end = 380
    _QUERYSUPPLYRESPONSE._serialized_start = 382
    _QUERYSUPPLYRESPONSE._serialized_end = 419
    _QUERYNFTSREQUEST._serialized_start = 421
    _QUERYNFTSREQUEST._serialized_end = 532
    _QUERYNFTSRESPONSE._serialized_start = 534
    _QUERYNFTSRESPONSE._serialized_end = 653
    _QUERYNFTREQUEST._serialized_start = 655
    _QUERYNFTREQUEST._serialized_end = 702
    _QUERYNFTRESPONSE._serialized_start = 704
    _QUERYNFTRESPONSE._serialized_end = 760
    _QUERYCLASSREQUEST._serialized_start = 762
    _QUERYCLASSREQUEST._serialized_end = 799
    _QUERYCLASSRESPONSE._serialized_start = 801
    _QUERYCLASSRESPONSE._serialized_end = 863
    _QUERYCLASSESREQUEST._serialized_start = 865
    _QUERYCLASSESREQUEST._serialized_end = 946
    _QUERYCLASSESRESPONSE._serialized_start = 948
    _QUERYCLASSESRESPONSE._serialized_end = 1075
    _QUERY._serialized_start = 1078
    _QUERY._serialized_end = 2036
