import json

from bitstring import ConstBitStream

# from .crc import calculate
from .encryption import decrypt

OFFSET_ENCRYPTED = 16


class Packet:
    header_size = 38

    def __init__(self) -> None:
        self.header = {}
        self.payload = {}

    def set_header_value(self, key, value):
        self.header[key] = value

    def get_header_value(self, key):
        return self.header[key]


class D2LParser:
    last_packet = None
    prev_packet = None

    def __init__(self, d2l_key: str, d2l_iv: str) -> None:
        self.d2l_key = bytes.fromhex(d2l_key)
        self.d2l_iv = bytes.fromhex(d2l_iv)

    def get_last_packet(self) -> Packet:
        return self.last_packet

    def get_previous_packet(self) -> Packet:
        return self.prev_packet

    def parse_request(self, msg_encrypted: bytes) -> None:
        '''
        Return a Packet which contains a header and payload dict with all data
        '''
        self.prev_packet = self.last_packet
        self.last_packet = Packet()
        msg_decrypted = self._decrypt(msg_encrypted)
        self._parse_header(msg_decrypted, self.last_packet)
        self._parse_payload(msg_decrypted, self.last_packet)

    def _parse_header(self, message: bytes, packet: Packet):
        bitstream = ConstBitStream(message)
        packet.set_header_value("versionProtocole", bitstream.read('uint:8'))
        bitstream.read(8)           # Unused
        packet.set_header_value("tailleTrame", bitstream.read('uintle:16'))
        packet.set_header_value("idD2L", bitstream.read('uintle:64'))
        packet.set_header_value("Clef", bitstream.read('bits:8').int & 0b00000011)
        bitstream.read(24)          # Unused
        packet.set_header_value("NombreAleatoire", bitstream.read('uintle:128'))
        packet.set_header_value("CRC16", bitstream.read('uintle:16'))
        packet.set_header_value("taillePayload", bitstream.read('uintle:16'))
        bitstream.read('bits:1')    # Unused
        packet.set_header_value("IsRequeteOuReponse", bitstream.read('bool:1'))
        packet.set_header_value("TypePayload", bitstream.read('bits:6').uint)
        bitstream.read('bits:1')    # Unused
        packet.header["IsErreurTraitement"] = bitstream.read('bool:1')
        packet.header["CommandeSuivante"] = bitstream.read('bits:6').uint
        packet.payload_size = packet.header["taillePayload"]

    def _parse_payload(self, message: bytes, packet: Packet):
        msg_payload = message[packet.header_size:]
        str_payload = msg_payload[:packet.payload_size].decode('utf-8')

        # Append end of JSON if omitted
        if "}" != str_payload[-1]:
            if "\"" not in str_payload[-2:]:
                str_payload += '"'
            if "}" not in str_payload[-2:]:
                str_payload += ' }'

        packet.payload = json.loads(str_payload)

    def _decrypt(self, msg_encrypted: bytes):
        message_done = msg_encrypted[:OFFSET_ENCRYPTED]
        message_todo = msg_encrypted[OFFSET_ENCRYPTED:]
        message_todo = decrypt(message_todo, self.d2l_key, self.d2l_iv)
        return message_done + message_todo
