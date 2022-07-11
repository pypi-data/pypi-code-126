""" 
module of exceptions relationated with unathorized errors as 
unauthenticate user errors
"""
from http import HTTPStatus
from typing import Optional

from .utils import utils


# ACCESS DENIED
class AccessDenied(Exception):
    """Excepction for login or user register with invalid credentials

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "accessDenied"
    message = "Error authentication user"
    status = HTTPStatus(401)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class SubscriptionError(Exception):
    """Exception for subscription error in some service

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "subscriptionError"
    message = "Action no allowed, check your subscription"
    status = HTTPStatus(401)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class InvalidUser(Exception):
    """
    Exception for errors with the user provided

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "invalidUser"
    message = "The user provided is invalid or does not exist"
    status = HTTPStatus(400)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class LoginUnsuccesful(Exception):
    """
    Exception when login is unsuccesful

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "loginUnsuccesful"
    message = "Unsaccesfull login"
    status = HTTPStatus(400)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


# NO AUTHENTICATED
class TokenError(Exception):
    """
    Exception when occurr any problems with a token in some service

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "tokenError"
    message = "Error validating access token"
    status = HTTPStatus(400)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class RegisterTokenError(Exception):
    """
    Exception occurs when an error is generated registering a token.

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "registerTokenError"
    message = "Error validating register token"
    status = HTTPStatus(400)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)
