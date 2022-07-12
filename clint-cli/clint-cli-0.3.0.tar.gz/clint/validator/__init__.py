"""Validator classes."""

from .commit import Commit
from .exceptions import GenerationException, ValidationException
from .footer import Footer
from .paragraph import Paragraph
from .subject import Subject

OPERATION_NAME = Commit.OPERATION_NAME
OPERATION_BASE_ERROR_CODE = 100
