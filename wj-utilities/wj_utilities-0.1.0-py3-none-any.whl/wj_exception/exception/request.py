""" 
module for exceptions relationated with request errors like 
an invalid parameter
"""
from http import HTTPStatus
from typing import Optional

from .utils import utils


# INVALID REQUESTS
class InvalidRequestParameters(Exception):
    """Exception when any parameter is invalid in a request

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "invalidRequestParameters"
    message = "request parameter is invalid"
    status = HTTPStatus(400)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class MissingParameters(Exception):
    """Exception when any parameter has missed in a request

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "missingParameters"
    message = "request missed parameters"
    status = HTTPStatus(400)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class MissingHeaders(Exception):
    """Exception when any header has missed in a request

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "missingHeaders"
    message = "request missed headers"
    status = HTTPStatus(400)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class InvalidParamaterFormat(Exception):
    """Exception when any parameter in a request has invalid format

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "invalidParamaterFormat"
    message = "invalid parameter format"
    status = HTTPStatus(422)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class InvalidParamaterValue(Exception):
    """Exception when any parameter in a request has invalid value

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "invalidParamaterValue"
    message = "parameter has not valid value"
    status = HTTPStatus(422)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)
