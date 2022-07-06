import sys

__version__ = '0.0.1'


if sys.version_info < (3, 8):
    raise SystemError('Python 3.8 or newer required.')

from piban.piban import Piban  # noqa
