from dataclasses import dataclass
from typing import List


@dataclass
class Price:
    source: str
    buy: int
    sell: int


@dataclass
class PricesList:
    prices: List[Price]
