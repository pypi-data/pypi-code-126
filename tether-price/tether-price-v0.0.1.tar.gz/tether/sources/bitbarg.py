import json
from queue import Queue
from typing import Tuple, Optional

import requests
from requests import RequestException

from .base import SourceBase
from .. import config
from ..exceptions import TetherException
from ..models import Price


class Bitbarg(SourceBase):
    __source_name = 'Bitbarg'
    __site_url = 'https://bitbarg.com/live-price/'

    def get_price(self, queue: Queue) -> None:
        buy, sell = self._fetch_price()
        queue.put(
            Price(
                self.__source_name, buy, sell
            )
        )

    def _fetch_price(self) -> Optional[Tuple[int, int]]:
        try:
            req = requests.get(self.__site_url, timeout=config.TIMEOUT)
        except RequestException:
            raise TetherException('Cannot connect to Bitbarg sever.')

        text = req.text
        start = text.find('prices')
        end = start + 1
        while text[end] != '}':
            end += 1

        prices = json.loads(text[start + 8:end + 1])
        return prices['buy'], prices['sell']
