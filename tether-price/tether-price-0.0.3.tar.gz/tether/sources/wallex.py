from json import JSONDecodeError
from typing import Tuple

import requests
from requests import RequestException

from .base import SourceBase
from .. import config
from ..exceptions import TetherException


class Wallex(SourceBase):
    _source_name = 'Wallex'
    __site_url = 'https://api.wallex.ir/v1/markets'

    def _fetch_price(self) -> Tuple[int, int]:
        try:
            req = requests.get(self.__site_url, timeout=config.TIMEOUT)
        except RequestException:
            raise TetherException('Cannot connect to Wallex sever.')

        try:
            data = req.json()['result']['symbols']['USDTTMN']['stats']
            buy = int(float(data['askPrice']))
            sell = int(float(data['bidPrice']))
            return buy, sell
        except JSONDecodeError:
            raise TetherException('Cannot decode response text.')
