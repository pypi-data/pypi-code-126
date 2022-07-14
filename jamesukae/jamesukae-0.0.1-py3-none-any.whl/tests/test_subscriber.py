from sre_constants import CALL
from time import sleep
from unittest.mock import Mock

from settrade.context import Context
from settrade.realtime import RealtimeDataConnection
from tests.utils import getsize

CALLBACK_DELAY = 5
MEMORY_USAGE_DELAY = 30

TOPIC_ERR = "$sys/u/_broker/_uref/error/subscribe"
TOPIC_PRICEINFO = "proto/topic/infov3/AOT"
TOPIC_1 = "topic1"
TOPIC_2 = "topic2"


class TestNewSubscriber:
    def test_new_subscriber(self, rt: RealtimeDataConnection):
        s1 = rt.create_subscriber("topic1")
        s2 = rt.create_subscriber("topic2")
        c1 = rt.get_call_backer()
        c2 = rt.get_call_backer()

        assert id(c1) == id(c2)
        assert id(s1) != id(s2)


class TestAddRemoveCallback:
    def test_subscriber_hook_on_message(self, rt: RealtimeDataConnection):

        s1 = rt.create_subscriber("topic1")
        s2 = rt.create_subscriber("topic2")

        c = rt.get_call_backer()

        callback = Mock()
        callback1 = Mock()
        callback2 = Mock()

        s1.add_callback("on_message", callback)
        s1.add_callback("on_message", callback1)
        assert len(s1.callback_list) == 2

        s2.add_callback("on_message", callback)
        s2.add_callback("on_message", callback2)
        assert len(s2.callback_list) == 2

        assert len(c.callback_pool["on_message"]) == 0

        s1.stop()
        assert len(s1.callback_list) == 0

        s2.stop()
        assert len(s2.callback_list) == 0


class TestAddRemoveCallbackToCallbacker:
    def test_subscriber_hook_on_message_to_call_backer(
        self, rt: RealtimeDataConnection
    ):

        s1 = rt.create_subscriber("topic1")
        s2 = rt.create_subscriber("topic2")

        c = rt.get_call_backer()

        callback = Mock()
        callback1 = Mock()
        callback2 = Mock()

        s1.add_callback("on_message", callback)
        s1.add_callback("on_message", callback1)
        assert len(s1.callback_list) == 2

        s2.add_callback("on_message", callback)
        s2.add_callback("on_message", callback2)
        assert len(s2.callback_list) == 2

        assert len(c.callback_pool["on_message"]) == 0

        s1.start()
        assert len(c.callback_pool["on_message"]) == 2

        s2.start()
        assert len(c.callback_pool["on_message"]) == 4

        s1.stop()
        assert len(c.callback_pool["on_message"]) == 2
        assert len(s1.callback_list) == 0

        s2.stop()
        assert len(c.callback_pool["on_message"]) == 0
        assert len(s2.callback_list) == 0


class TestMemoryUsage:
    def test_initial(self, rt: RealtimeDataConnection):
        s1 = rt.create_subscriber("topic1")

        size_before = getsize(s1)

        sleep(MEMORY_USAGE_DELAY)

        size_after = getsize(s1)

        assert size_before == size_after
