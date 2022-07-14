from typing import List

import pytest

from settrade.context import Context
from settrade.equity import InvestorEquity, MarketRepEquity
from settrade.market import MarketData
from settrade.realtime import RealtimeDataConnection
from settrade.user import Investor, InvestorDerivatives, MarketRepDerivatives

BROKER_ID = "041"
D_INV_APP_CODE = "ALGO"
D_INV_API_KEY = "z6XAEdzJr7vrgG1a"
D_INV_API_SECRET = "APYMJFceZ7MaZ22LNIJKelBfblV216Y73yfIMkm1nE3b"
D_INV_ACCOUNT_NO = "FT0012D"
D_INV_PIN = "111111"

RT_CALLBACK_TYPES = [
    "on_message",
    "on_disconnect",
    "on_subscribe",
    "on_unsubscribe",
    "on_connect",
    "on_connect_fail",
    "on_log",
    "on_publish",
]

CALLBACK_DELAY = 5
MEMORY_USAGE_DELAY = 30

TOPIC_ERR = "$sys/u/_broker/_uref/error/subscribe"
TOPIC_PRICEINFO = "proto/topic/infov3/AOT"
TOPIC_1 = "topic1"
TOPIC_2 = "topic2"


SYMBOL_AOT = "AOT"
SYMBOL_TRUE = "TRUE"
SYMBOL_INVALID = "ZXCASDXZC"

ARG_1 = "arg1"
ARG_2 = "arg2"
KW_ARG_1 = "kwarg1"
KW_ARG_2 = "kwarg2"

INVALID_SYM = "__SYM__"
INVALID_DV_ACCOUNT_NO = "__FT0007D__"
INVALID_EQ_ACCOUNT_NO = "__FT0007E__"
INVALID_DV_MARKET = "__SET100__"
INVALID_EQ_MARKET = "__SET100__"


ERR_MES_DISCONNECT = {"is_success": False, "message": "disconnected with rc : 7"}


@pytest.fixture
def d_inv_order_1() -> dict:
    return {
        "symbol": "S50H23",
        "side": "Long",
        "position": "Open",
        "priceType": "Limit",
        "price": 750,
        "volume": 1,
        "icebergVol": 0,
        "validityType": "Day",
        "validityDateCondition": None,
        "stopCondition": None,
        "stopSymbol": None,
        "stopPrice": None,
        "triggerSession": None,
        "bypassWarning": True,
    }


@pytest.fixture
def e_mkt_order_1() -> dict:
    return {
        "account_no": "FT0007EA",
        "bypass_warning": True,
        "client_type": "Corporate",
        "price": 60,
        "price_type": "Limit",
        "qty_open": 100,
        "side": "Buy",
        "symbol": "AOT",
        "trustee_id_type": "Local",
        "valid_till_date": "2022-06-02",
        "validity_type": "Day",
        "volume": 100,
    }


@pytest.fixture
def e_mkt_order_2() -> dict:
    return {
        "account_no": "FT0007EA",
        "bypass_warning": True,
        "client_type": "Corporate",
        "price": 70,
        "price_type": "Limit",
        "qty_open": 200,
        "side": "Buy",
        "symbol": "AOT",
        "trustee_id_type": "Local",
        "valid_till_date": "2022-06-02",
        "validity_type": "Day",
        "volume": 200,
    }


@pytest.fixture
def make_order():
    def _make_order(price: float):
        return {
            "account_no": "FT0007EA",
            "bypass_warning": True,
            "client_type": "Corporate",
            "price": price,
            "price_type": "Limit",
            "qty_open": 200,
            "side": "Buy",
            "symbol": "AOT",
            "trustee_id_type": "Local",
            "valid_till_date": "2022-06-02",
            "validity_type": "Day",
            "volume": 200,
        }

    return _make_order


@pytest.fixture
def d_inv_context() -> Context:
    return Context(
        broker_id=BROKER_ID,
        app_code=D_INV_APP_CODE,
        api_key=D_INV_API_KEY,
        api_secret=D_INV_API_SECRET,
    )


@pytest.fixture
def context_auto_queue() -> Context:
    return Context(
        broker_id="041",
        app_code="ALGO",
        api_key="igXvDIp4WoHIyYs4",
        api_secret="AMrBoe8fq1/1x/DC7gA4/GlJ8FsMCGjbdAXZ26MIL6uS",
        auto_queue=True,
    )


@pytest.fixture
def context_equity_inv() -> Context:
    return Context(
        broker_id="041",
        app_code="ALGO",
        api_key="igXvDIp4WoHIyYs4",
        api_secret="AMrBoe8fq1/1x/DC7gA4/GlJ8FsMCGjbdAXZ26MIL6uS",
        auto_queue=True,
    )


@pytest.fixture
def context_equity_mkt() -> Context:
    return Context(
        broker_id="041",
        app_code="IC_ORDER",
        api_key="8O2sfRv3Tx29lEaQ",
        api_secret="ANHudrpQQeKrfPvzPrFNAABSjBSP5frfHNVRIhpT7rxF",
        auto_queue=True,
    )


@pytest.fixture
def context_realtime() -> Context:
    return Context(
        broker_id="041",
        app_code="ALGO",
        api_key="igXvDIp4WoHIyYs4",
        api_secret="AMrBoe8fq1/1x/DC7gA4/GlJ8FsMCGjbdAXZ26MIL6uS",
    )


