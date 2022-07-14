from settrade.market import MarketData


class TestGetQuoteStock:
    def test_success(self, market_data: MarketData):
        # login
        market_data._ctx.login()

        # test
        market_data.get_quote_stock("AOT")


class TestGetQuoteSymbol:
    def test_success(self, market_data: MarketData):
        # login
        market_data._ctx.login()

        # test
        market_data.get_quote_symbol("SA")


class TestGetQuoteOption:
    def test_success(self, market_data: MarketData):
        # login
        market_data._ctx.login()

        # test
        market_data.get_quote_option(
            symbol="SA",
            underlying_price=0,
            volatility=0,
            remain_day=0,
            interest_rate=0,
            dividend=0,
        )


class TestGetSeriesOption:
    def test_success(self, market_data: MarketData):
        # login
        market_data._ctx.login()

        # test
        market_data.get_series_option(
            symbol="SA",
            underlying_price=0,
            volatility=0,
            remain_day=0,
            interest_rate=0,
            dividend=0,
        )


class TestGetQuoteFutures:
    def test_success(self, market_data: MarketData):
        # login
        market_data._ctx.login()

        # test
        market_data.get_quote_futures("SA")


class TestGetSeriesFutures:
    def test_success(self, market_data: MarketData):
        # login
        market_data._ctx.login()

        # test
        market_data.get_series_futures("SA")
