import json
import re
from typing import List


def request_validation(
    request, body_type: str, expected_headers: dict, expected_values: List[str]
):
    """
    Function for validate W&J API requests

    Args:
        request: HTTP request object.
        body_type: String. Name of body type.
        expected_headers: List. String list with expected request headers.
        expected_values: List. String list with expected parameters for request body.

    Returns:
        dictionary that contains the following keys:

            ok: Boolean indicating the result of the validation.
            If True indicates that the request meets all requirements.

            details: String with details of validation.

            body: Dictionary with request body.
    """
    details, body = None, None

    if headers_validation(request, expected_headers) and expected_values:
        try:
            body = request.data

            if type(body).__name__ == body_type.lower():
                validation_ok = body_validation(body, body_type, expected_values)
                details = (
                    f"Required parameters {', '.join(expected_values)}"
                    if not validation_ok
                    else "OK"
                )
            else:
                validation_ok = False
                details = f"Invalid body syntax. Expected a {body_type}, but got {type(body).__name__}."

        except json.decoder.JSONDecodeError as e:
            validation_ok = False
            details = "[JSONDecodeError] Invalid JSON."

    elif not expected_values:
        validation_ok = True
        details = "Expected body parameters is an empty list"
    else:
        validation_ok = False
        details = "Received headers is not valid"

    return {"ok": validation_ok, "details": details, "body": body}


def headers_validation(request, expected_headers: dict):
    """
    Function for validate JSON request headers

    Args:
        request: Request object.
        expected_headers: list. String list with expected request headers.

    Returns:
        Boolean. True if request header is valid.
    """
    request_headers = request.META
    for header in expected_headers:
        if header in request_headers.keys():
            if request_headers[header] != expected_headers[header] and not re.search(
                rf"\b(\w*{expected_headers[header]}\w*)\b", request_headers[header]
            ):
                return False
        else:
            return False
    return True


def body_validation(
    body=None, body_type: str = None, expected_params: List[str] = None
):
    """
    Function used to validate body parameters

    Args:
        body: body request object.
        body_type: str. Name of body type.
        expected_params: list. String list with expected parameters for request body

    Returns:
        Boolean indicating the result of body validation
    """
    if type(body).__name__ == body_type:
        for parameter in expected_params:
            if parameter not in body.keys():
                return False
    else:
        return False
    return True