@pytest.fixture
def investor_1() -> Investor:
    return Investor(
        broker_id="041",
        app_code="ALGO",
        api_key="igXvDIp4WoHIyYs4",
        api_secret="AMrBoe8fq1/1x/DC7gA4/GlJ8FsMCGjbdAXZ26MIL6uS",
    )


@pytest.fixture
def d_investor(d_inv_context: Context) -> InvestorDerivatives:
    return InvestorDerivatives(context=d_inv_context, account_no=D_INV_ACCOUNT_NO)


@pytest.fixture
def d_investor_acc_not_found(d_inv_context: Context) -> InvestorDerivatives:
    return InvestorDerivatives(context=d_inv_context, account_no="wrong_no")


@pytest.fixture
def d_investor_auto_queue(context_auto_queue: Context) -> InvestorDerivatives:
    return InvestorDerivatives(context=context_auto_queue, account_no="FT0007D")


@pytest.fixture
def e_investor(context_equity_inv: Context) -> InvestorEquity:
    return InvestorEquity(context=context_equity_inv, account_no="FT0007EA")


@pytest.fixture
def me_investor(context_equity_mkt: Context) -> MarketRepEquity:
    return MarketRepEquity(context=context_equity_mkt)


@pytest.fixture
def d_investor_auto_queue_place_orders(
    d_investor_auto_queue: InvestorDerivatives, d_inv_order_1: dict
) -> dict:
    d_investor_auto_queue._ctx.login()
    order_l = [d_inv_order_1]
    data = d_investor_auto_queue.place_orders(pin="123457", order_list=order_l * 50)

    return data


@pytest.fixture
def e_mkt_investor_place_order(
    me_investor: MarketRepEquity, e_mkt_order_1: dict
) -> dict:
    me_investor._ctx.login()
    data = me_investor.place_order(
        account_no=e_mkt_order_1["account_no"],
        bypass_warning=e_mkt_order_1["bypass_warning"],
        client_type=e_mkt_order_1["client_type"],
        price=e_mkt_order_1["price"],
        price_type=e_mkt_order_1["price_type"],
        qty_open=e_mkt_order_1["qty_open"],
        side=e_mkt_order_1["side"],
        symbol=e_mkt_order_1["symbol"],
        trustee_id_type=e_mkt_order_1["trustee_id_type"],
        valid_till_date=e_mkt_order_1["valid_till_date"],
        validity_type=e_mkt_order_1["validity_type"],
        volume=e_mkt_order_1["volume"],
    )

    return data


@pytest.fixture
def e_mkt_investor_place_orders(
    me_investor: MarketRepEquity, e_mkt_order_1: dict
) -> List[dict]:
    me_investor._ctx.login()
    results = []
    for _ in range(2):
        data = me_investor.place_order(
            account_no=e_mkt_order_1["account_no"],
            bypass_warning=e_mkt_order_1["bypass_warning"],
            client_type=e_mkt_order_1["client_type"],
            price=e_mkt_order_1["price"],
            price_type=e_mkt_order_1["price_type"],
            qty_open=e_mkt_order_1["qty_open"],
            side=e_mkt_order_1["side"],
            symbol=e_mkt_order_1["symbol"],
            trustee_id_type=e_mkt_order_1["trustee_id_type"],
            valid_till_date=e_mkt_order_1["valid_till_date"],
            validity_type=e_mkt_order_1["validity_type"],
            volume=e_mkt_order_1["volume"],
        )

        results.append(data)

    return results


@pytest.fixture
def market_data(context_equity_inv: Context) -> MarketData:
    return MarketData(context=context_equity_inv)


@pytest.fixture
def d_place_order(d_investor: InvestorDerivatives) -> dict:
    # login
    d_investor._ctx.login()

    result = d_investor.place_order(
        symbol="S50H23",
        side="Long",
        position="Open",
        price_type="Limit",
        price=900,
        volume=1,
        iceberg_vol=0,
        validity_type="Day",
        stop_condition=None,
        stop_price=None,
        stop_symbol=None,
        trigger_session=None,
        validity_date_condition=None,
        bypass_warning=True,
        pin=D_INV_PIN,
    )

    return result


# fintectm12
D_MKT_APP_CODE = "IC_ORDER"
D_MKT_API_KEY = "RyXKsbkpWB9CMGy7"
D_MKT_API_SECRET = "fe8JxkDcsOsRG+BgipOjQztMvYX+zTMmw5lByO4IIPE="


@pytest.fixture
def d_mkt_context() -> Context:
    return Context(
        broker_id=BROKER_ID,
        app_code=D_MKT_APP_CODE,
        api_key=D_MKT_API_KEY,
        api_secret=D_MKT_API_SECRET,
    )


@pytest.fixture
def d_market_rep(d_mkt_context: Context) -> MarketRepDerivatives:
    return MarketRepDerivatives(context=d_mkt_context)


@pytest.fixture
def rt(investor_1: Investor):
    rt = investor_1.RealtimeDataConnection()
    yield rt
    rt.stop()


@pytest.fixture
def rt_callback_type() -> List:
    return RT_CALLBACK_TYPES
