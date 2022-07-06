from json import JSONDecodeError
from typing import Tuple

import requests
from requests import RequestException

from .base import SourceBase
from .. import config
from ..exceptions import TetherException


class ArzPaya(SourceBase):
    _source_name = 'ArzPaya'
    __site_url = 'https://api.arzpaya.com/public/Landing/usdt'

    def _fetch_price(self) -> Tuple[int, int]:
        try:
            req = requests.get(self.__site_url, timeout=config.TIMEOUT)
        except RequestException:
            raise TetherException('Cannot connect to ArzPaya sever.')

        try:
            data = req.json()['Data']
            buy = int(data['CurrentBuyPrice'])
            sell = int(data['CurrentSellPrice'])
            return buy, sell
        except JSONDecodeError:
            raise TetherException('Cannot decode response text.')
