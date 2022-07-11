"""CLint runner."""
from clint import validator


class Runner:  # pylint: disable=too-few-public-methods
    """Runner class for running the validator classes."""

    @staticmethod
    def validate(message: str) -> str:
        """Validate commit message."""
        try:
            commit = validator.Commit.generate(msg=message)
            commit.validate()
        except validator.GenerationException as exc:
            return f"Parsing error: {exc}"
        except validator.ValidationException as exc:
            return f"Validation error: {exc}"
        else:
            return "Your commit message is CC compliant!"
