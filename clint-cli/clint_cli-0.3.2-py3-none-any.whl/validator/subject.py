"""Subject validator."""
import re
from typing import Optional

from ..cli.result import Result
from .exceptions import GenerationException


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
        if not self.type:
            result.add_action(
                action="type_empty", message="Type cannot be empty.", is_error=True
            )
        elif not self.type.islower():
            result.add_action(
                action="type_case",
                message=f"Type '{self.type}' is not lowercase.",
                is_error=True,
            )
        elif self.type not in self.VALID_COMMIT_TYPES:
            result.add_action(
                action="type_valid",
                message=f"Type '{self.type}' is not valid.",
                is_error=True,
            )
        if self.scope:
            if not self.scope.startswith("("):
                result.add_action(
                    action="scope_start",
                    message=f"Scope '{self.type}' should starts with '('.",
                    is_error=True,
                )
            if not self.scope.endswith(")"):
                result.add_action(
                    action="scope_end",
                    message=f"Scope '{self.type}' should ends with ')'.",
                    is_error=True,
                )
            if len(self.scope) == 2:
                result.add_action(
                    action="scope_empty",
                    message=f"Scope '{self.type}' cannot be empty.",
                    is_error=True,
                )
        if not self.separator:
            result.add_action(
                action="separator_empty",
                message="Separator cannot be empty.",
                is_error=True,
            )
        elif self.separator != ": ":
            result.add_action(
                action="separator_invalid",
                message=f"Separator '{self.separator}' is not valid.",
                is_error=True,
            )
        if not self.description:
            result.add_action(
                action="description_empty",
                message="Description cannot be empty.",
                is_error=True,
            )
        if "\n" in self.description:
            result.add_action(
                action="description_newline",
                message="Description cannot have new lines.",
                is_error=True,
            )
