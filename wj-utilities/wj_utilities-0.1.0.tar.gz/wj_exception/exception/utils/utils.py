"""module for aditional functionalities requiered forthe wj exceptions implementation"""

import warnings


def is_valid_string(string):
    """validate if string is correct type str

    Args:
        string: str. any string for validation

    Returns:
        boolean. True when parameter is a string type
    """

    return isinstance(string, str)


def is_validate_message(new_message: str = None) -> bool:
    """validate if a message are a correct type and value

    Args:
        new_message: sting. Content of a message for any exceptions

    Returns:
        boolean. True if message is valid
    """

    if new_message is not None:
        if is_valid_string(new_message):
            return True
        else:
            warnings.warn(f"message {new_message} must be a string type", stacklevel=3)
            return False
    else:
        return False
