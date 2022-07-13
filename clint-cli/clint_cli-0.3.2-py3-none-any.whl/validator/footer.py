"""Footer validator."""
import re
import string

from ..cli.result import Result
from .exceptions import GenerationException


class Footer:
    """Validator class for paragraphs (body & footers) on the commit message."""

    PATTERN = re.compile(
        r"(?P<token>BREAKING CHANGE|[\w|-]+)"
        + r"(?P<separator>:\s+|\s#)"
        + r"(?P<description>[\w. ]+)"
        + r"\n?"
    )

    def __init__(self, token: str, separator: str, description: str):
        self.token = token or ""
        self.separator = separator or ""
        self.description = description or ""

    @staticmethod
    def generate(msg: str) -> "Footer":
        """
        Get a new instance of Footer from a commit footer line.

        Parameters
        ----------
        msg: str
            Commit footer line.

        Returns
        -------
        Footer
            New instance.

        Raises
        ------
        ValidatorException
            If the commit footer line did not match the pattern.
        """
        match = Footer.PATTERN.match(msg)
        if match is None:
            raise GenerationException(f"Message '{msg}' did not match the pattern.")
        groups = match.groupdict()
        return Footer(
            token=groups["token"],
            separator=groups["separator"],
            description=groups["description"],
        )

    def validate(self, result: Result) -> None:
        """
        Validate that all attributes in the class are conventional commits compliant.

        Parameters
        ----------
        result: Result
            Result object to register errors.

        Raises
        ------
        ValidatorException
            If any attribute is not valid.
        """
        # pylint: disable=duplicate-code
        if not self.token:
            result.add_action(
                action="token_empty",
                message="Token cannot be empty.",
                is_error=True,
            )
        for whitespace in string.whitespace:
            if self.token != "BREAKING CHANGE" and whitespace in self.token:
                result.add_action(
                    action="token_whitespace",
                    message=f"Token '{self.token}' cannot have '{whitespace}' char.",
                    is_error=True,
                )
        if not self.separator:
            result.add_action(
                action="separator_empty",
                message="Separator cannot be empty.",
                is_error=True,
            )
        valid_separators = [": ", " #"]
        if self.separator and self.separator not in valid_separators:
            result.add_action(
                action="separator_valid",
                message=f"Separator '{self.separator}' is not valid.",
                is_error=True,
            )
        if not self.description:
            result.add_action(
                action="description_empty",
                message="Description cannot be empty.",
                is_error=True,
            )
