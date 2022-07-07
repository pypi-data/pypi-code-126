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

class TradeSpi:
    api = None

    def onHeartBeatStop(self):
        pass

    def onRegisterAccount(self, msg):
        pass

    def onLogin(self, msg):
        pass

    def onQueryAccountInfo(self, msg):
        pass

    def onDepositAsset(self, msg):
        pass

    def onQueryAsset(self, msg):
        pass

    def onQueryOrders(self, msg):
        pass

    def onQueryTrades(self, msg):
        pass

    def onQueryPositions(self, msg):
        pass

    def onQueryHistoryOrders(self, msg):
        pass

    def onQueryHistoryTrades(self, msg):
        pass

    def onOrderReport(self, msg):
        pass

    def onTradeReport(self, msg):
        pass

    def onCancelOrderReject(self, msg):
        pass

    def onQueryHistoryAsset(self, msg):
        pass

    def onQueryHistoryDeposit(self, msg):
        pass
