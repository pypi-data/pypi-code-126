import requests

from queue import PriorityQueue
from threading import Thread
from typing import List, Callable

from simple_proxy2.data.observer import Observer
from simple_proxy2.data.proxy import Proxy
from simple_proxy2.data.proxy_info import ProxyInfo
from simple_proxy2.tools.simple_timer import SimpleTimer
from simple_proxy2.tools.random_user_agent import get_random as random_agent


class ProxyPool(Observer):
    def __init__(self,
                 test_url: str,
                 success_rate_supplier: Callable[[], float],
                 proxy_infos: List[ProxyInfo]):
        self._test_url = test_url
        self._success_rate_supplier = success_rate_supplier
        self._pool = PriorityQueue()

        self._init_proxy_thread = Thread(
            target=self._init_proxy, args=(proxy_infos,))
        self._init_proxy_started = False

    def _init_proxy(self, proxy_infos: List[ProxyInfo]):
        assert len(
            proxy_infos) > 0, "At least one proxy must exist for ProxyPool to work properly."

        for info in proxy_infos:
            if not self._init_proxy_started:
                break

            proxy = Proxy(info, self._success_rate_supplier)
            proxy.register_observer(self)

            try:
                timer = SimpleTimer()
                with timer:
                    requests.get(self._test_url,
                                 proxies=proxy.info().as_requests_dict(),
                                 headers={'User-Agent': random_agent()},
                                 timeout=1)
                proxy.update_response_time(timer.time_elapsed())
            except:
                proxy.update_response_time(999.0)
                continue
            finally:
                self._pool.put(proxy)

    def poll(self) -> Proxy:
        assert self._init_proxy_started, "Proxy initialization is not started." \
                                         " Make sure to use the pool with #start()"

        return self._pool.get()

    def notify(self, proxy: Proxy):
        self._pool.task_done()
        self._pool.put(proxy)

    def start(self):
        self._init_proxy_started = True
        self._init_proxy_thread.start()

    def end(self):
        self._init_proxy_started = False
        self._init_proxy_thread.join()

    def __enter__(self):
        self.start()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
