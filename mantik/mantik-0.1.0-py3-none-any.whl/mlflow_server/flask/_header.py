import logging
import re

import flask


logger = logging.getLogger(__name__)

AUTHORIZATION_HEADER_NAME = "Authorization"
BEARER_TOKEN_REGEX = re.compile(r"Bearer (.*)")


class MissingAuthorizationHeaderException(Exception):
    """The authorization header as in invalid form or missing."""


def get_authorization_token(request: flask.Request) -> str:
    """Get the authorization token from the request."""
    logger.debug("Getting token from request headers %s", request.headers)
    header = request.headers.get(AUTHORIZATION_HEADER_NAME)
    if header is None:
        raise MissingAuthorizationHeaderException(
            f"Request is missing '{AUTHORIZATION_HEADER_NAME}' header"
        )
    token = _get_token_from_header(header)
    logger.debug("Got token %s", token)
    return token


def _get_token_from_header(header: str) -> str:
    """Split the authorization header content.

    Notes
    -----
    The header can have two distinguished forms:

    1. Authorization: <token>
    2. Authorization: Bearer <token>

    """
    match = BEARER_TOKEN_REGEX.match(header)
    if match is None:
        return header
    return match.group(1)
