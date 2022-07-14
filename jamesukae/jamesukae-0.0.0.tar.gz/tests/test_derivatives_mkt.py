from settrade.user import MarketRepDerivatives
from tests.conftest import D_INV_ACCOUNT_NO


class TestGetAccountInfo:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        result = d_market_rep.get_account_info(D_INV_ACCOUNT_NO)

        assert "creditLine" in result, result
        assert "excessEquity" in result, result
        assert "cashBalance" in result, result
        assert "equity" in result, result
        assert "totalMR" in result, result
        assert "totalMM" in result, result
        assert "callForceFlag" in result, result
        assert "callForceMargin" in result, result
        assert "liquidationValue" in result, result
        assert "callForceMarginMM" in result, result
        assert "initialMargin" in result, result
        assert "closingMethod" in result, result


class TestGetAccountInfoDetail:
    def test_success(self, d_market_rep: MarketRepDerivatives):

        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_account_info_detail(D_INV_ACCOUNT_NO)

        # check
        assert "creditLine" in result, result
        assert "excessEquity" in result, result
        assert "cashBalance" in result, result
        assert "equity" in result, result
        assert "totalMR" in result, result
        assert "totalMM" in result, result
        assert "callForceFlag" in result, result
        assert "callForceMargin" in result, result
        assert "liquidationValue" in result, result
        assert "callForceMarginMM" in result, result
        assert "initialMargin" in result, result
        assert "closingMethod" in result, result
        assert "creditLimit" in result, result
        assert "premiumToPay" in result, result
        assert "totalComm" in result, result
        assert "receivedPaymentAfterComm" in result, result
        assert "totalUnrealizedPL" in result, result
        assert "futureMTM" in result, result
        assert "optionsMTM" in result, result
        assert "currentNonCashCollateral" in result, result
        assert "nonCashCollateral" in result, result
        assert "commissionConfirmOrder" in result, result
        assert "commissionPendingOrder" in result, result
        assert "foreignCurrency" in result, result
        assert "depositWithdrawalNonCash" in result, result
        assert "startCashBalance" in result, result
        assert "startEquityBalance" in result, result
        assert "startCallForceFlag" in result, result
        assert "startCallForceMargin" in result, result
        assert "totalFM" in result, result
        assert "isMarkToMarket" in result, result
        assert "canOpen" in result, result
        assert "canClose" in result, result
        assert "previousFutureMTM" in result, result
        assert "marginMethod" in result, result
        assert "virtualMarginDisplay" in result, result
        assert "virtualMargin" in result, result
        assert "equityNonCash" in result, result
        assert "markToMarket" in result, result


class TestGetCommission:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_commission(D_INV_ACCOUNT_NO)

        # check
        assert "fixedComm" in result, result
        assert "percentComm" in result, result
        assert "fee" in result, result


class TestGetOrder:
    def test_success(self, d_market_rep: MarketRepDerivatives, d_place_order: dict):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_order(order_no=d_place_order["orderNo"])

        # check
        check_order(result)


class TestGetOrders:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_orders()

        # check
        assert isinstance(result, list), result
        for item in result:
            check_order(item)


class TestGetOrderByAccNo:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_orders_by_account_no(D_INV_ACCOUNT_NO)

        # check
        assert isinstance(result, list), result
        for item in result:
            check_order(item)


