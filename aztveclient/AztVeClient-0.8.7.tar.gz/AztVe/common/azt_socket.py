#  =============================================================================
#  GNU Lesser General Public License (LGPL)
#
#  Copyright (c) 2022 Qujamlee from www.aztquant.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  =============================================================================
import socket
from .azt_errors import *

PACK_HEAD = b"aztquant"
PACK_HEAD_LEN = len(PACK_HEAD)
MSG_LEN_LEN = 1


class Socket:
    def __init__(self):
        self.__addr = None
        self.__socket = None
        self.__connected = False
        self.__closed = True

    def connect(self, addr: str, timeout=None):
        try:
            addr = addr.split(":")
        except AttributeError:
            return ArgsError("行情服务地址格式错误！")
            # raise Exception("行情服务地址格式错误！")
        if len(addr) != 2:
            return ArgsError("行情服务地址格式错误！")
        ip, port = addr
        try:
            port = int(port)
        except ValueError:
            return ArgsError("行情服务地址格式错误！")

        self.__addr = (ip, port)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if timeout is not None:
            self.__socket.settimeout(timeout)
        try:
            self.__socket.connect(self.__addr)
            self.set_connected()
            self.set_closed(False)
        except TimeoutError:
            if self.__socket:
                self.close()
            return ConnectedFailed

    def set_connected(self, flag=True):
        self.__connected = flag

    def is_connected(self):
        return self.__connected

    def set_closed(self, flag=True):
        self.__closed = flag

    def is_closed(self):
        return self.__closed

    def send(self, msg: str = None):
        if not self.__closed:
            msgbytes = bytes(msg)
            msgbyteslenstr = str(len(msgbytes))
            msgbyteslenlenstr = str(len(msgbyteslenstr))
            return self.__socket.send(
                PACK_HEAD + bytes(msgbyteslenlenstr, encoding="utf-8") + bytes(msgbyteslenstr,
                                                                               encoding="utf-8") + msgbytes)

    def recv(self):
        if self.__closed:
            return None
        try:
            pack_head_bytes = self.__socket.recv(PACK_HEAD_LEN)
            if pack_head_bytes != PACK_HEAD:
                return None
            msg_len_len_bytes = self.__socket.recv(MSG_LEN_LEN)
            msg_len_len = int(msg_len_len_bytes.decode("utf-8"))
            msg_len_bytes = self.__socket.recv(msg_len_len)
            msg_len = int(msg_len_bytes.decode("utf-8"))
            return self.__socket.recv(msg_len)
        except ConnectionAbortedError as e1:
            if self.__closed:
                return None
            raise e1
        except Exception as e2:
            raise e2

    def close(self):
        self.set_closed()
        self.set_connected(False)
        self.__socket.close()
