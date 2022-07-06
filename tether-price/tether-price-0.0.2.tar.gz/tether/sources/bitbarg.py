import json
from typing import Tuple

import requests
from requests import RequestException

from .base import SourceBase
from .. import config
from ..exceptions import TetherException


class Bitbarg(SourceBase):
    _source_name = 'Bitbarg'
    __site_url = 'https://bitbarg.com/live-price/'

    def _fetch_price(self) -> Tuple[int, int]:
        try:
            req = requests.get(self.__site_url, timeout=config.TIMEOUT)
        except RequestException:
            raise TetherException('Cannot connect to Bitbarg sever.')

        text = req.text
        start = text.find('prices')
        end = start + 1
        while text[end] != '}':
            end += 1

        try:
            prices = json.loads(text[start + 8:end + 1])
            return prices['buy'], prices['sell']
        except json.JSONDecodeError:
            raise TetherException('Cannot decode response text.')
