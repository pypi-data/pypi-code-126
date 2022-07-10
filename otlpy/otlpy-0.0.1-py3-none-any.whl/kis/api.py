from base64 import b64decode
from typing import Any, Optional

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from httpx import AsyncClient, codes
from loguru import logger

from otlpy.base.settings import BaseSettings


class Settings(BaseSettings):
    kis_app_authorization: str
    kis_app_debug: bool
    kis_app_real: bool
    kis_app_key: str
    kis_app_secret: str
    kis_account_htsid: str
    kis_account_custtype: str
    kis_account_cano_domestic_stock: Optional[str]
    kis_account_prdt_domestic_stock: Optional[str]
    kis_account_cano_domestic_futureoption: Optional[str]
    kis_account_prdt_domestic_futureoption: Optional[str]
    kis_account_cano_overseas_stock: Optional[str]
    kis_account_prdt_overseas_stock: Optional[str]


def aes_cbc_base64_dec(key: str, iv: str, cipher_text: str) -> str:
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    return bytes.decode(
        unpad(cipher.decrypt(b64decode(cipher_text)), AES.block_size)
    )


class API:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        if settings.kis_app_real:
            self.url_base = "https://openapi.koreainvestment.com:9443"
            self.url_ws = "ws://ops.koreainvestment.com:21000"
        else:
            self.url_base = "https://openapivts.koreainvestment.com:29443"
            self.url_ws = "ws://ops.koreainvestment.com:31000"
        self.authorization = settings.kis_app_authorization
        self.content_type = "application/json; charset=UTF-8"

    def _headers1(self) -> dict[str, str]:
        return {
            "content-type": self.content_type,
        }

    def _headers3(self) -> dict[str, str]:
        return {
            "content-type": self.content_type,
            "appkey": self.settings.kis_app_key,
            "appsecret": self.settings.kis_app_secret,
        }

    def _headers4(self) -> dict[str, str]:
        return {
            "content-type": self.content_type,
            "appkey": self.settings.kis_app_key,
            "appsecret": self.settings.kis_app_secret,
            "authorization": self.authorization,
        }

    async def _post(
        self,
        client: AsyncClient,
        url_path: str,
        headers: dict[str, Any],
        data: dict[str, Any],
        debug: bool = True,
    ) -> Any:
        response = await client.post(
            "%s%s" % (self.url_base, url_path),
            headers=headers,
            json=data,
        )
        if response.status_code == codes.OK:
            response_data = response.json()
            if debug and self.settings.kis_app_debug:
                logger.debug("\n%s\n%s\n%s" % (url_path, data, response_data))
            return response_data

        logger.error(response)
        return {}

    async def _hash(self, client: AsyncClient, data: Any) -> str:
        url_path = "/uapi/hashkey"
        headers = self._headers3()
        response_data = await self._post(
            client, url_path, headers, data, False
        )
        return str(response_data["HASH"])

    async def token(self) -> None:
        async with AsyncClient(timeout=None) as client:
            url_path = "/oauth2/tokenP"
            headers = self._headers1()
            data = {
                "grant_type": "client_credentials",
                "appkey": self.settings.kis_app_key,
                "appsecret": self.settings.kis_app_secret,
            }
            response_data = await self._post(
                client, url_path, headers, data, False
            )
            self.authorization = "%s %s" % (
                response_data["token_type"],
                response_data["access_token"],
            )
            logger.info(self.authorization)

    async def domestic_stock_create_market_order(
        self, ticker: str, order_side: str, amount: int
    ) -> Any:
        order_type = "01"
        price = 0
        return await self.domestic_stock_create_order(
            ticker, order_type, order_side, amount, price
        )

    async def domestic_stock_create_market_buy_order(
        self, ticker: str, amount: int
    ) -> Any:
        if self.settings.kis_app_real:
            order_side = "TTTC0802U"
        else:
            order_side = "VTTC0802U"
        return await self.domestic_stock_create_market_order(
            ticker, order_side, amount
        )

    async def domestic_stock_create_market_sell_order(
        self, ticker: str, amount: int
    ) -> Any:
        if self.settings.kis_app_real:
            order_side = "TTTC0801U"
        else:
            order_side = "VTTC0801U"
        return await self.domestic_stock_create_market_order(
            ticker, order_side, amount
        )

    async def domestic_stock_create_limit_order(
        self, ticker: str, order_side: str, amount: int, price: int
    ) -> Any:
        order_type = "00"
        return await self.domestic_stock_create_order(
            ticker, order_type, order_side, amount, price
        )

    async def domestic_stock_create_limit_buy_order(
        self, ticker: str, amount: int, price: int
    ) -> Any:
        if self.settings.kis_app_real:
            order_side = "TTTC0802U"
        else:
            order_side = "VTTC0802U"
        return await self.domestic_stock_create_limit_order(
            ticker, order_side, amount, price
        )

    async def domestic_stock_create_limit_sell_order(
        self, ticker: str, amount: int, price: int
    ) -> Any:
        if self.settings.kis_app_real:
            order_side = "TTTC0801U"
        else:
            order_side = "VTTC0801U"
        return await self.domestic_stock_create_limit_order(
            ticker, order_side, amount, price
        )

    async def domestic_stock_create_order(
        self,
        ticker: str,
        order_type: str,
        order_side: str,
        amount: int,
        price: int,
    ) -> Any:
        async with AsyncClient(timeout=None) as client:
            url_path = "/uapi/domestic-stock/v1/trading/order-cash"
            data = {
                "CANO": self.settings.kis_account_cano_domestic_stock,
                "ACNT_PRDT_CD": self.settings.kis_account_prdt_domestic_stock,
                "PDNO": ticker,
                "ORD_DVSN": order_type,
                "ORD_QTY": str(int(amount)),
                "ORD_UNPR": str(int(price)),
            }
            headers = {
                **self._headers4(),
                "tr_id": order_side,
                "custtype": self.settings.kis_account_custtype,
                "hashkey": await self._hash(client, data),
            }
            response_data = await self._post(client, url_path, headers, data)
            return response_data

    def ws_senddata(self, subscribe: bool, tr_id: str, tr_key: str) -> str:
        if subscribe:
            tr_type = "1"
        else:
            tr_type = "2"
        return (
            '{"header":{"appkey":"'
            + self.settings.kis_app_key
            + '","appsecret":"'
            + self.settings.kis_app_secret
            + '","custtype":"'
            + self.settings.kis_account_custtype
            + '","tr_type":"'
            + tr_type
            + '","content-type":"utf-8"},"body":{"input":{"tr_id":"'
            + tr_id
            + '","tr_key":"'
            + tr_key
            + '"}}}'
        )

    def ws_domestic_stock_trade(
        self, ticker: str, subscribe: bool = True
    ) -> str:
        return self.ws_senddata(subscribe, "H0STCNT0", ticker)

    def ws_domestic_stock_orderbook(
        self, ticker: str, subscribe: bool = True
    ) -> str:
        return self.ws_senddata(subscribe, "H0STASP0", ticker)

    def ws_domestic_stock_execution(self, subscribe: bool = True) -> str:
        return self.ws_senddata(
            subscribe, "H0STCNI0", self.settings.kis_account_htsid
        )
