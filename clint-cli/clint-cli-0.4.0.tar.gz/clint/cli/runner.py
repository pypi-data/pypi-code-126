"""CLint runner."""
from clint import validator

from ..hook_handler import HookException, HookHandler
from ..result import Result


class Runner:
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

    @staticmethod
    def change_hook_handler(is_enabling: bool) -> Result:
        """Change hook handler configuration."""
        try:
            handler = HookHandler()
        except HookException as exception:
            return Result(
                operation=HookHandler.OPERATION_NAME,
                base_error_code=HookHandler.OPERATION_BASE_ERROR_CODE,
            ).add_action(
                action=f"{'Enable' if is_enabling else 'Disable'} hook",
                message=str(exception),
                is_error=True,
            )
        else:
            if is_enabling:
                return handler.enable()
            return handler.disable()
