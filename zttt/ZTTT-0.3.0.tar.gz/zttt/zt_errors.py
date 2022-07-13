
"""
zt_errors.py
--------------

The file contains the errors that can be raised by the zttt package.
"""


class ZTError(Exception):
    """Base class for all zt_errors."""
    pass


class ZTBadFunctionCall(AttributeError, ZTError):
    """Raised when a function is called with the wrong arguments. Mostly used for debugging."""
    pass


class ZTGameException(ZTError):
    """Raised when something function call crashes the game."""
    pass


class ZTInvalidInput(ValueError, ZTGameException):
    """Raised when the input provided is not valid."""
    pass
