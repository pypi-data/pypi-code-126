
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fibc/core/channel/v1/query.proto\x12\x13ibc.core.channel.v1\x1a\x1fibc/core/client/v1/client.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a!ibc/core/channel/v1/channel.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto":\n\x13QueryChannelRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t"\x8c\x01\n\x14QueryChannelResponse\x12-\n\x07channel\x18\x01 \x01(\x0b2\x1c.ibc.core.channel.v1.Channel\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"R\n\x14QueryChannelsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xc0\x01\n\x15QueryChannelsResponse\x128\n\x08channels\x18\x01 \x03(\x0b2&.ibc.core.channel.v1.IdentifiedChannel\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse\x120\n\x06height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"p\n\x1eQueryConnectionChannelsRequest\x12\x12\n\nconnection\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xca\x01\n\x1fQueryConnectionChannelsResponse\x128\n\x08channels\x18\x01 \x03(\x0b2&.ibc.core.channel.v1.IdentifiedChannel\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse\x120\n\x06height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"E\n\x1eQueryChannelClientStateRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t"\xb4\x01\n\x1fQueryChannelClientStateResponse\x12J\n\x17identified_client_state\x18\x01 \x01(\x0b2).ibc.core.client.v1.IdentifiedClientState\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"z\n!QueryChannelConsensusStateRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x17\n\x0frevision_number\x18\x03 \x01(\x04\x12\x17\n\x0frevision_height\x18\x04 \x01(\x04"\xad\x01\n"QueryChannelConsensusStateResponse\x12-\n\x0fconsensus_state\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\r\n\x05proof\x18\x03 \x01(\x0c\x126\n\x0cproof_height\x18\x04 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"U\n\x1cQueryPacketCommitmentRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04"z\n\x1dQueryPacketCommitmentResponse\x12\x12\n\ncommitment\x18\x01 \x01(\x0c\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"\x80\x01\n\x1dQueryPacketCommitmentsRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xc6\x01\n\x1eQueryPacketCommitmentsResponse\x125\n\x0bcommitments\x18\x01 \x03(\x0b2 .ibc.core.channel.v1.PacketState\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse\x120\n\x06height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"R\n\x19QueryPacketReceiptRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04"u\n\x1aQueryPacketReceiptResponse\x12\x10\n\x08received\x18\x02 \x01(\x08\x12\r\n\x05proof\x18\x03 \x01(\x0c\x126\n\x0cproof_height\x18\x04 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"Z\n!QueryPacketAcknowledgementRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04"\x84\x01\n"QueryPacketAcknowledgementResponse\x12\x17\n\x0facknowledgement\x18\x01 \x01(\x0c\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"\xaa\x01\n"QueryPacketAcknowledgementsRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12#\n\x1bpacket_commitment_sequences\x18\x04 \x03(\x04"\xd0\x01\n#QueryPacketAcknowledgementsResponse\x12:\n\x10acknowledgements\x18\x01 \x03(\x0b2 .ibc.core.channel.v1.PacketState\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse\x120\n\x06height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"i\n\x1dQueryUnreceivedPacketsRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12#\n\x1bpacket_commitment_sequences\x18\x03 \x03(\x04"e\n\x1eQueryUnreceivedPacketsResponse\x12\x11\n\tsequences\x18\x01 \x03(\x04\x120\n\x06height\x18\x02 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"_\n\x1aQueryUnreceivedAcksRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x1c\n\x14packet_ack_sequences\x18\x03 \x03(\x04"b\n\x1bQueryUnreceivedAcksResponse\x12\x11\n\tsequences\x18\x01 \x03(\x04\x120\n\x06height\x18\x02 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"F\n\x1fQueryNextSequenceReceiveRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t"\x88\x01\n QueryNextSequenceReceiveResponse\x12\x1d\n\x15next_sequence_receive\x18\x01 \x01(\x04\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x002\x8b\x16\n\x05Query\x12\xa2\x01\n\x07Channel\x12(.ibc.core.channel.v1.QueryChannelRequest\x1a).ibc.core.channel.v1.QueryChannelResponse"B\x82\xd3\xe4\x93\x02<\x12:/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}\x12\x88\x01\n\x08Channels\x12).ibc.core.channel.v1.QueryChannelsRequest\x1a*.ibc.core.channel.v1.QueryChannelsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/ibc/core/channel/v1/channels\x12\xbf\x01\n\x12ConnectionChannels\x123.ibc.core.channel.v1.QueryConnectionChannelsRequest\x1a4.ibc.core.channel.v1.QueryConnectionChannelsResponse">\x82\xd3\xe4\x93\x028\x126/ibc/core/channel/v1/connections/{connection}/channels\x12\xd0\x01\n\x12ChannelClientState\x123.ibc.core.channel.v1.QueryChannelClientStateRequest\x1a4.ibc.core.channel.v1.QueryChannelClientStateResponse"O\x82\xd3\xe4\x93\x02I\x12G/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/client_state\x12\x92\x02\n\x15ChannelConsensusState\x126.ibc.core.channel.v1.QueryChannelConsensusStateRequest\x1a7.ibc.core.channel.v1.QueryChannelConsensusStateResponse"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01\x12~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/consensus_state/revision/{revision_number}/height/{revision_height}\x12\xdb\x01\n\x10PacketCommitment\x121.ibc.core.channel.v1.QueryPacketCommitmentRequest\x1a2.ibc.core.channel.v1.QueryPacketCommitmentResponse"`\x82\xd3\xe4\x93\x02Z\x12X/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{sequence}\x12\xd3\x01\n\x11PacketCommitments\x122.ibc.core.channel.v1.QueryPacketCommitmentsRequest\x1a3.ibc.core.channel.v1.QueryPacketCommitmentsResponse"U\x82\xd3\xe4\x93\x02O\x12M/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments\x12\xcf\x01\n\rPacketReceipt\x12..ibc.core.channel.v1.QueryPacketReceiptRequest\x1a/.ibc.core.channel.v1.QueryPacketReceiptResponse"]\x82\xd3\xe4\x93\x02W\x12U/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_receipts/{sequence}\x12\xe3\x01\n\x15PacketAcknowledgement\x126.ibc.core.channel.v1.QueryPacketAcknowledgementRequest\x1a7.ibc.core.channel.v1.QueryPacketAcknowledgementResponse"Y\x82\xd3\xe4\x93\x02S\x12Q/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acks/{sequence}\x12\xe7\x01\n\x16PacketAcknowledgements\x127.ibc.core.channel.v1.QueryPacketAcknowledgementsRequest\x1a8.ibc.core.channel.v1.QueryPacketAcknowledgementsResponse"Z\x82\xd3\xe4\x93\x02T\x12R/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acknowledgements\x12\x86\x02\n\x11UnreceivedPackets\x122.ibc.core.channel.v1.QueryUnreceivedPacketsRequest\x1a3.ibc.core.channel.v1.QueryUnreceivedPacketsResponse"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01\x12~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_commitment_sequences}/unreceived_packets\x12\xf1\x01\n\x0eUnreceivedAcks\x12/.ibc.core.channel.v1.QueryUnreceivedAcksRequest\x1a0.ibc.core.channel.v1.QueryUnreceivedAcksResponse"|\x82\xd3\xe4\x93\x02v\x12t/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_ack_sequences}/unreceived_acks\x12\xd4\x01\n\x13NextSequenceReceive\x124.ibc.core.channel.v1.QueryNextSequenceReceiveRequest\x1a5.ibc.core.channel.v1.QueryNextSequenceReceiveResponse"P\x82\xd3\xe4\x93\x02J\x12H/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequenceB;Z9github.com/cosmos/ibc-go/v3/modules/core/04-channel/typesb\x06proto3')
_QUERYCHANNELREQUEST = DESCRIPTOR.message_types_by_name['QueryChannelRequest']
_QUERYCHANNELRESPONSE = DESCRIPTOR.message_types_by_name['QueryChannelResponse']
_QUERYCHANNELSREQUEST = DESCRIPTOR.message_types_by_name['QueryChannelsRequest']
_QUERYCHANNELSRESPONSE = DESCRIPTOR.message_types_by_name['QueryChannelsResponse']
_QUERYCONNECTIONCHANNELSREQUEST = DESCRIPTOR.message_types_by_name['QueryConnectionChannelsRequest']
_QUERYCONNECTIONCHANNELSRESPONSE = DESCRIPTOR.message_types_by_name['QueryConnectionChannelsResponse']
_QUERYCHANNELCLIENTSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryChannelClientStateRequest']
_QUERYCHANNELCLIENTSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryChannelClientStateResponse']
_QUERYCHANNELCONSENSUSSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryChannelConsensusStateRequest']
_QUERYCHANNELCONSENSUSSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryChannelConsensusStateResponse']
_QUERYPACKETCOMMITMENTREQUEST = DESCRIPTOR.message_types_by_name['QueryPacketCommitmentRequest']
_QUERYPACKETCOMMITMENTRESPONSE = DESCRIPTOR.message_types_by_name['QueryPacketCommitmentResponse']
_QUERYPACKETCOMMITMENTSREQUEST = DESCRIPTOR.message_types_by_name['QueryPacketCommitmentsRequest']
_QUERYPACKETCOMMITMENTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryPacketCommitmentsResponse']
_QUERYPACKETRECEIPTREQUEST = DESCRIPTOR.message_types_by_name['QueryPacketReceiptRequest']
_QUERYPACKETRECEIPTRESPONSE = DESCRIPTOR.message_types_by_name['QueryPacketReceiptResponse']
_QUERYPACKETACKNOWLEDGEMENTREQUEST = DESCRIPTOR.message_types_by_name['QueryPacketAcknowledgementRequest']
_QUERYPACKETACKNOWLEDGEMENTRESPONSE = DESCRIPTOR.message_types_by_name['QueryPacketAcknowledgementResponse']
_QUERYPACKETACKNOWLEDGEMENTSREQUEST = DESCRIPTOR.message_types_by_name['QueryPacketAcknowledgementsRequest']
_QUERYPACKETACKNOWLEDGEMENTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryPacketAcknowledgementsResponse']
_QUERYUNRECEIVEDPACKETSREQUEST = DESCRIPTOR.message_types_by_name['QueryUnreceivedPacketsRequest']
_QUERYUNRECEIVEDPACKETSRESPONSE = DESCRIPTOR.message_types_by_name['QueryUnreceivedPacketsResponse']
_QUERYUNRECEIVEDACKSREQUEST = DESCRIPTOR.message_types_by_name['QueryUnreceivedAcksRequest']
_QUERYUNRECEIVEDACKSRESPONSE = DESCRIPTOR.message_types_by_name['QueryUnreceivedAcksResponse']
_QUERYNEXTSEQUENCERECEIVEREQUEST = DESCRIPTOR.message_types_by_name['QueryNextSequenceReceiveRequest']
_QUERYNEXTSEQUENCERECEIVERESPONSE = DESCRIPTOR.message_types_by_name['QueryNextSequenceReceiveResponse']
QueryChannelRequest = _reflection.GeneratedProtocolMessageType('QueryChannelRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelRequest)
QueryChannelResponse = _reflection.GeneratedProtocolMessageType('QueryChannelResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelResponse)
QueryChannelsRequest = _reflection.GeneratedProtocolMessageType('QueryChannelsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELSREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelsRequest)
QueryChannelsResponse = _reflection.GeneratedProtocolMessageType('QueryChannelsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELSRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelsResponse)
QueryConnectionChannelsRequest = _reflection.GeneratedProtocolMessageType('QueryConnectionChannelsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCONNECTIONCHANNELSREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryConnectionChannelsRequest)
QueryConnectionChannelsResponse = _reflection.GeneratedProtocolMessageType('QueryConnectionChannelsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCONNECTIONCHANNELSRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryConnectionChannelsResponse)
QueryChannelClientStateRequest = _reflection.GeneratedProtocolMessageType('QueryChannelClientStateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELCLIENTSTATEREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelClientStateRequest)
QueryChannelClientStateResponse = _reflection.GeneratedProtocolMessageType('QueryChannelClientStateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELCLIENTSTATERESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelClientStateResponse)
QueryChannelConsensusStateRequest = _reflection.GeneratedProtocolMessageType('QueryChannelConsensusStateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELCONSENSUSSTATEREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelConsensusStateRequest)
QueryChannelConsensusStateResponse = _reflection.GeneratedProtocolMessageType('QueryChannelConsensusStateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCHANNELCONSENSUSSTATERESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryChannelConsensusStateResponse)
QueryPacketCommitmentRequest = _reflection.GeneratedProtocolMessageType('QueryPacketCommitmentRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETCOMMITMENTREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketCommitmentRequest)
QueryPacketCommitmentResponse = _reflection.GeneratedProtocolMessageType('QueryPacketCommitmentResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETCOMMITMENTRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketCommitmentResponse)
QueryPacketCommitmentsRequest = _reflection.GeneratedProtocolMessageType('QueryPacketCommitmentsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETCOMMITMENTSREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketCommitmentsRequest)
QueryPacketCommitmentsResponse = _reflection.GeneratedProtocolMessageType('QueryPacketCommitmentsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETCOMMITMENTSRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketCommitmentsResponse)
QueryPacketReceiptRequest = _reflection.GeneratedProtocolMessageType('QueryPacketReceiptRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETRECEIPTREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketReceiptRequest)
QueryPacketReceiptResponse = _reflection.GeneratedProtocolMessageType('QueryPacketReceiptResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETRECEIPTRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketReceiptResponse)
QueryPacketAcknowledgementRequest = _reflection.GeneratedProtocolMessageType('QueryPacketAcknowledgementRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETACKNOWLEDGEMENTREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketAcknowledgementRequest)
QueryPacketAcknowledgementResponse = _reflection.GeneratedProtocolMessageType('QueryPacketAcknowledgementResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETACKNOWLEDGEMENTRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketAcknowledgementResponse)
QueryPacketAcknowledgementsRequest = _reflection.GeneratedProtocolMessageType('QueryPacketAcknowledgementsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETACKNOWLEDGEMENTSREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketAcknowledgementsRequest)
QueryPacketAcknowledgementsResponse = _reflection.GeneratedProtocolMessageType('QueryPacketAcknowledgementsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPACKETACKNOWLEDGEMENTSRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPacketAcknowledgementsResponse)
QueryUnreceivedPacketsRequest = _reflection.GeneratedProtocolMessageType('QueryUnreceivedPacketsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYUNRECEIVEDPACKETSREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryUnreceivedPacketsRequest)
QueryUnreceivedPacketsResponse = _reflection.GeneratedProtocolMessageType('QueryUnreceivedPacketsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYUNRECEIVEDPACKETSRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryUnreceivedPacketsResponse)
QueryUnreceivedAcksRequest = _reflection.GeneratedProtocolMessageType('QueryUnreceivedAcksRequest', (_message.Message,), {'DESCRIPTOR': _QUERYUNRECEIVEDACKSREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryUnreceivedAcksRequest)
QueryUnreceivedAcksResponse = _reflection.GeneratedProtocolMessageType('QueryUnreceivedAcksResponse', (_message.Message,), {'DESCRIPTOR': _QUERYUNRECEIVEDACKSRESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryUnreceivedAcksResponse)
QueryNextSequenceReceiveRequest = _reflection.GeneratedProtocolMessageType('QueryNextSequenceReceiveRequest', (_message.Message,), {'DESCRIPTOR': _QUERYNEXTSEQUENCERECEIVEREQUEST, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryNextSequenceReceiveRequest)
QueryNextSequenceReceiveResponse = _reflection.GeneratedProtocolMessageType('QueryNextSequenceReceiveResponse', (_message.Message,), {'DESCRIPTOR': _QUERYNEXTSEQUENCERECEIVERESPONSE, '__module__': 'ibc.core.channel.v1.query_pb2'})
_sym_db.RegisterMessage(QueryNextSequenceReceiveResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/cosmos/ibc-go/v3/modules/core/04-channel/types'
    _QUERYCHANNELRESPONSE.fields_by_name['proof_height']._options = None
    _QUERYCHANNELRESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCHANNELSRESPONSE.fields_by_name['height']._options = None
    _QUERYCHANNELSRESPONSE.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCONNECTIONCHANNELSRESPONSE.fields_by_name['height']._options = None
    _QUERYCONNECTIONCHANNELSRESPONSE.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCHANNELCLIENTSTATERESPONSE.fields_by_name['proof_height']._options = None
    _QUERYCHANNELCLIENTSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCHANNELCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._options = None
    _QUERYCHANNELCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPACKETCOMMITMENTRESPONSE.fields_by_name['proof_height']._options = None
    _QUERYPACKETCOMMITMENTRESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPACKETCOMMITMENTSRESPONSE.fields_by_name['height']._options = None
    _QUERYPACKETCOMMITMENTSRESPONSE.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPACKETRECEIPTRESPONSE.fields_by_name['proof_height']._options = None
    _QUERYPACKETRECEIPTRESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPACKETACKNOWLEDGEMENTRESPONSE.fields_by_name['proof_height']._options = None
    _QUERYPACKETACKNOWLEDGEMENTRESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPACKETACKNOWLEDGEMENTSRESPONSE.fields_by_name['height']._options = None
    _QUERYPACKETACKNOWLEDGEMENTSRESPONSE.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYUNRECEIVEDPACKETSRESPONSE.fields_by_name['height']._options = None
    _QUERYUNRECEIVEDPACKETSRESPONSE.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYUNRECEIVEDACKSRESPONSE.fields_by_name['height']._options = None
    _QUERYUNRECEIVEDACKSRESPONSE.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYNEXTSEQUENCERECEIVERESPONSE.fields_by_name['proof_height']._options = None
    _QUERYNEXTSEQUENCERECEIVERESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Channel']._options = None
    _QUERY.methods_by_name['Channel']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}'
    _QUERY.methods_by_name['Channels']._options = None
    _QUERY.methods_by_name['Channels']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/ibc/core/channel/v1/channels'
    _QUERY.methods_by_name['ConnectionChannels']._options = None
    _QUERY.methods_by_name['ConnectionChannels']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/ibc/core/channel/v1/connections/{connection}/channels'
    _QUERY.methods_by_name['ChannelClientState']._options = None
    _QUERY.methods_by_name['ChannelClientState']._serialized_options = b'\x82\xd3\xe4\x93\x02I\x12G/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/client_state'
    _QUERY.methods_by_name['ChannelConsensusState']._options = None
    _QUERY.methods_by_name['ChannelConsensusState']._serialized_options = b'\x82\xd3\xe4\x93\x02\x80\x01\x12~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/consensus_state/revision/{revision_number}/height/{revision_height}'
    _QUERY.methods_by_name['PacketCommitment']._options = None
    _QUERY.methods_by_name['PacketCommitment']._serialized_options = b'\x82\xd3\xe4\x93\x02Z\x12X/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{sequence}'
    _QUERY.methods_by_name['PacketCommitments']._options = None
    _QUERY.methods_by_name['PacketCommitments']._serialized_options = b'\x82\xd3\xe4\x93\x02O\x12M/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments'
    _QUERY.methods_by_name['PacketReceipt']._options = None
    _QUERY.methods_by_name['PacketReceipt']._serialized_options = b'\x82\xd3\xe4\x93\x02W\x12U/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_receipts/{sequence}'
    _QUERY.methods_by_name['PacketAcknowledgement']._options = None
    _QUERY.methods_by_name['PacketAcknowledgement']._serialized_options = b'\x82\xd3\xe4\x93\x02S\x12Q/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acks/{sequence}'
    _QUERY.methods_by_name['PacketAcknowledgements']._options = None
    _QUERY.methods_by_name['PacketAcknowledgements']._serialized_options = b'\x82\xd3\xe4\x93\x02T\x12R/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acknowledgements'
    _QUERY.methods_by_name['UnreceivedPackets']._options = None
    _QUERY.methods_by_name['UnreceivedPackets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x80\x01\x12~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_commitment_sequences}/unreceived_packets'
    _QUERY.methods_by_name['UnreceivedAcks']._options = None
    _QUERY.methods_by_name['UnreceivedAcks']._serialized_options = b'\x82\xd3\xe4\x93\x02v\x12t/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_ack_sequences}/unreceived_acks'
    _QUERY.methods_by_name['NextSequenceReceive']._options = None
    _QUERY.methods_by_name['NextSequenceReceive']._serialized_options = b'\x82\xd3\xe4\x93\x02J\x12H/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequence'
    _QUERYCHANNELREQUEST._serialized_start = 247
    _QUERYCHANNELREQUEST._serialized_end = 305
    _QUERYCHANNELRESPONSE._serialized_start = 308
    _QUERYCHANNELRESPONSE._serialized_end = 448
    _QUERYCHANNELSREQUEST._serialized_start = 450
    _QUERYCHANNELSREQUEST._serialized_end = 532
    _QUERYCHANNELSRESPONSE._serialized_start = 535
    _QUERYCHANNELSRESPONSE._serialized_end = 727
    _QUERYCONNECTIONCHANNELSREQUEST._serialized_start = 729
    _QUERYCONNECTIONCHANNELSREQUEST._serialized_end = 841
    _QUERYCONNECTIONCHANNELSRESPONSE._serialized_start = 844
    _QUERYCONNECTIONCHANNELSRESPONSE._serialized_end = 1046
    _QUERYCHANNELCLIENTSTATEREQUEST._serialized_start = 1048
    _QUERYCHANNELCLIENTSTATEREQUEST._serialized_end = 1117
    _QUERYCHANNELCLIENTSTATERESPONSE._serialized_start = 1120
    _QUERYCHANNELCLIENTSTATERESPONSE._serialized_end = 1300
    _QUERYCHANNELCONSENSUSSTATEREQUEST._serialized_start = 1302
    _QUERYCHANNELCONSENSUSSTATEREQUEST._serialized_end = 1424
    _QUERYCHANNELCONSENSUSSTATERESPONSE._serialized_start = 1427
    _QUERYCHANNELCONSENSUSSTATERESPONSE._serialized_end = 1600
    _QUERYPACKETCOMMITMENTREQUEST._serialized_start = 1602
    _QUERYPACKETCOMMITMENTREQUEST._serialized_end = 1687
    _QUERYPACKETCOMMITMENTRESPONSE._serialized_start = 1689
    _QUERYPACKETCOMMITMENTRESPONSE._serialized_end = 1811
    _QUERYPACKETCOMMITMENTSREQUEST._serialized_start = 1814
    _QUERYPACKETCOMMITMENTSREQUEST._serialized_end = 1942
    _QUERYPACKETCOMMITMENTSRESPONSE._serialized_start = 1945
    _QUERYPACKETCOMMITMENTSRESPONSE._serialized_end = 2143
    _QUERYPACKETRECEIPTREQUEST._serialized_start = 2145
    _QUERYPACKETRECEIPTREQUEST._serialized_end = 2227
    _QUERYPACKETRECEIPTRESPONSE._serialized_start = 2229
    _QUERYPACKETRECEIPTRESPONSE._serialized_end = 2346
    _QUERYPACKETACKNOWLEDGEMENTREQUEST._serialized_start = 2348
    _QUERYPACKETACKNOWLEDGEMENTREQUEST._serialized_end = 2438
    _QUERYPACKETACKNOWLEDGEMENTRESPONSE._serialized_start = 2441
    _QUERYPACKETACKNOWLEDGEMENTRESPONSE._serialized_end = 2573
    _QUERYPACKETACKNOWLEDGEMENTSREQUEST._serialized_start = 2576
    _QUERYPACKETACKNOWLEDGEMENTSREQUEST._serialized_end = 2746
    _QUERYPACKETACKNOWLEDGEMENTSRESPONSE._serialized_start = 2749
    _QUERYPACKETACKNOWLEDGEMENTSRESPONSE._serialized_end = 2957
    _QUERYUNRECEIVEDPACKETSREQUEST._serialized_start = 2959
    _QUERYUNRECEIVEDPACKETSREQUEST._serialized_end = 3064
    _QUERYUNRECEIVEDPACKETSRESPONSE._serialized_start = 3066
    _QUERYUNRECEIVEDPACKETSRESPONSE._serialized_end = 3167
    _QUERYUNRECEIVEDACKSREQUEST._serialized_start = 3169
    _QUERYUNRECEIVEDACKSREQUEST._serialized_end = 3264
    _QUERYUNRECEIVEDACKSRESPONSE._serialized_start = 3266
    _QUERYUNRECEIVEDACKSRESPONSE._serialized_end = 3364
    _QUERYNEXTSEQUENCERECEIVEREQUEST._serialized_start = 3366
    _QUERYNEXTSEQUENCERECEIVEREQUEST._serialized_end = 3436
    _QUERYNEXTSEQUENCERECEIVERESPONSE._serialized_start = 3439
    _QUERYNEXTSEQUENCERECEIVERESPONSE._serialized_end = 3575
    _QUERY._serialized_start = 3578
    _QUERY._serialized_end = 6405
