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
from .quote_spi import QuoteSpi
from AztVe.common import SocketCls, logger
from AztVe import common
from AztVe.protobufs import Quote_Message_pb2 as MsgProto, UnitedMessage_pb2 as UnitMsgProto
from AztVe.structs import quote_spi_struct

import threading


class QuoteApiBase:
    spi = QuoteSpi()

    def __init__(self):
        self.__socket = SocketCls()

        self.__handle = threading.Thread(target=self.__report_recv)
        self.__handle.setDaemon(True)

    def __report_recv(self):
        while True:
            msg = self.__socket.recv()
            if msg is None:
                break
            # 解析msg
            repmsg = MsgProto.RepMessage()
            repmsg.ParseFromString(msg)
            self.__report_handel(repmsg)

    def __report_handel(self, repmsg):
        if repmsg.type == MsgProto.QuoteMsgID_Subscribe:
            codesproto = MsgProto.QuoteRegisterMsgs()
            repmsg.message.Unpack(codesproto)
            tickers = [ticker for ticker in codesproto.exchange_securitys]
            error = common.SubscribeError("Subscribe failed") if repmsg.status == MsgProto.Message_Err else None
            self.spi.onSubscribe(tickers, error)

        elif repmsg.type == MsgProto.QuoteMsgID_Unsubscribe:
            codesproto = MsgProto.QuoteRegisterMsgs()
            repmsg.message.Unpack(codesproto)
            tickers = [ticker for ticker in codesproto.exchange_securitys]
            error = common.UnsubscribeError(
                "Unsubscribe failed") if repmsg.status == MsgProto.Message_Err else None
            self.spi.onUnSubscribe(tickers, error)

        elif repmsg.type == MsgProto.QuoteMsgID_DepthMarketData:
            if repmsg.status == MsgProto.Message_Ok:
                unidataproto = UnitMsgProto.UnitedMessage()
                repmsg.message.Unpack(unidataproto)
                quote_msg = MsgProto.QuoteMsg()
                unidataproto.msg_body.Unpack(quote_msg)
                data = quote_spi_struct.QuoteStockMsg.__proto2py__(quote_msg)
                self.spi.onDepthMarketData(data, None)
            else:
                self.spi.onDepthMarketData(None, common.MarketDataError("Error DepthMarketData"))
        elif repmsg.type == MsgProto.QuoteMsgID_Disconnected:
            disconnected = MsgProto.DisconnectedStatus()
            repmsg.message.Unpack(disconnected)
            self.spi.onDisconnected(common.ConnectedBroken(disconnected.disconn))

    def _start(self, server_addr: str, spi=None, timeout=None):
        error = self.__socket.connect(server_addr, timeout)
        if not error:
            if spi.__class__ is type:
                spi = spi()
            self.spi = spi
            self.__handle.start()

        return error

    def _stop(self):
        return self.__socket.close()

    def _join(self, timeout=None):
        self.__handle.join(timeout=timeout)

    def _subscribe(self, codes):
        if self.__socket.is_closed():
            raise common.UnconnectedError("尚未连接行情服务器！")
        req = MsgProto.QuoteRegisterMsgs()
        req.exchange_securitys.extend(codes)
        req_msg = MsgProto.QuoteMsgType()
        req_msg.em = MsgProto.QuoteMsgID_Subscribe
        req_msg.message.Pack(req)
        return self.__socket.send(req_msg.SerializeToString())

    def _unsubscribe(self, codes):
        if self.__socket.is_closed():
            raise common.UnconnectedError("尚未连接行情服务器！")
        req = MsgProto.QuoteRegisterMsgs()
        req.exchange_securitys.extend(codes)
        req_msg = MsgProto.QuoteMsgType()
        req_msg.em = MsgProto.QuoteMsgID_Unsubscribe
        req_msg.message.Pack(req)
        return self.__socket.send(req_msg.SerializeToString())
