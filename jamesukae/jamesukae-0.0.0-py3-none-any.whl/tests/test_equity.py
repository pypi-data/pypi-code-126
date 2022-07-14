from typing import List

import pytest

from settrade.equity import MarketRepEquity
from settrade.errors import SettradeError
from settrade.user import InvestorEquity


class TestInvestorLogin:
    def test_success(self, e_investor: InvestorEquity):
        e_investor._ctx.login()


class TestInvestorGetOrders:
    def test_success(self, e_investor: InvestorEquity):
        e_investor._ctx.login()
        e_investor.get_orders()


class TestInvestorGetPortfolios:
    def test_success(self, e_investor: InvestorEquity):
        e_investor._ctx.login()
        e_investor.get_portfolios()


class TestInvestorGetTrades:
    def test_success(self, e_investor: InvestorEquity):
        e_investor._ctx.login()
        e_investor.get_trades()


class TestInvestorGetAccountInfo:
    def test_success(self, e_investor: InvestorEquity):
        e_investor._ctx.login()
        e_investor.get_account_info()


class TestInvestorPlaceOrder:
    def test_success(self, e_investor: InvestorEquity):
        e_investor._ctx.login()
        e_investor.place_order(
            side="Buy",
            bypass_warning=True,
            client_type="Corporate",
            pin="123457",
            price=60,
            price_type="Limit",
            qty_open=0,
            symbol="AOT",
            trustee_id_type="Local",
            valid_till_date="2022-06-01",
            validity_type="Day",
            volume=100,
        )

    def test_fail_symbol_not_found(self, e_investor: InvestorEquity):
        e_investor._ctx.login()
        with pytest.raises(SettradeError) as e:
            e_investor.place_order(
                side="Buy",
                bypass_warning=True,
                client_type="Corporate",
                pin="123457",
                price=700,
                price_type="Limit",
                qty_open=0,
                symbol="AAAAAAA",
                trustee_id_type="Local",
                valid_till_date="2022-06-01",
                validity_type="Day",
                volume=1,
            )
        assert e.value.status_code == 404


class TestMarketRepLogin:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()


class TestMarketRepGetAccountInfo:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()
        me_investor.get_account_info("FT0007EA")


class TestMarketrepGetOrder:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()
        me_investor.get_order("")


class TestMarketrepGetOrders:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()
        me_investor.get_orders()


class TestMarketrepGetOrderByAccountNo:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()
        me_investor.get_orders_by_account_no("FT0007EA")


class TestMarketrepGetPortfolios:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()
        me_investor.get_portfolios("FT0007EA")


class TestMarketrepGetTrades:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()
        me_investor.get_trades("FT0007EA")


class TestMarketrepPlaceOrder:
    def test_success(self, me_investor: MarketRepEquity):
        me_investor._ctx.login()
        me_investor.place_order(
            account_no="FT0007EA",
            bypass_warning=True,
            client_type="Corporate",
            price=60,
            price_type="Limit",
            qty_open=100,
            side="Buy",
            symbol="AOT",
            trustee_id_type="Local",
            valid_till_date="2022-06-02",
            validity_type="Day",
            volume=100,
        )


class TestMarketrepCancelOrder:
    def test_success(
        self, me_investor: MarketRepEquity, e_mkt_investor_place_order: dict
    ):
        me_investor._ctx.login()
        me_investor.cancel_order("FT0007EA", e_mkt_investor_place_order["orderNo"])


class TestMarketreCancelOrders:
    def test_success(
        self, me_investor: MarketRepEquity, e_mkt_investor_place_orders: List[dict]
    ):
        me_investor._ctx.login()
        order_number_l = [order["orderNo"] for order in e_mkt_investor_place_orders]
        me_investor.cancel_orders("FT0007EA", order_number_l)


class TestMarketrerepChangeOrders:
    def test_success(
        self,
        me_investor: MarketRepEquity,
        e_mkt_investor_place_order: dict,
        e_mkt_order_2: dict,
    ):
        me_investor._ctx.login()
        me_investor.change_order(
            account_no="FT0007EA",
            bypass_warning=e_mkt_order_2["bypass_warning"],
            new_iceberg_volume=None,
            new_price=e_mkt_order_2["price"],
            new_trustee_id_type=e_mkt_order_2["trustee_id_type"],
            new_volume=e_mkt_order_2["volume"],
            order_no=e_mkt_investor_place_order["orderNo"],
            new_account_no=None,
        )
