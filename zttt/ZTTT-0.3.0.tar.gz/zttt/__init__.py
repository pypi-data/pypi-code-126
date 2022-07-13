
"""
The Main zttt Module
=====================

The module contains 2 main classes:
1. PvP: The class for the PvP game
2. PvC: The class for the PvC game

The module also contains the submodule zt_errors which contain the following errors
1. ZTError: The base class for all ZTErrors
2. ZTBadFunctionCall: The error raised when a function is called with the wrong arguments. Mostly used for debugging
3. ZTGameException: The error raised when a function call crashes the game
4. ZTWrongInput: The error raised when the input provided is not valid

"""

from .pvc import PvC
from .pvp import PvP
from . import zt_errors

__version__ = '0.2.0'
__author__ = 'Sumanth NR'
__email__ = 'sumanthnr62@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 Sumanth NR'
