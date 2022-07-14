import time
from unittest.mock import Mock

from requests import Response

from settrade.context import RateLimit


class TestUpdate:
    def test_update_no_header(self):
        r = RateLimit()
        r.update(response=None)
        assert r.remaining_per_second == 5, r
        assert r.remaining_per_minute == 60, r

    def test_update_has_header(self):
        r = RateLimit()
        res = Response()
        res.headers["X-RateLimit-Remaining-second"] = "1"
        res.headers["X-RateLimit-Remaining-minute"] = "1"
        res.headers["X-RateLimit-Limit-second"] = "1"
        res.headers["X-RateLimit-Limit-minute"] = "2"

        r.update(response=res)

        assert r.remaining_per_second == 1, r
        assert r.remaining_per_minute == 1, r
        assert r.rate_per_second == 1, r
        assert r.rate_per_minute == 2, r


class TestResetRemaining:
    def test_reset_remaining_success(self):
        r = RateLimit()
        r.reset_remaining()
        assert r.remaining_per_second == 5, r
        assert r.remaining_per_minute == 60, r


class TestIsDifferenceBlock:
    def test_is_difference_block_base_case(self):
        r = RateLimit()
        assert r.is_difference_block(60 * 1000), r

    def test_is_difference_block_case_false(self):
        r = RateLimit()
        r.last_request_at = r.now() - 50
        assert not r.is_difference_block(60 * 1000), r

    def test_is_difference_block_case_true(self):
        r = RateLimit()
        r.last_request_at = r.now() - 70 * 1000
        assert r.is_difference_block(60 * 1000), r


class TestTimeUntilNextBlock:
    def setup_method(self, method):
        self.now = RateLimit.now
        RateLimit.now = Mock(return_value=99)

    def teardown_method(self, method):
        RateLimit.now = self.now

    def test_base_case(self):
        r = RateLimit()
        assert r.time_until_next_block(2) == 0, r

    def test_next_box(self):
        r = RateLimit()
        r.last_request_at = 95
        assert r.time_until_next_block(20) == 1, r


class TestWait:
    def setup_method(self, method):
        self.sleep = time.sleep
        time.sleep = Mock()

    def teardown_method(self, method):
        time.sleep = self.sleep

    def test_case_no_wait(self):
        r = RateLimit()
        r.wait()
        time.sleep.assert_not_called()

    def test_case_wait(self):
        r = RateLimit()
        r.remaining_per_minute = 0
        r.last_request_at = r.now()
        r.wait()
        time.sleep.assert_called_once()

    def test_case_has_remaining_but_diff_block(self):
        r = RateLimit()
        r.remaining_per_second = 0
        r.last_request_at = r.now() - 1 * 1500
        r.wait()
        time.sleep.assert_not_called()
