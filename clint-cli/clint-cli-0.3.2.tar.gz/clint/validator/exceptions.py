"""Exceptions for validator package."""
from clint.exceptions import ClintException


class ValidatorException(ClintException):
    """Generic validator exception."""


class GenerationException(ValidatorException):
    """Exception in generation process."""


class ValidationException(ValidatorException):
    """Exception in validation process."""
