import abc

from easytradesdk.entity.Symbol import Symbol
from easytradesdk.entity.TC import TC


class AbsContext(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getPosition(self, tc, symbol):
        pass

    @abc.abstractmethod
    def getPositions(self):
        pass

    @abc.abstractmethod
    def getStrategyParams(self):
        pass

    @abc.abstractmethod
    def getExecuteInterval(self):
        pass

    @abc.abstractmethod
    def getExecutingTimeMills(self):
        pass

    @abc.abstractmethod
    def getMarketApi(self):
        pass

    @abc.abstractmethod
    def getTradeApi(self):
        pass

    @abc.abstractmethod
    def calculateMaxAvailableBuyQuantity(self, tc: TC, symbol: Symbol, amount=None, offsetPrice=None, scale=2):
        pass
