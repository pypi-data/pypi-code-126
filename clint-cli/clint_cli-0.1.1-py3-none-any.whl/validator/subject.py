"""Subject validator."""
import re
from typing import Optional

from .exceptions import GenerationException, ValidationException


class Subject:
    """Validator class for subject section of the commit message."""

    PATTERN = re.compile(
        r"^(?P<type>\w+)?"
        + r"(?P<scope>\([\w\- ]+\))?"
        + r"(?P<breaking>!)?"
        + r"(?P<separator>:\s+)?"
        + r"(?P<description>[\w. ]+)?$"
    )

    VALID_COMMIT_TYPES = {
        "build",
        "chore",
        "ci",
        "docs",
        "feat",
        "fix",
        "perf",
        "refactor",
        "revert",
        "style",
        "test",
    }

    def __init__(
        self, c_type: str, scope: str, breaking: str, separator: str, description: str
    ):  # pylint: disable=too-many-arguments
        """
        Initialize the class attributes.

        Parameters
        ----------
        c_type: str
            Type of the commit changes.
        scope: str, optional
            Scope of the commit changes.
        breaking: str
            Breaking changes in commit. Possible values are "!" or "".
        separator: str
            Separator in the message. Only valid value is ": ".
        description: str
            Description of the commit.
        """
        self.type = c_type or ""
        self.scope = scope or ""
        self.breaking = breaking or ""
        self.separator = separator or ""
        self.description = description or ""

    @staticmethod
    def generate(msg: str) -> Optional["Subject"]:
        """
        Get a new instance of Subject from a commit subject line.

        Parameters
        ----------
        msg: str
            Commit subject line.

        Returns
        -------
        Subject, optional
            Subject instance if the subject line matches the pattern. None otherwise.
        """
        match = Subject.PATTERN.match(msg)
        if match is None:
            raise GenerationException(f"Message '{msg}' did not match the pattern.")
        groups = match.groupdict()
        return Subject(
            groups["type"],
            groups["scope"],
            groups["breaking"],
            groups["separator"],
            groups["description"],
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
        if not self.type:
            raise ValidationException("Type cannot be empty.")
        if not self.type.islower():
            raise ValidationException(f"Type '{self.type}' is not lowercase.")
        if self.type not in self.VALID_COMMIT_TYPES:
            raise ValidationException(f"Type '{self.type}' is not valid.")
        if self.scope and not self.scope.startswith("("):
            raise ValidationException(f"Scope '{self.type}' should starts with '('.")
        if self.scope and not self.scope.endswith(")"):
            raise ValidationException(f"Scope '{self.type}' should ends with ')'.")
        if self.scope and len(self.scope) == 2:
            raise ValidationException(f"Scope '{self.type}' cannot be empty.")
        if not self.separator:
            raise ValidationException("Separator cannot be empty.")
        if self.separator != ": ":
            raise ValidationException(f"Separator '{self.separator}' is not valid.")
        if not self.description:
            raise ValidationException("Description cannot be empty.")
        if "\n" in self.description:
            raise ValidationException("Description cannot have new lines.")
        return True
