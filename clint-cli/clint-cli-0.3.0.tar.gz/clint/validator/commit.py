"""Commit validator."""
from typing import Optional

from ..cli.result import Result
from .paragraph import Paragraph
from .subject import Subject


class Commit:
    """Validator class for commit message."""

    OPERATION_NAME = "Validator"
    OPERATION_BASE_ERROR_CODE = 0

    def __init__(self, text: str):
        split = text.split("\n\n")
        self.subject = Subject.generate(split.pop(0))
        self.paragraphs = tuple(Paragraph.generate(p) for p in split)

    @staticmethod
    def generate(msg: str) -> Optional["Commit"]:
        """
        Get a new Commit instance from a commit message.

        Parameters
        ----------
        msg: str
            Commit message.

        Returns
        -------
        Commit, optional
            Commit instance if the commit message matches the pattern. None otherwise.
        """
        return Commit(text=msg)

    def validate(self) -> Result:
        """
        Validate that all attributes in the class are conventional commits compliant.

        Returns
        -------
        bool:
            True if the object is valid.

        Raises
        ------
        ValidatorException
            If any attribute is not valid.
        """
        # pylint: disable=duplicate-code
        result = Result(
            operation=self.OPERATION_NAME,
            base_error_code=self.OPERATION_BASE_ERROR_CODE,
        )
        self.subject.validate(result=result)
        for paragraph in self.paragraphs:
            paragraph.validate(result=result)
        if not result.actions:
            result.add_action(
                action="validation",
                message="Your commit message is CC compliant!",
                is_error=False,
            )
        return result
