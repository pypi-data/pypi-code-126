from json import JSONDecodeError
from typing import Tuple

import requests
from requests import RequestException

from .base import SourceBase
from .. import config
from ..exceptions import TetherException


class Hamtapay(SourceBase):
    _source_name = 'Hamtapay'
    __site_url = 'https://api.hamtapay.net/system/' \
                 '90asju92th0asfj0u-2350h9sdhf8nisdvcjnm3t928zhf-1249jj9sf9hj1-29rjoafjo9aq92/prices'

    def _fetch_price(self) -> Tuple[int, int]:
        try:
            req = requests.get(self.__site_url, timeout=config.TIMEOUT)
        except RequestException:
            raise TetherException('Cannot connect to Hamtapay sever.')

        try:
            data = req.json()['data']['IRT']['USDT_TRC20']
            buy = int(float(data['BUY']))
            sell = int(float(data['SELL']))
            return buy, sell
        except JSONDecodeError:
            raise TetherException('Cannot decode response text.')
