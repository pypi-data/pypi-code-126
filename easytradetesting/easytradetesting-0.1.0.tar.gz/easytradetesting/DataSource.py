import abc

from easytradesdk.entity.KlineInterval import KlineInterval
from easytradesdk.entity.Symbol import Symbol
from easytradesdk.entity.TC import TC


class DataSource(metaclass=abc.ABCMeta):

    @staticmethod
    def resolveKlineTableName(tc: TC, symbol: Symbol, interval: KlineInterval):
        return "easytrade_kline_" + tc.value.lower() + "_" + symbol.value.lower() + "_" + interval.value

    @staticmethod
    def resolveBackTestOrderTableName():
        return "easytrade_backtestorder"

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def createKlineTable(self, tc: TC, symbol: Symbol, interval: KlineInterval):
        pass

    @abc.abstractmethod
    def saveKline(self, tc: TC, symbol: Symbol, interval: KlineInterval, kline):
        pass

    @abc.abstractmethod
    def saveKlines(self, tc: TC, symbol: Symbol, interval: KlineInterval, klines):
        pass

    @abc.abstractmethod
    def queryKline(self, tc: TC, symbol: Symbol, interval: KlineInterval, startTimeMills=None, endTimeMills=None, limit=200):
        pass

    @abc.abstractmethod
    def queryLatestKline(self, tc: TC, symbol: Symbol, interval: KlineInterval, endTimeMills=None, limit=200):
        pass

    @abc.abstractmethod
    def countKline(self, tc: TC, symbol: Symbol, interval: KlineInterval, startTimeMills=None, endTimeMills=None):
        pass

    @abc.abstractmethod
    def createBackTestOrderTable(self):
        pass

    @abc.abstractmethod
    def saveBackTestOrder(self, backTestOrder):
        pass

    @abc.abstractmethod
    def saveBackTestOrders(self, backTestOrders):
        pass

    @abc.abstractmethod
    def getBackTestOrder(self, clientOrderId):
        pass

    @abc.abstractmethod
    def queryBackTestOrders(self, startTimeMills=None, endTimeMills=None, tc: TC = None, symbol: Symbol = None, limit=50):
        pass

    @abc.abstractmethod
    def truncateBackTestOrders(self):
        pass
