"""Exceptions in validator class."""


class ValidatorException(Exception):
    """Generic validator exception."""


class GenerationException(ValidatorException):
    """Exception in generation process."""


class ValidationException(ValidatorException):
    """Exception in validation process."""
