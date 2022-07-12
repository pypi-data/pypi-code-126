"""CLint operation results."""
from clint.cli.exceptions import ResultException


class Result:  # pylint: disable=too-few-public-methods
    """Class that stores result of an operation."""

    def __init__(self, operation: str, base_error_code):
        self.operation = operation
        self.actions = {}
        self.return_code = 0
        self.__base_error_code = base_error_code

    def add_action(self, action: str, message: str, is_error: bool) -> "Result":
        """
        Register new action in the operation.

        Parameters
        ----------
        action: str
            Action name of the operation.
        message: str
            Output message of the action.
        is_error: bool
            Indicate if the action ends in an error or not.

        Returns
        -------
        Result:
            Self object, to chain actions.

        Raises
        ------
        ResultException
            If the action has already been registered.
        """
        if action in self.actions:
            raise ResultException("Action result already registered.")
        self.actions[action] = message
        if is_error:
            if self.return_code == 0:
                self.return_code = self.__base_error_code
            self.return_code += 1
        return self
