import base64
import typing

from thriftpy2.protocol import TCompactProtocolFactory
from thriftpy2.transport import TMemoryBuffer


class ThriftReadWrite:
    def __init__(self, thrift_type):
        self.thrift_type = thrift_type
        self._t_memory_buffer = TMemoryBuffer()
        self._t_proto = TCompactProtocolFactory().get_protocol(self._t_memory_buffer)

    def to_bytes(self, thrift_obj) -> bytes:
        """Convert a thrift object into bytes."""
        if not isinstance(thrift_obj, self.thrift_type):
            raise TypeError(f"Expected {self.thrift_type} but got {type(thrift_obj)}.")
        self._t_memory_buffer.clean()
        thrift_obj.write(self._t_proto)
        thrift_bytes = self._t_memory_buffer.getvalue()
        return thrift_bytes

    def from_bytes(self, thrift_bytes: typing.Union[bytes, str]):
        """Convert bytes into a thrift object."""
        if not isinstance(thrift_bytes, (bytes, str)):
            raise TypeError(f"Expected bytes but got {type(thrift_bytes)}.")
        self._t_memory_buffer.clean()
        self._t_memory_buffer.setvalue(thrift_bytes)
        thrift_obj = self.thrift_type()
        thrift_obj.read(self._t_proto)
        return thrift_obj


class Base64ReadWrite:
    def to_base64(self, obj: bytes) -> str:
        return base64.b64encode(obj).decode("utf-8")

    def from_base64(self, base64_str: str) -> bytes:
        return base64.b64decode(base64_str)
