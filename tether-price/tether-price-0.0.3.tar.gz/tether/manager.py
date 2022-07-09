from queue import Queue
from threading import Thread
from typing import List

from .models import PricesList
from .sources.base import SourceBase


class SourceManager:
    _sources: List[SourceBase] = []

    def __init__(self) -> None:
        pass

    def add(self, source: SourceBase) -> None:
        if source not in self._sources:
            self._sources.append(source)

    def get_prices_list(self) -> PricesList:
        queue = Queue()
        threads: List[Thread] = []

        for source in self._sources:
            tr = Thread(target=source.get_price, args=(queue,))
            threads.append(tr)
            tr.start()

        for tr in threads:
            tr.join()

        prices = []
        while not queue.empty():
            prices.append(queue.get())

        return PricesList(prices)
