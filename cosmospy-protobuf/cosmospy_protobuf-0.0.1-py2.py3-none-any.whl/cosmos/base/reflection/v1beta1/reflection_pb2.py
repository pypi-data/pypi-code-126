
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/cosmos/base/reflection/v1beta1/reflection.proto\x12\x1ecosmos.base.reflection.v1beta1\x1a\x1cgoogle/api/annotations.proto"\x1a\n\x18ListAllInterfacesRequest"4\n\x19ListAllInterfacesResponse\x12\x17\n\x0finterface_names\x18\x01 \x03(\t"4\n\x1aListImplementationsRequest\x12\x16\n\x0einterface_name\x18\x01 \x01(\t"C\n\x1bListImplementationsResponse\x12$\n\x1cimplementation_message_names\x18\x01 \x03(\t2\xb8\x03\n\x11ReflectionService\x12\xbc\x01\n\x11ListAllInterfaces\x128.cosmos.base.reflection.v1beta1.ListAllInterfacesRequest\x1a9.cosmos.base.reflection.v1beta1.ListAllInterfacesResponse"2\x82\xd3\xe4\x93\x02,\x12*/cosmos/base/reflection/v1beta1/interfaces\x12\xe3\x01\n\x13ListImplementations\x12:.cosmos.base.reflection.v1beta1.ListImplementationsRequest\x1a;.cosmos.base.reflection.v1beta1.ListImplementationsResponse"S\x82\xd3\xe4\x93\x02M\x12K/cosmos/base/reflection/v1beta1/interfaces/{interface_name}/implementationsB5Z3github.com/cosmos/cosmos-sdk/client/grpc/reflectionb\x06proto3')
_LISTALLINTERFACESREQUEST = DESCRIPTOR.message_types_by_name['ListAllInterfacesRequest']
_LISTALLINTERFACESRESPONSE = DESCRIPTOR.message_types_by_name['ListAllInterfacesResponse']
_LISTIMPLEMENTATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListImplementationsRequest']
_LISTIMPLEMENTATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListImplementationsResponse']
ListAllInterfacesRequest = _reflection.GeneratedProtocolMessageType('ListAllInterfacesRequest', (_message.Message,), {'DESCRIPTOR': _LISTALLINTERFACESREQUEST, '__module__': 'cosmos.base.reflection.v1beta1.reflection_pb2'})
_sym_db.RegisterMessage(ListAllInterfacesRequest)
ListAllInterfacesResponse = _reflection.GeneratedProtocolMessageType('ListAllInterfacesResponse', (_message.Message,), {'DESCRIPTOR': _LISTALLINTERFACESRESPONSE, '__module__': 'cosmos.base.reflection.v1beta1.reflection_pb2'})
_sym_db.RegisterMessage(ListAllInterfacesResponse)
ListImplementationsRequest = _reflection.GeneratedProtocolMessageType('ListImplementationsRequest', (_message.Message,), {'DESCRIPTOR': _LISTIMPLEMENTATIONSREQUEST, '__module__': 'cosmos.base.reflection.v1beta1.reflection_pb2'})
_sym_db.RegisterMessage(ListImplementationsRequest)
ListImplementationsResponse = _reflection.GeneratedProtocolMessageType('ListImplementationsResponse', (_message.Message,), {'DESCRIPTOR': _LISTIMPLEMENTATIONSRESPONSE, '__module__': 'cosmos.base.reflection.v1beta1.reflection_pb2'})
_sym_db.RegisterMessage(ListImplementationsResponse)
_REFLECTIONSERVICE = DESCRIPTOR.services_by_name['ReflectionService']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z3github.com/cosmos/cosmos-sdk/client/grpc/reflection'
    _REFLECTIONSERVICE.methods_by_name['ListAllInterfaces']._options = None
    _REFLECTIONSERVICE.methods_by_name['ListAllInterfaces']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/cosmos/base/reflection/v1beta1/interfaces'
    _REFLECTIONSERVICE.methods_by_name['ListImplementations']._options = None
    _REFLECTIONSERVICE.methods_by_name['ListImplementations']._serialized_options = b'\x82\xd3\xe4\x93\x02M\x12K/cosmos/base/reflection/v1beta1/interfaces/{interface_name}/implementations'
    _LISTALLINTERFACESREQUEST._serialized_start = 113
    _LISTALLINTERFACESREQUEST._serialized_end = 139
    _LISTALLINTERFACESRESPONSE._serialized_start = 141
    _LISTALLINTERFACESRESPONSE._serialized_end = 193
    _LISTIMPLEMENTATIONSREQUEST._serialized_start = 195
    _LISTIMPLEMENTATIONSREQUEST._serialized_end = 247
    _LISTIMPLEMENTATIONSRESPONSE._serialized_start = 249
    _LISTIMPLEMENTATIONSRESPONSE._serialized_end = 316
    _REFLECTIONSERVICE._serialized_start = 319
    _REFLECTIONSERVICE._serialized_end = 759