class TestGetPortfolios:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_portfolios(D_INV_ACCOUNT_NO)

        # check
        assert "portfolioList" in result, result
        assert isinstance(result["portfolioList"], list), result["portfolioList"]
        for item in result["portfolioList"]:
            assert "brokerId" in item, result
            assert "accountNo" in item, result
            assert "symbol" in item, result
            assert "underlying" in item, result
            assert "securityType" in item, result
            assert "lastTradingDate" in item, result
            assert "multiplier" in item, result
            assert "currency" in item, result
            assert "currentXRT" in item, result
            assert "asOfDateXRT" in item, result
            assert "hasLongPosition" in item, result
            assert "startLongPosition" in item, result
            assert "actualLongPosition" in item, result
            assert "availableLongPosition" in item, result
            assert "startLongPrice" in item, result
            assert "startLongCost" in item, result
            assert "longAvgPrice" in item, result
            assert "longAvgCost" in item, result
            assert "shortAvgCostTHB" in item, result
            assert "longAvgCostTHB" in item, result
            assert "openLongPosition" in item, result
            assert "closeLongPosition" in item, result
            assert "startXRTLong" in item, result
            assert "startXRTLongCost" in item, result
            assert "avgXRTLong" in item, result
            assert "avgXRTLongCost" in item, result
            assert "hasShortPosition" in item, result
            assert "startShortPosition" in item, result
            assert "actualShortPosition" in item, result
            assert "availableShortPosition" in item, result
            assert "startShortPrice" in item, result
            assert "startShortCost" in item, result
            assert "shortAvgPrice" in item, result
            assert "shortAvgCost" in item, result
            assert "openShortPosition" in item, result
            assert "closeShortPosition" in item, result
            assert "startXRTShort" in item, result
            assert "avgXRTShort" in item, result
            assert "avgXRTShortCost" in item, result
            assert "marketPrice" in item, result
            assert "realizedPL" in item, result
            assert "realizedPLByCost" in item, result
            assert "realizedPLCurrency" in item, result
            assert "realizedPLByCostCurrency" in item, result
            assert "shortAmount" in item, result
            assert "longAmount" in item, result
            assert "shortAmountByCost" in item, result
            assert "longAmountByCost" in item, result
            assert "priceDigit" in item, result
            assert "settleDigit" in item, result
            assert "longUnrealizePL" in item, result
            assert "longUnrealizePLByCost" in item, result
            assert "longPercentUnrealizePL" in item, result
            assert "longPercentUnrealizePLByCost" in item, result
            assert "longOptionsValue" in item, result
            assert "longMarketValue" in item, result
            assert "shortUnrealizePL" in item, result
            assert "shortPercentUnrealizePL" in item, result
            assert "shortUnrealizePLByCost" in item, result
            assert "shortPercentUnrealizePLByCost" in item, result
            assert "shortOptionsValue" in item, result
            assert "shortMarketValue" in item, result
            assert "longAvgPriceTHB" in item, result
            assert "shortAvgPriceTHB" in item, result
        # check Total port
        assert "totalPortfolio" in result, result
        assert "amount" in result["totalPortfolio"], result
        assert "marketValue" in result["totalPortfolio"], result
        assert "amountByCost" in result["totalPortfolio"], result
        assert "unrealizePL" in result["totalPortfolio"], result
        assert "unrealizePLByCost" in result["totalPortfolio"], result
        assert "realizePL" in result["totalPortfolio"], result
        assert "realizePLByCost" in result["totalPortfolio"], result
        assert "percentUnrealizePL" in result["totalPortfolio"], result
        assert "percentUnrealizePLByCost" in result["totalPortfolio"], result["data"]
        assert "optionsValue" in result["totalPortfolio"], result


class TestGetTrades:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_trades(D_INV_ACCOUNT_NO)

        # check
        assert isinstance(result, list), result
        for item in result:
            assert "brokerId" in item, result
            assert "orderNo" in item, result
            assert "tradeDate" in item, result
            assert "entryId" in item, result
            assert "accountNo" in item, result
            assert "tradeNo" in item, result
            assert "tradeId" in item, result
            assert "tradeTime" in item, result
            assert "symbol" in item, result
            assert "side" in item, result
            assert "qty" in item, result
            assert "px" in item, result
            assert "openClose" in item, result
            assert "status" in item, result
            assert "tradeType" in item, result
            assert "rectifiedQty" in item, result
            assert "multiplier" in item, result
            assert "currency" in item, result
            assert "ledgerDate" in item, result
            assert "ledgerSeq" in item, result
            assert "ledgerTime" in item, result
            assert "refLedgerDate" in item, result
            assert "refLedgerSeq" in item, result
            assert "rejectCode" in item, result
            assert "rejectReason" in item, result


class TestGetTradeSummaries:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.get_trade_summaries(D_INV_ACCOUNT_NO)

        # check
        assert isinstance(result, list), result
        for item in result:
            assert "orderNo" in item, result
            assert "tradeDate" in item, result
            assert "accountNo" in item, result
            assert "symbol" in item, result
            assert "side" in item, result
            assert "qty" in item, result
            assert "px" in item, result
            assert "settlementDate" in item, result
            assert "openClose" in item, result
            assert "totalCommission" in item, result
            assert "totalFee" in item, result
            assert "totalVat" in item, result
            assert "totalWHTax" in item, result
            assert "totalChargeAmount" in item, result


