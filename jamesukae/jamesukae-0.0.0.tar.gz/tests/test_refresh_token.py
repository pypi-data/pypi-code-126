import time

import pytest

from settrade.user import InvestorDerivatives


@pytest.mark.skip(reason="this test too long")
def test_context(d_investor: InvestorDerivatives):
    d_investor._ctx.login()
    for _ in range(4):
        d_investor._ctx.refresh()
        d_investor.get_account_info()
        time.sleep(60)
