
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19cosmos_proto/cosmos.proto\x12\x0ccosmos_proto\x1a google/protobuf/descriptor.proto"8\n\x13InterfaceDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t"c\n\x10ScalarDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12,\n\nfield_type\x18\x03 \x03(\x0e2\x18.cosmos_proto.ScalarType*X\n\nScalarType\x12\x1b\n\x17SCALAR_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12SCALAR_TYPE_STRING\x10\x01\x12\x15\n\x11SCALAR_TYPE_BYTES\x10\x02:?\n\x14implements_interface\x12\x1f.google.protobuf.MessageOptions\x18\xc9\xd6\x05 \x03(\t::\n\x11accepts_interface\x12\x1d.google.protobuf.FieldOptions\x18\xc9\xd6\x05 \x01(\t:/\n\x06scalar\x12\x1d.google.protobuf.FieldOptions\x18\xca\xd6\x05 \x01(\t:\\\n\x11declare_interface\x12\x1c.google.protobuf.FileOptions\x18\xbd\xb30 \x03(\x0b2!.cosmos_proto.InterfaceDescriptor:V\n\x0edeclare_scalar\x12\x1c.google.protobuf.FileOptions\x18\xbe\xb30 \x03(\x0b2\x1e.cosmos_proto.ScalarDescriptorB-Z+github.com/cosmos/cosmos-proto;cosmos_protob\x06proto3')
_SCALARTYPE = DESCRIPTOR.enum_types_by_name['ScalarType']
ScalarType = enum_type_wrapper.EnumTypeWrapper(_SCALARTYPE)
SCALAR_TYPE_UNSPECIFIED = 0
SCALAR_TYPE_STRING = 1
SCALAR_TYPE_BYTES = 2
IMPLEMENTS_INTERFACE_FIELD_NUMBER = 93001
implements_interface = DESCRIPTOR.extensions_by_name['implements_interface']
ACCEPTS_INTERFACE_FIELD_NUMBER = 93001
accepts_interface = DESCRIPTOR.extensions_by_name['accepts_interface']
SCALAR_FIELD_NUMBER = 93002
scalar = DESCRIPTOR.extensions_by_name['scalar']
DECLARE_INTERFACE_FIELD_NUMBER = 793021
declare_interface = DESCRIPTOR.extensions_by_name['declare_interface']
DECLARE_SCALAR_FIELD_NUMBER = 793022
declare_scalar = DESCRIPTOR.extensions_by_name['declare_scalar']
_INTERFACEDESCRIPTOR = DESCRIPTOR.message_types_by_name['InterfaceDescriptor']
_SCALARDESCRIPTOR = DESCRIPTOR.message_types_by_name['ScalarDescriptor']
InterfaceDescriptor = _reflection.GeneratedProtocolMessageType('InterfaceDescriptor', (_message.Message,), {'DESCRIPTOR': _INTERFACEDESCRIPTOR, '__module__': 'cosmos_proto.cosmos_pb2'})
_sym_db.RegisterMessage(InterfaceDescriptor)
ScalarDescriptor = _reflection.GeneratedProtocolMessageType('ScalarDescriptor', (_message.Message,), {'DESCRIPTOR': _SCALARDESCRIPTOR, '__module__': 'cosmos_proto.cosmos_pb2'})
_sym_db.RegisterMessage(ScalarDescriptor)
if (_descriptor._USE_C_DESCRIPTORS == False):
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(implements_interface)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(accepts_interface)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(scalar)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(declare_interface)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(declare_scalar)
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-proto;cosmos_proto'
    _SCALARTYPE._serialized_start = 236
    _SCALARTYPE._serialized_end = 324
    _INTERFACEDESCRIPTOR._serialized_start = 77
    _INTERFACEDESCRIPTOR._serialized_end = 133
    _SCALARDESCRIPTOR._serialized_start = 135
    _SCALARDESCRIPTOR._serialized_end = 234
