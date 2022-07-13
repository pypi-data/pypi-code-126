"""CLint runner."""
from clint import validator

from .result import Result


class Runner:  # pylint: disable=too-few-public-methods
    """Runner class for running the validator classes."""

    @staticmethod
    def validate(message: str) -> Result:
        """Validate commit message."""
        try:
            commit = validator.Commit.generate(msg=message)
            result = commit.validate()
        except validator.GenerationException as exc:
            return Result(
                operation=validator.OPERATION_NAME,
                base_error_code=validator.OPERATION_BASE_ERROR_CODE,
            ).add_action(action="generation", message=str(exc), is_error=True)
        except validator.ValidationException as exc:
            return Result(
                operation=validator.OPERATION_NAME,
                base_error_code=validator.OPERATION_BASE_ERROR_CODE,
            ).add_action(action="validation", message=str(exc), is_error=True)
        else:
            return result
