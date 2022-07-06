"""Footer validator."""
import re
import string

from .exceptions import GenerationException, ValidationException


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

    def validate(self) -> bool:
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
        if not self.token:
            raise ValidationException("Token cannot be empty.")
        for whitespace in string.whitespace:
            if self.token != "BREAKING CHANGE" and whitespace in self.token:
                raise ValidationException(
                    f"Token '{self.token}' cannot have '{whitespace}' char."
                )
        if not self.separator:
            raise ValidationException("Separator cannot be empty.")
        valid_separators = [": ", " #"]
        if self.separator not in valid_separators:
            raise ValidationException(f"Separator '{self.separator}' is not valid.")
        if not self.description:
            raise ValidationException("Description cannot be empty.")
        return True
