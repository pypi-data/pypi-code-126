
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.mint.v1beta1 import mint_pb2 as cosmos_dot_mint_dot_v1beta1_dot_mint__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/mint/v1beta1/query.proto\x12\x13cosmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/mint/v1beta1/mint.proto"\x14\n\x12QueryParamsRequest"H\n\x13QueryParamsResponse\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.cosmos.mint.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\x17\n\x15QueryInflationRequest"[\n\x16QueryInflationResponse\x12A\n\tinflation\x18\x01 \x01(\x0cB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\x1e\n\x1cQueryAnnualProvisionsRequest"j\n\x1dQueryAnnualProvisionsResponse\x12I\n\x11annual_provisions\x18\x01 \x01(\x0cB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x002\xc5\x03\n\x05Query\x12\x80\x01\n\x06Params\x12\'.cosmos.mint.v1beta1.QueryParamsRequest\x1a(.cosmos.mint.v1beta1.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/mint/v1beta1/params\x12\x8c\x01\n\tInflation\x12*.cosmos.mint.v1beta1.QueryInflationRequest\x1a+.cosmos.mint.v1beta1.QueryInflationResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/mint/v1beta1/inflation\x12\xa9\x01\n\x10AnnualProvisions\x121.cosmos.mint.v1beta1.QueryAnnualProvisionsRequest\x1a2.cosmos.mint.v1beta1.QueryAnnualProvisionsResponse".\x82\xd3\xe4\x93\x02(\x12&/cosmos/mint/v1beta1/annual_provisionsB+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3')
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYINFLATIONREQUEST = DESCRIPTOR.message_types_by_name['QueryInflationRequest']
_QUERYINFLATIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryInflationResponse']
_QUERYANNUALPROVISIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryAnnualProvisionsRequest']
_QUERYANNUALPROVISIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryAnnualProvisionsResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'cosmos.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'cosmos.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QueryInflationRequest = _reflection.GeneratedProtocolMessageType('QueryInflationRequest', (_message.Message,), {'DESCRIPTOR': _QUERYINFLATIONREQUEST, '__module__': 'cosmos.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryInflationRequest)
QueryInflationResponse = _reflection.GeneratedProtocolMessageType('QueryInflationResponse', (_message.Message,), {'DESCRIPTOR': _QUERYINFLATIONRESPONSE, '__module__': 'cosmos.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryInflationResponse)
QueryAnnualProvisionsRequest = _reflection.GeneratedProtocolMessageType('QueryAnnualProvisionsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYANNUALPROVISIONSREQUEST, '__module__': 'cosmos.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAnnualProvisionsRequest)
QueryAnnualProvisionsResponse = _reflection.GeneratedProtocolMessageType('QueryAnnualProvisionsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYANNUALPROVISIONSRESPONSE, '__module__': 'cosmos.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAnnualProvisionsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/mint/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYINFLATIONRESPONSE.fields_by_name['inflation']._options = None
    _QUERYINFLATIONRESPONSE.fields_by_name['inflation']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYANNUALPROVISIONSRESPONSE.fields_by_name['annual_provisions']._options = None
    _QUERYANNUALPROVISIONSRESPONSE.fields_by_name['annual_provisions']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/mint/v1beta1/params'
    _QUERY.methods_by_name['Inflation']._options = None
    _QUERY.methods_by_name['Inflation']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/mint/v1beta1/inflation'
    _QUERY.methods_by_name['AnnualProvisions']._options = None
    _QUERY.methods_by_name['AnnualProvisions']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/cosmos/mint/v1beta1/annual_provisions'
    _QUERYPARAMSREQUEST._serialized_start = 140
    _QUERYPARAMSREQUEST._serialized_end = 160
    _QUERYPARAMSRESPONSE._serialized_start = 162
    _QUERYPARAMSRESPONSE._serialized_end = 234
    _QUERYINFLATIONREQUEST._serialized_start = 236
    _QUERYINFLATIONREQUEST._serialized_end = 259
    _QUERYINFLATIONRESPONSE._serialized_start = 261
    _QUERYINFLATIONRESPONSE._serialized_end = 352
    _QUERYANNUALPROVISIONSREQUEST._serialized_start = 354
    _QUERYANNUALPROVISIONSREQUEST._serialized_end = 384
    _QUERYANNUALPROVISIONSRESPONSE._serialized_start = 386
    _QUERYANNUALPROVISIONSRESPONSE._serialized_end = 492
    _QUERY._serialized_start = 495
    _QUERY._serialized_end = 948
