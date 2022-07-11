from typing import Generator

from ..trading import PricePoint

PriceStream = Generator[PricePoint, None, None]