class TestPlaceOrder:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        # test
        result = d_market_rep.place_order(
            account_no=D_INV_ACCOUNT_NO,
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
        )

        # check
        check_order(result)


class TestPlaceOrders:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        orders = [
            {
                "symbol": "S50H23",
                "side": "Long",
                "position": "Open",
                "priceType": "Limit",
                "price": 900,
                "volume": 1,
                "icebergVol": 0,
                "validityType": "Day",
                "validityDateCondition": None,
                "stopCondition": None,
                "stopSymbol": None,
                "stopPrice": None,
                "triggerSession": None,
                "bypassWarning": True,
            },
            {
                "symbol": "S50H23",
                "side": "Long",
                "position": "Open",
                "priceType": "Limit",
                "price": 910,
                "volume": 1,
                "icebergVol": 0,
                "validityType": "Day",
                "validityDateCondition": None,
                "stopCondition": None,
                "stopSymbol": None,
                "stopPrice": None,
                "triggerSession": None,
                "bypassWarning": True,
            },
        ]

        result = d_market_rep.place_orders(
            account_no=D_INV_ACCOUNT_NO,
            order_list=orders,
        )

        # check
        assert "results" in result, result
        assert isinstance(result["results"], list), result
        for item in result["results"]:
            assert "order" in item, result
            assert "httpStatusCode" in item, result
            check_order(item["order"])


class TestChangeOrder:
    def test_success(self, d_market_rep: MarketRepDerivatives, d_place_order: dict):
        # login
        d_market_rep._ctx.login()

        d_market_rep.change_order(
            account_no=D_INV_ACCOUNT_NO,
            order_no=d_place_order["orderNo"],
            new_price=910,
            new_volume=3,
            bypass_warning=False,
            new_account_no=None,
        )


class TestCancelOrder:
    def test_success(self, d_market_rep: MarketRepDerivatives, d_place_order: dict):
        # login
        d_market_rep._ctx.login()

        d_market_rep.cancel_order(
            account_no=D_INV_ACCOUNT_NO,
            order_no=d_place_order["orderNo"],
        )


class TestCancelOrders:
    def test_success(self, d_market_rep: MarketRepDerivatives, d_place_order: dict):
        # login
        d_market_rep._ctx.login()

        result = d_market_rep.cancel_orders(
            account_no=D_INV_ACCOUNT_NO,
            order_no_list=[d_place_order["orderNo"]],
        )

        # check
        assert isinstance(result["results"], list), result
        for item in result["results"]:
            assert "orderNo" in item, result


class TestPlaceTradeReport:
    def test_success(self, d_market_rep: MarketRepDerivatives):
        # login
        d_market_rep._ctx.login()

        result = d_market_rep.place_trade_report(
            buyer=D_INV_ACCOUNT_NO,
            seller=None,
            symbol="S50H23",
            position="Open",
            price=900.9,
            volume=200,
            cpm="00TH",
            ty_type="TX SET50 Futures",
            control_key="A1",
        )

        # check
        assert isinstance(result, list), result


def check_order(order: dict):
    assert "orderNo" in order, order
    assert "tfxOrderNo" in order, order
    assert "accountNo" in order, order
    assert "entryId" in order, order
    assert "entryTime" in order, order
    assert "tradeDate" in order, order
    assert "transactionTime" in order, order
    assert "cancelId" in order, order
    assert "cancelTime" in order, order
    assert "symbol" in order, order
    assert "side" in order, order
    assert "position" in order, order
    assert "priceType" in order, order
    assert "price" in order, order
    assert "qty" in order, order
    assert "icebergVol" in order, order
    assert "balanceQty" in order, order
    assert "matchQty" in order, order
    assert "cancelQty" in order, order
    assert "validity" in order, order
    assert "validToDate" in order, order
    assert "isStopOrderNotActivate" in order, order
    assert "triggerCondition" in order, order
    assert "triggerSymbol" in order, order
    assert "triggerPrice" in order, order
    assert "triggerSession" in order, order
    assert "status" in order, order
    assert "showStatus" in order, order
    assert "statusMeaning" in order, order
    assert "rejectCode" in order, order
    assert "rejectReason" in order, order
    assert "cpm" in order, order
    assert "trType" in order, order
    assert "terminalType" in order, order
    assert "version" in order, order
    assert "canCancel" in order, order
    assert "canChange" in order, order
    assert "priceDigit" in order, order
