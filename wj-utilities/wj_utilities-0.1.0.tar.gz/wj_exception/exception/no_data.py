""" 
module for data not found exceptions
"""
from http import HTTPStatus
from typing import Optional

from .utils import utils


# NO DATA EXCEPTIONS
class ItemNotFound(Exception):
    """Excepction for any dato not found in databases

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "itemNotFound"
    message = "data not found"
    status = HTTPStatus(404)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class ErrorSavingData(Exception):
    """Excepction when occur any error saving data in the databases

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "errorSavingData"
    message = "Unexpected error when saving data"
    status = HTTPStatus(404)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)


class ModelNotFound(Exception):
    """Excepction when any model or table has not found in the databases

    Parameters:
    message: string: Optional exception message input must be a string type
    """

    code = "modelNotFound"
    message = "model not found or not exist in the databases"
    status = HTTPStatus(404)

    def __init__(self, message: Optional[str] = None):

        if utils.is_validate_message(message):
            self.message = message

        super().__init__(self.message)
