import pytest

try:
    import gevent
except ImportError:
    gevent = None
    from time import sleep as noncooperative_sleep

    cooperative_sleep = noncooperative_sleep
else:
    cooperative_sleep = gevent.sleep
    noncooperative_sleep = gevent.monkey.get_original("time", "sleep")

from ..concurrency.query_pool import CooperativeQueryPool, NonCooperativeQueryPool


def sleep(seconds, cooperative=True):
    print(f"sleep for {seconds} seconds ...")
    try:
        if cooperative:
            cooperative_sleep(seconds)
        else:
            noncooperative_sleep(seconds)
    except BaseException as e:
        print(f"sleep interrupted: {e}")
        raise
    print("sleep done")


@pytest.mark.parametrize("cooperative", [True, False])
@pytest.mark.skipif(gevent is None, reason="requires gevent for now")
def test_query_success(cooperative):
    """test executing a query which returns a value"""
    if cooperative:
        pool = CooperativeQueryPool(timeout=0.1)
    else:
        pool = NonCooperativeQueryPool(timeout=0.1)

    def myfunc(a, b=0):
        sleep(a + b, cooperative=cooperative)
        return True

    with gevent.Timeout(5):
        while not pool.execute(myfunc, args=(0.5,), kwargs={"b": 0.5}):
            pass  # every iteration waits for 0.1 seconds


@pytest.mark.parametrize("cooperative", [True, False])
@pytest.mark.skipif(gevent is None, reason="requires gevent for now")
def test_query_exception(cooperative):
    """test executing a query which raises an exception"""
    if cooperative:
        pool = CooperativeQueryPool(timeout=0.1)
    else:
        pool = NonCooperativeQueryPool(timeout=0.1)

    def myfunc(a, b=0):
        sleep(a + b, cooperative=cooperative)
        raise RuntimeError

    with gevent.Timeout(5):
        with pytest.raises(RuntimeError):
            while not pool.execute(myfunc, args=(0.5,), kwargs={"b": 0.5}):
                pass  # every iteration waits for 0.1 seconds


@pytest.mark.parametrize("cooperative", [True, False])
@pytest.mark.skipif(gevent is None, reason="requires gevent for now")
def test_query_wait(cooperative):
    """test executing a query which returns a value"""
    if cooperative:
        pool = CooperativeQueryPool(timeout=0.1)
    else:
        pool = NonCooperativeQueryPool(timeout=0.1)

    finished = False

    def myfunc():
        nonlocal finished
        sleep(1, cooperative=cooperative)
        finished = True

    pool.execute(myfunc)

    assert pool.wait(timeout=3), "query did not finish in time"

    assert finished, "query did not finish"


@pytest.mark.skipif(gevent is None, reason="requires gevent for now")
def test_query_cancel():
    """test canceling a query"""
    pool = CooperativeQueryPool(timeout=0.1)

    raised = False

    def myfunc():
        nonlocal raised
        try:
            sleep(2)
        except gevent.GreenletExit:
            raised = True
            raise

    pool.execute(myfunc)

    assert pool.cancel(timeout=3), "could not cancel the query in time"

    assert raised, "query was not cancelled"


@pytest.mark.parametrize("cooperative", [True, False])
@pytest.mark.skipif(gevent is None, reason="requires gevent for now")
def test_query_maxqueries(cooperative):
    """test executing a query which returns a value"""
    if cooperative:
        pool = CooperativeQueryPool(timeout=0.1, maxqueries=1)
    else:
        pool = NonCooperativeQueryPool(timeout=0.1, maxqueries=1)

    def myfunc(a, b=0):
        sleep(a + b, cooperative=cooperative)
        return True

    with gevent.Timeout(5):
        while not pool.execute(myfunc, args=(0.1,), kwargs={"b": 0.1}):
            pass  # every iteration waits for 0.1 seconds
        while not pool.execute(myfunc, args=(0.1,), kwargs={"b": 0.2}):
            pass  # every iteration waits for 0.1 seconds

    previous = pool.execute(myfunc, timeout=0, args=(0.1,), kwargs={"b": 0.2})
    missing = pool.execute(myfunc, timeout=0, args=(0.1,), kwargs={"b": 0.1})
    assert previous, "pool size not large enough"
    assert missing is None, "pool size too large"
    assert pool.wait(timeout=3)

    if cooperative:
        pool = CooperativeQueryPool(timeout=0.1, maxqueries=3)
    else:
        pool = NonCooperativeQueryPool(timeout=0.1, maxqueries=3)

    with gevent.Timeout(5):
        while not pool.execute(myfunc, args=(0.1,), kwargs={"b": 0.1}):
            pass  # every iteration waits for 0.1 seconds
        while not pool.execute(myfunc, args=(0.1,), kwargs={"b": 0.2}):
            pass  # every iteration waits for 0.1 seconds

    previous = pool.execute(myfunc, timeout=0, args=(0.1,), kwargs={"b": 0.2})
    assert previous, "pool size not large enough"
    previous = pool.execute(myfunc, timeout=0, args=(0.1,), kwargs={"b": 0.1})
    assert previous, "pool size not large enough"
    assert pool.wait(timeout=3)


@pytest.mark.skipif(gevent is None, reason="requires gevent for now")
def test_noncooperative_query_in_noncooperative_pool():
    """test executing a non-cooperative query in a non-cooperative pool (proper usage)"""
    pool = NonCooperativeQueryPool(timeout=0.1)

    call_count = 0

    def myfunc(**kw):
        nonlocal call_count
        call_count += 1
        if call_count > 1:
            # Note: this exception will also be printed when the test passed
            raise RuntimeError("the gevent loop was blocked")
        sleep(**kw)

    with pytest.raises(gevent.Timeout, match="the gevent loop was not blocked"):
        with gevent.Timeout(0.5, "the gevent loop was not blocked"):
            while not pool.execute(myfunc, kwargs={"seconds": 2, "cooperative": False}):
                pass  # every iteration waits for 0.1 seconds

    assert pool.wait(timeout=4)


@pytest.mark.skipif(gevent is None, reason="requires gevent for now")
def test_noncooperative_query_in_cooperative_pool():
    """test executing a non-cooperative query in a cooperative pool (improper usage)"""
    pool = CooperativeQueryPool(timeout=0.1)

    call_count = 0

    def myfunc(**kw):
        nonlocal call_count
        call_count += 1
        if call_count > 1:
            # Note: this exception will also be printed when the test passed
            raise RuntimeError("the gevent loop was blocked")
        sleep(**kw)

    with pytest.raises(RuntimeError, match="the gevent loop was blocked"):
        with gevent.Timeout(0.5, "the gevent loop was not blocked"):
            while not pool.execute(myfunc, kwargs={"seconds": 2, "cooperative": False}):
                pass  # every iteration waits for 0.1 seconds

    assert pool.cancel(timeout=4)
