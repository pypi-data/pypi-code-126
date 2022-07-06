from . import Message, Handler as Base
from .v1 import Ping, Pong

from bidict import bidict

from abc import ABC


class Labeled(Message, ABC):
    LABEL_SIZE_SIZE = 1 # bytes

    def __init__(self, label):
        super().__init__()
        self.label = label

    def __str__(self):
        return super().__str__() + f'[label={self.label}]'

    def send(self, handler):
        handler.sock.sendall(self.get_bytes_to_send(handler))

    def get_bytes_to_send(self, handler):
        label_bytes = self.label.encode(handler.ENCODING)
        size = len(label_bytes)
        assert size > 0 and size < 256**self.LABEL_SIZE_SIZE

        return size.to_bytes(self.LABEL_SIZE_SIZE, handler.BYTE_ORDER) \
            + label_bytes

    @classmethod
    def recv(cls, handler):
        return cls(cls.recv_label(handler))

    @classmethod
    def recv_label(cls, handler):
        size = handler.recv_bytes(cls.LABEL_SIZE_SIZE)
        if size is None: return None
        size = int.from_bytes(size, handler.BYTE_ORDER)
        assert size > 0

        label = handler.recv_bytes(size)
        if label is None: return None
        label = str(label, handler.ENCODING)

        return label


class Signed(Labeled, ABC):
    pass # FIXME


class SignOn(Signed):
    pass


class SignOff(Signed):
    pass


class LabelFind(Labeled):
    pass


class LabelNone(Labeled):
    pass


class LabelInfo(Labeled):
    HOST_SIZE_SIZE = 1 # bytes
    PORT_SIZE = 2 # bytes

    def __init__(self, label, host, port):
        super().__init__(label)
        self.host = host
        self.port = port

    def __str__(self):
        return self.__repr__() \
            + f'[label={self.label} host={self.host} port={self.port}]'

    def get_bytes_to_send(self, handler):
        label = super().get_bytes_to_send(handler)

        host_bytes = self.host.encode(handler.ENCODING)
        host_size = len(host_bytes)
        assert host_size > 0 and host_size < 256**self.HOST_SIZE_SIZE

        return label \
            + host_size.to_bytes(self.HOST_SIZE_SIZE, handler.BYTE_ORDER) \
            + host_bytes \
            + self.port.to_bytes(self.PORT_SIZE, handler.BYTE_ORDER)

    @classmethod
    def recv(cls, handler):
        label = cls.recv_label(handler)

        host_size = handler.recv_bytes(cls.HOST_SIZE_SIZE)
        if host_size is None: return None
        host_size = int.from_bytes(host_size, handler.BYTE_ORDER)
        assert host_size > 0

        host = handler.recv_bytes(host_size)
        if host is None: return None
        host = str(host, handler.ENCODING)

        port = handler.recv_bytes(cls.PORT_SIZE)
        if port is None: return None
        port = int.from_bytes(port, handler.BYTE_ORDER)

        return cls(label, host, port)


class Handler(Base):
    VERSION = 2

    ENCODING = 'utf-8'

    MSG_BY_ID = bidict({
        1: Ping,
        2: Pong,
        3: SignOn,
        4: SignOff,
        5: LabelFind,
        6: LabelNone,
        7: LabelInfo,
    })

    def server(self, master):
        while msg := self.recv():
            print(f'     {self.addr} -> {msg}')
            reply = None

            if isinstance(msg, Ping):
                reply = Pong(msg.nonce)

            elif isinstance(msg, SignOn):
                master.sign_on(self.sock, msg.label, self.addr)

            elif isinstance(msg, SignOff):
                master.sign_off(msg.label)

            elif isinstance(msg, LabelFind):
                if msg.label in master.labels:
                    host = master.labels[msg.label][0]
                    port = master.labels[msg.label][1]
                    reply = LabelInfo(msg.label, host, port)

                else:
                    reply = LabelNone(msg.label)

            else:
                raise ValueError(f'unhandled message: {msg}')

            if reply:
                print(f'     {self.addr} <- {reply}')
                self.send(reply)

