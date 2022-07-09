from enum import Enum
from typing import Union, Dict, Any, List, Type, Literal

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]

Language = Literal['de', 'en']


class Category(str, Enum):
    ALL = 'all',
    TABLES = 'tables',
    STATISTICS = 'statistics',
    CUBES = 'cubes',
    VARIABLES = 'variables',
    TIME_SERIES = 'time-series'

    def __str__(self):
        return self.value


class Criterion(str, Enum):
    CODE = 'code',
    CONTENT = 'content'

    def __str__(self):
        return self.value


class Area(str, Enum):
    ALL = 'all'

    def __str__(self):
        return self.value


class DataType(str, Enum):
    Category = 'klassifizierend'
    D1 = 'insgesamt'
    D2 = 'räumlich'
    D3 = 'sachlich'
    Value = 'wert'
    Time = 'zeitlich'
    Date = 'zeitidentifizierend'

    def __str__(self):
        return self.value
