"""Complementary functions for get response error with standard format

    Typical usage example

    try:
        raise Exception()
    except Exception as e:
        response_error = get_response_error(exception=e)
"""

import sys


def __location_error() -> str:
    """return path of system information for location in an exception

    Returns:
        string with the  occurred exception path.
    """
    _, _, tb = sys.exc_info()
    return f"{tb.tb_frame.f_code.co_filename} in line {tb.tb_lineno}"


def __response_error_wj_exception(exception) -> dict:
    """Function for get standarize error response from a wj_exception.

    Args:
        exception: Exception. Is an custom wj exception with code, message and status

    Returns:
        dictionary with error response in standard format
    """

    return {
        "error": {
            "code": exception.code,
            "message": exception.message,
            "location": __location_error(),
        }
    }


def __response_error_exception(exception) -> dict:
    """Function for get standarize error response from a general python exception.

    Args:
        exception: Exception. Python exception object

    Returns:
        dictionary that contains the following keys:
        error: dictionary with following keys:
            message: string. Message with exception detail.
            code: string. Representation or exception name.
            location: string. Path where exception occured.
    """

    error = {"error": {}}

    if exception.args:
        error["error"]["message"] = f"{'. '.join(exception.args)}"
    else:
        error["error"]["message"] = exception.__doc__

    error["error"]["code"] = type(exception).__name__
    error["error"]["location"] = __location_error()

    return error


def get_response_error(exception) -> dict:
    """This function verify if the exception is a wj_exception and get correspond yours error response

    Args:
        exception: Exception. Python exception object

    Returns:
        dictionary that contains the following keys:
        error: dictionary with following keys:
            message: string. Message with exception detail.
            code: string. Representation or exception name.
            location: string. Path where exception occured.
    """

    if "wj_exception.exception" in str(type(exception)):
        return __response_error_wj_exception(exception=exception)

    return __response_error_exception(exception=exception)
