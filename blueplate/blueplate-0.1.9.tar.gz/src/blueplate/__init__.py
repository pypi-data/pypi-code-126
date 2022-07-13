""" This module replaces the Pythonista3 builtin modules for calling shortcuts. This will work either in PyTo or Mac
>>> from minimock import Mock
>>> fn = Mock('print')
>>> fn('Test')
Called print('Test')

"""

from .blueplate.version import version
from .blueplate import logger
from .blueplate import special

__all__ = ["version", "logger", "special"]
