import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

__version__ = "1.2.4"
