from .context import Context
from .derivatives import InvestorDerivatives, MarketRepDerivatives
from .equity import InvestorEquity, MarketRepEquity
from .market import MarketData
from .realtime import RealtimeDataConnection


class _BaseUser:
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        broker_id: str,
        app_code: str,
        is_auto_queue: bool = False,
    ):
        self._api_key = api_key
        self._api_secret = api_secret
        self._broker_id = broker_id
        self._app_code = app_code
        self._is_auto_queue = is_auto_queue
        self._ctx = Context(
            api_key=api_key,
            api_secret=api_secret,
            app_code=app_code,
            auto_queue=is_auto_queue,
            broker_id=broker_id,
        )
        self._ctx.login()

    def MarketData(self):
        return MarketData(self._ctx)

    def RealtimeDataConnection(self):
        return RealtimeDataConnection(self._ctx)


class Investor(_BaseUser):
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        broker_id: str,
        app_code: str,
        is_auto_queue: bool = False,
    ):
        super().__init__(
            api_key=api_key,
            api_secret=api_secret,
            broker_id=broker_id,
            app_code=app_code,
            is_auto_queue=is_auto_queue,
        )

    def Derivatives(self, account_no: str):
        return InvestorDerivatives(self._ctx, account_no)

    def Equity(self, account_no: str):
        return InvestorEquity(self._ctx, account_no)


class MarketRep(_BaseUser):
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        broker_id: str,
        app_code: str,
        is_auto_queue: bool = False,
    ):
        super().__init__(
            api_key=api_key,
            api_secret=api_secret,
            broker_id=broker_id,
            app_code=app_code,
            is_auto_queue=is_auto_queue,
        )

    def Derivatives(self):
        return MarketRepDerivatives(self._ctx)

    def Equity(self):
        return MarketRepEquity(self._ctx)
