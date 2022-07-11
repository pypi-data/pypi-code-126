import decimal
import traceback

from obspy import UTCDateTime

from easytradetesting.BackTestContext import BackTestContext
from easytradetesting.BackTestResult import BackTestResult
from easytradetesting.DataFetcher import DataFetcher
from easytradetesting.DataSource import DataSource
from easytradetesting.api.MarketApi import LocalMarketApi
from easytradetesting.api.TradeApi import TradeApi
from easytradesdk.entity.KlineInterval import KlineInterval
from easytradesdk.entity.Position import Position
from easytradesdk.entity.Slippage import Slippage
from easytradesdk.entity.Symbol import Symbol
from easytradesdk.entity.TC import TC


class BackTestEngine:

    def __init__(self, dataSource: DataSource, dataFetcher: DataFetcher, startDate: str, endDate: str):
        self.__dataSource = dataSource
        self.__startDate = startDate
        self.__endDate = endDate
        self.__startTimeMills = int(UTCDateTime.strptime(startDate + " 00:00:00", "%Y-%m-%d %H:%M:%S").timestamp) * 1000
        self.__endTimeStampMills = int(UTCDateTime.strptime(endDate + " 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp) * 1000
        self.__executeInstance = None
        self.__backTestContext = BackTestContext()
        self.__dataFetcher = dataFetcher

    def configKlines(self, tc: TC, symbol: Symbol, klineInterval: KlineInterval):

        """
            配置要回测的K线, 从行情API拉取放到本地数据库中，如果回测时间段的K线数量和行情API的一致，则不会再拉去数据。
            :param tc:      交易所
            :param symbol:  交易标的
            :param klineInterval: K线周期
            :return:
        """

        if tc is None or symbol is None:
            raise Exception("invalid params")

        _key = tc.value + ":" + symbol.value

        self.__dataSource.createKlineTable(tc, symbol, klineInterval)

        _remoteKlineCount = self.__dataFetcher.countKline(tc, symbol, klineInterval, self.__startTimeMills, self.__endTimeStampMills)
        _localKlineCount = self.__dataSource.countKline(tc, symbol, klineInterval, self.__startTimeMills, self.__endTimeStampMills)

        _startTimeMills = self.__startTimeMills

        if _remoteKlineCount == _localKlineCount:
            return self

        while True:

            _klines = self.__dataFetcher.fetchKline(tc, symbol, klineInterval, _startTimeMills, None, 200)

            _idx = -1

            for i, v in enumerate(_klines):

                if v.timeMills >= self.__endTimeStampMills:
                    _idx = i
                    break

            if _idx >= 0:
                _klines = _klines[0:_idx]

            for _kline in _klines:
                self.__dataSource.saveKline(tc, symbol, klineInterval, _kline)

            if len(_klines) < 200 or _idx >= 0:
                break

            _startTimeMills = _klines[len(_klines) - 1].endTimeMills

        return self

    def configPosition(self, tc: TC, symbol: Symbol, initialAmount=0, initialHolding=0):

        """
            配置仓位信息
            :param tc:              交易所
            :param symbol:          交易标的
            :param initialAmount:   初始金额
            :param initialHolding:  初始持仓
            :return:
        """

        if tc is None or symbol is None:
            raise Exception("invalid params")

        _key = tc.value + ":" + symbol.value
        _positions = self.__backTestContext.getPositions()

        if _key not in _positions:
            _position = Position()
            _position.tc = tc.value
            _position.symbol = symbol.value
            _position.initialAmount = decimal.Decimal(str(initialAmount))
            _position.initialHolding = decimal.Decimal(str(initialHolding))
            _position.remainAmount = decimal.Decimal(str(initialAmount))
            _position.remainHolding = decimal.Decimal(str(initialHolding))
            _positions[_key] = _position

        return self

    def configSlippage(self, side, slippageType, value):

        """
            交易滑点配置
            :param side:          buy or sell
            :param slippageType:  滑点类型，1: 百分比，2：具体数值
            :param value:
            :return:
        """
        if slippageType != 1 and slippageType != 2:
            raise Exception("invalid slippageType")

        if side == "buy":
            self.__backTestContext.buySlippage = Slippage(slippageType, value)
        elif side == "sell":
            self.__backTestContext.sellSlippage = Slippage(slippageType, value)

        return self

    def configStrategyParams(self, params: dict):

        """
            配置策略参数
            :param params:
            :return:
        """
        self.__backTestContext.setStrategyParams(params)

        return self

    def build(self, clazz, executeInterval, cleanBackTestOrders=True):

        self.__dataSource.createBackTestOrderTable()

        if cleanBackTestOrders:
            self.__dataSource.truncateBackTestOrders()

        _instance = clazz()
        _instance.context = self.__backTestContext
        self.__executeInstance = _instance

        self.__backTestContext.setMarketApi(LocalMarketApi(self.__backTestContext))
        self.__backTestContext.setTradeApi(TradeApi(self.__backTestContext))
        self.__backTestContext.setExecuteInterval(executeInterval)
        self.__backTestContext.dataSource = self.__dataSource

        _positions = self.__backTestContext.getPositions()

        for _position in _positions.values():

            _tc = TC.parse(_position.tc)
            _symbol = Symbol.parse(_position.symbol)

            _startKlines = self.__dataSource.queryKline(_tc, _symbol, KlineInterval.S_1m, startTimeMills=self.__startTimeMills, limit=1)
            _endKlines = self.__dataSource.queryLatestKline(_tc, _symbol, KlineInterval.S_1m, endTimeMills=self.__endTimeStampMills, limit=1)

            if not _startKlines:
                raise Exception("first kline from " + str(self.__startTimeMills) + " not found")
            if not _endKlines:
                raise Exception("last kline to " + str(self.__endTimeStampMills) + " not found")

            _position.initialTicker = _startKlines[0].openingPrice
            _position.initialTotalAmount = _position.initialAmount + _position.initialHolding * _position.initialTicker
            _position.lastTicker = _endKlines[0].closingPrice

        return self

    def execute(self):

        self.__executeInstance.init()

        _startTimeStamp = self.__startTimeMills
        _endTimeStamp = self.__endTimeStampMills
        _executeInterval = self.__backTestContext.getExecuteInterval()

        while True:
            try:
                self.__executeInstance.executeStopLoss()
            except Exception as e:
                traceback.print_exc()
            try:
                self.__executeInstance.executeStopProfit()
            except Exception as e:
                traceback.print_exc()
            try:
                self.__backTestContext.setExecutingTimeMills(_startTimeStamp)
                self.__executeInstance.execute()
            except Exception as e:
                traceback.print_exc()

            if _startTimeStamp >= _endTimeStamp:
                break
            else:
                _startTimeStamp = _startTimeStamp + self.resolveExecuteIntervalMills(_executeInterval)

        try:
            self.__executeInstance.destroy()
        except Exception as e:
            traceback.print_exc()

        # 生产回测结果
        _backTestResult = BackTestResult(
            self.__startDate, self.__endDate, self.__backTestContext.backTestOrders, self.__backTestContext.getPositions())

        return _backTestResult

    @staticmethod
    def resolveExecuteIntervalMills(executeInterval):

        _symbol = executeInterval[-1]
        _cnt = int(executeInterval[0:len(executeInterval) - 1])

        if _symbol == 'm':
            return _cnt * 60 * 1000

        if _symbol == 'h':
            return _cnt * 3600 * 1000

        if _symbol == 'd':
            return _cnt * 24 * 3600 * 1000

        raise Exception("invalid executeInterval")
