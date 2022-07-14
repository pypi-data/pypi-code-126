import pytest

from settrade.context import Context
from settrade.errors import SettradeError
from settrade.realtime import RealtimeDataConnection


class TestLogin:
    def test_success(self):
        ctx = Context(
            broker_id="041",
            app_code="ALGO",
            api_key="z6XAEdzJr7vrgG1a",
            api_secret="APYMJFceZ7MaZ22LNIJKelBfblV216Y73yfIMkm1nE3b",
        )
        ctx.login()

    def test_fail(self):
        ctx = Context(
            broker_id="041",
            app_code="ALGO",
            api_key="z6XAEdzJr7vrgG1a",
            api_secret="APYMJFceZ7MaZ22LNIJKelBfblV216Y73yfIMkm1nE3a",
        )
        with pytest.raises(SettradeError) as e:
            ctx.login()
        assert e.value.status_code == 401
