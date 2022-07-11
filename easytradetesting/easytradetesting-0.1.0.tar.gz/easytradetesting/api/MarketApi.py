from easytradetesting.BackTestContext import BackTestContext
from easytradesdk.AbsMarketApi import AbsMarketApi
from easytradesdk.entity.KlineInterval import KlineInterval
from easytradesdk.entity.Symbol import Symbol
from easytradesdk.entity.TC import TC


class LocalMarketApi(AbsMarketApi):
    """
        数据 Api, 从本地获取 K 线数据
    """

    def __init__(self, backTestContext: BackTestContext):
        self.__backTestContext = backTestContext

    # 获取历史K线
    # [
    # {
    # 'timeMills': 1502942400000,
    # 'endTimeMills': 1502942459999,
    # 'startTime': '2017-08-17T04:00:00.000+00:00',
    # 'endTime': '2017-08-17T04:00:59.999+00:00',
    # 'openingPrice': '301.13',
    # 'closingPrice': '301.13',
    # 'highPrice': '301.13',
    # 'lowPrice': '301.13',
    # 'volume': '128.4108659',
    # 'quantity': '0.42643',
    # 'cnt': 2,
    # 'buyVolume': '128.4108659',
    # 'buyQuantity': '0.42643'
    # }
    # ]
    def fetchKline(self, tc: TC, symbol: Symbol, interval: KlineInterval, startTimeMills=None, endTimeMills=None, limit=200):
        """
            从本地数据库查询k线数据
            :param tc:              交易所
            :param symbol:          交易标的
            :param interval:        K线周期
            :param limit:           查询数量
            :param startTimeMills:  开始时间戳
            :param endTimeMills:    结束时间戳
            :return:
        """
        return self.__backTestContext.dataSource.queryKline(tc, symbol, interval, startTimeMills, endTimeMills, limit)

    # 获取历史k线
    # [
    # {
    # 'timeMills': 1502942400000,
    # 'endTimeMills': 1502942459999,
    # 'startTime': '2017-08-17T04:00:00.000+00:00',
    # 'endTime': '2017-08-17T04:00:59.999+00:00',
    # 'openingPrice': 301.13,
    # 'closingPrice': 301.13,
    # 'highPrice': 301.13,
    # 'lowPrice': 301.13,
    # 'volume': 128.4108659,
    # 'quantity': 0.42643,
    # 'cnt': 2,
    # 'buyVolume': 128.4108659,
    # 'buyQuantity': 0.42643
    # }
    # ]
    def fetchLatestKline(self, tc: TC, symbol: Symbol, interval: KlineInterval, endTimeMills=None, limit=200, excludeCurrent=0):
        """
            从本地数据库查询最近K线数据
            :param tc:              交易所
            :param symbol:          交易标的
            :param interval:        k线周期
            :param endTimeMills:    K线截止时间戳
            :param limit:           查询数量
            :param excludeCurrent:  如果设置为1, 则将最新的一条数据删除
            :return:
        """

        klines = self.__backTestContext.dataSource.queryLatestKline(tc, symbol, interval, endTimeMills, limit)

        if len(klines) > 0 and excludeCurrent == 1:
            del klines[len(klines) - 1]

        return klines

    def fetchDepth(self, tc: TC, symbol: Symbol, depthLimit=100):
        return None

    def fetchTicker(self, tc: TC, symbol: Symbol):
        return None
