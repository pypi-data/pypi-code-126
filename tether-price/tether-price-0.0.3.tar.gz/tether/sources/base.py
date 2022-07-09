import logging
from queue import Queue
from typing import Tuple

from ..exceptions import TetherException
from ..models import Price

logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class SourceBase:
    _source_name = ''

    def get_price(self, queue: Queue) -> None:
        try:
            buy, sell = self._fetch_price()
            queue.put(
                Price(self._source_name, buy, sell)
            )
        except TetherException as err:
            self.log_error(err)

    def log_error(self, error: Exception) -> None:
        message = f'[{self._source_name}] - Something went wrong: %s'
        logger.log(logging.ERROR, message, error)

    def _fetch_price(self) -> Tuple[int, int]:
        raise NotImplementedError
