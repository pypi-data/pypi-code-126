import pytest

from settrade.derivatives import InvestorDerivatives
from settrade.errors import SettradeError


# derivative ...
class TestAutoQueueGetAccountInfo:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_account_info()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(20):
            d_investor_auto_queue.get_account_info()


class TestAutoQueueGetAccountInfoDetail:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_account_info_detail()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(20):
            d_investor_auto_queue.get_account_info_detail()


class TestAutoQueueGetCommission:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_commission()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(20):
            d_investor_auto_queue.get_commission()


class TestAutoQueueGetOrder:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_orders()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(20):
            d_investor_auto_queue.get_orders()


class TestAutoQueueGetPortfolios:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_portfolios()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(20):
            d_investor_auto_queue.get_portfolios()


class TestAutoQueueGetTrades:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_trades()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(20):
            d_investor_auto_queue.get_trades()


class TestAutoQueueGetSummaries:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_trade_summaries()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(20):
            d_investor_auto_queue.get_trade_summaries()


class TestAutoQueuePlaceOrderAndCancelOrder:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(40):
            result = d_investor_auto_queue.place_order(
                symbol="S50H23",
                side="Long",
                position="Open",
                price_type="Limit",
                price=750,
                volume=1,
                iceberg_vol=0,
                validity_type="Day",
                validity_date_condition=None,
                stop_condition=None,
                stop_symbol=None,
                stop_price=None,
                trigger_session=None,
                bypass_warning=True,
                pin="123457",
            )
            orderNo = str(result["orderNo"])
            result = d_investor_auto_queue.cancel_order(orderNo, "123457")


class TestAutoQueuePlaceOrders:
    def test_success_min(
        self, d_investor_auto_queue: InvestorDerivatives, d_inv_order_1: dict
    ):
        d_investor_auto_queue._ctx.login()
        order_l = [d_inv_order_1]
        d_investor_auto_queue.place_orders(pin="123457", order_list=order_l * 1)

    def test_success_max(
        self, d_investor_auto_queue: InvestorDerivatives, d_inv_order_1: dict
    ):
        d_investor_auto_queue._ctx.login()
        order_l = [d_inv_order_1]
        d_investor_auto_queue.place_orders(pin="123457", order_list=order_l * 50)

    def test_fail_empty(
        self, d_investor_auto_queue: InvestorDerivatives, d_inv_order_1: dict
    ):
        d_investor_auto_queue._ctx.login()
        order_l = []
        with pytest.raises(SettradeError) as e:
            d_investor_auto_queue.place_orders(pin="123457", order_list=order_l)
        assert e.value.status_code == 400

    def test_fail_overload(
        self, d_investor_auto_queue: InvestorDerivatives, d_inv_order_1: dict
    ):
        d_investor_auto_queue._ctx.login()
        order_l = [d_inv_order_1]
        with pytest.raises(SettradeError) as e:
            d_investor_auto_queue.place_orders(pin="123457", order_list=order_l * 100)
        assert e.value.status_code == 400

    def test_success_queue(
        self, d_investor_auto_queue: InvestorDerivatives, d_inv_order_1: dict
    ):
        d_investor_auto_queue._ctx.login()
        order_l = [d_inv_order_1]
        for _ in range(70):
            d_investor_auto_queue.place_orders(pin="123457", order_list=order_l * 1)


class TestAutoQueueCancelOrders:
    def test_success(
        self,
        d_investor_auto_queue: InvestorDerivatives,
        d_investor_auto_queue_place_orders: dict,
    ):
        d_investor_auto_queue._ctx.login()

        orders = d_investor_auto_queue_place_orders["results"]
        for order in orders:
            orderNo = order["order"]["orderNo"]
            d_investor_auto_queue.cancel_order(str(orderNo), "123457")

    def test_fail(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()

        with pytest.raises(SettradeError) as e:
            d_investor_auto_queue.cancel_order(str(""), "123457")
        assert e.value.status_code == 400

    def test_fail_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()

        for _ in range(150):
            with pytest.raises(SettradeError) as e:
                d_investor_auto_queue.cancel_order(str(""), "123457")
            assert e.value.status_code == 400


class TestAutoQueueGets:
    def test_success(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        d_investor_auto_queue.get_account_info()
        d_investor_auto_queue.get_account_info_detail()
        d_investor_auto_queue.get_portfolios()
        d_investor_auto_queue.get_trade_summaries()
        d_investor_auto_queue.get_commission()
        d_investor_auto_queue.get_orders()
        d_investor_auto_queue.get_trades()

    def test_success_queue(self, d_investor_auto_queue: InvestorDerivatives):
        d_investor_auto_queue._ctx.login()
        for _ in range(10):
            d_investor_auto_queue.get_account_info()
            d_investor_auto_queue.get_account_info_detail()
            d_investor_auto_queue.get_portfolios()
            d_investor_auto_queue.get_trade_summaries()
            d_investor_auto_queue.get_commission()
            d_investor_auto_queue.get_orders()
            d_investor_auto_queue.get_trades()


class TestAutoQueueCrossMethod:
    def test_success_1(
        self,
        d_investor_auto_queue: InvestorDerivatives,
        d_investor_auto_queue_place_orders: dict,
    ):
        orders = d_investor_auto_queue_place_orders["results"]
        for order in orders:
            orderNo = order["order"]["orderNo"]
            d_investor_auto_queue.cancel_order(str(orderNo), "123457")
            d_investor_auto_queue.get_account_info()
