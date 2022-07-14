import requests

from .config import config
from .context import Context, Option
from .errors import InvalidEnvironmentError
from .util import response_to_dict


class MarketData:
    def __init__(self, context: Context):
        self._ctx = context

        if config["environment"] == "prod":
            self.market_url = "https://marketapi.settrade.com"
        elif config["environment"] == "uat":
            self.market_url = "https://marketapi-test.settrade.com"
        else:
            raise InvalidEnvironmentError()

    def get_candlestick(
        self,
        symbol: str,
        interval: str,
        limit: int,
        start: str,
        end: str,
        normalized: bool,
    ):
        raise NotImplementedError("Not implemented yet")

    def get_quote_stock(self, symbol: str):
        path = f"{self.market_url}/api/marketdata/v3/{self._ctx.broker_id}/stocks/{symbol}/quote"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_quote_symbol(self, symbol: str):
        path = f"{self._ctx.base_url}/api/marketdata/v3/{self._ctx.broker_id}/quote/{symbol}"
        response = self._ctx.dispatch(Option("GET", path))
        return response_to_dict(response)

    def get_quote_option(
        self,
        symbol: str,
        underlying_price: float,
        volatility: float,
        remain_day: float,
        interest_rate: float,
        dividend: float,
    ):
        path = f"{self._ctx.base_url}/api/marketdata/v3/{self._ctx.broker_id}/options/{symbol}/quote"
        params = {
            "underlyingPrice": underlying_price,
            "volatility": volatility,
            "remainDay": remain_day,
            "interestRate": interest_rate,
            "dividend": dividend,
        }
        response = self._ctx.dispatch(Option("GET", path, params=params))
        return response_to_dict(response)

    def get_series_option(
        self,
        symbol: str,
        underlying_price: float,
        volatility: float,
        remain_day: float,
        interest_rate: float,
        dividend: float,
    ):
        headers = {
            "Authorization": f"Bearer {self._ctx.token}",
            "User-Agent": "0",
        }
        path = f"{self._ctx.base_url}/api/marketdata/v3/{self._ctx.broker_id}/options/{symbol}/quote"
        response = requests.get(
            path,
            headers=headers,
            params={
                "underlyingPrice": underlying_price,
                "volatility": volatility,
                "remainDay": remain_day,
                "interestRate": interest_rate,
                "dividend": dividend,
            },
        )
        return response_to_dict(response)

    def get_quote_futures(self, symbol: str):
        headers = {
            "Authorization": f"Bearer {self._ctx.token}",
            "User-Agent": "0",
        }
        path = f"{self._ctx.base_url}/api/marketdata/v3/{self._ctx.broker_id}/futures/{symbol}/quote"
        response = requests.get(
            path,
            headers=headers,
        )
        return response_to_dict(response)

    def get_series_futures(self, underlying: str):
        headers = {
            "Authorization": f"Bearer {self._ctx.token}",
            "User-Agent": "0",
        }
        path = f"{self._ctx.base_url}/api/marketdata/v3/{self._ctx.broker_id}/futures/series/{underlying}"
        response = requests.get(
            path,
            headers=headers,
        )
        return response_to_dict(response)
