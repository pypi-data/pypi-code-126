"""Exceptions for validator package."""
from clint.exceptions import ClintException


class HookException(ClintException):
    """Generic hook exception."""


class ResultException(ClintException):
    """Generic result exception."""
