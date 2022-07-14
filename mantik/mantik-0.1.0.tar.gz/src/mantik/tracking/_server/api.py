import typing as t

import mantik.mlflow_server.flask.api as _api
import mantik.mlflow_server.tokens.cognito.exceptions as exceptions
import mantik.tracking._server._credentials as _credentials
import mantik.tracking._server.tokens as _tokens
import mantik.utils as utils
import requests


def create_tokens(
    credentials: t.Optional[_credentials.Credentials] = None,
) -> _tokens.Tokens:
    """Get the required tokens from the Cognito API.

    Raises
    ------
    RuntimeError
        If MLflow tracking URI environment variable is not set.

    """
    if credentials is None:
        credentials = _credentials.Credentials.from_env()
    return _get_tokens(
        url=_create_api_url(_api.tokens.CREATE_TOKEN_API_PATH),
        data=credentials.to_dict(),
    )


def refresh_tokens(
    tokens: _tokens.Tokens,
    credentials: t.Optional[_credentials.Credentials] = None,
) -> _tokens.Tokens:
    """Refresh the tokens.

    Raises
    ------
    RuntimeError
        If MLflow tracking URI environment variable is not set.

    Notes
    -----
    Refreshing a password requires to send the refresh token instead of the
    user's password.

    """
    if credentials is None:
        credentials = _credentials.Credentials.from_env()
    data = {
        **credentials.to_dict(include_password=False),
        "refresh_token": tokens.refresh_token,
    }
    try:
        return _get_tokens(
            url=_create_api_url(_api.tokens.REFRESH_TOKEN_API_PATH),
            data=data,
            refresh_token=tokens.refresh_token,
        )
    except requests.HTTPError as e:
        if _refresh_token_has_expired(e) or _refresh_token_is_invalid(e):
            return create_tokens(credentials)
        raise e


def _refresh_token_has_expired(e: requests.HTTPError) -> bool:
    return (
        e.response.status_code == 401
        and exceptions.REFRESH_TOKEN_EXPIRED_ERROR_MESSAGE in e.response.text
    )


def _refresh_token_is_invalid(e: requests.HTTPError) -> bool:
    return (
        e.response.status_code == 401
        and exceptions.REFRESH_TOKEN_INVALID_ERROR_MESSAGE in e.response.text
    )


def _create_api_url(endpoint: str) -> str:
    # If the request path contains double slashes, the request
    # is not forwarded to the API but to the UI and, thus, fails.
    mlflow_tracking_uri = utils.env.get_required_env_var(
        utils.mlflow.TRACKING_URI_ENV_VAR
    )
    if mlflow_tracking_uri is None:
        raise RuntimeError(
            f"MLflow tracking URI environment variable not set "
            f"('{utils.mlflow.TRACKING_URI_ENV_VAR}')"
        )
    return utils.urls.ensure_https_and_remove_double_slashes_from_path(
        f"{mlflow_tracking_uri}/{endpoint}"
    )


def _get_tokens(
    url: str, data: t.Dict, refresh_token: t.Optional[str] = None
) -> _tokens.Tokens:
    response = _get_response(url=url, data=data)
    return _tokens.Tokens.from_response(
        response=response,
        refresh_token=refresh_token,
    )


def _get_response(url: str, data: t.Dict) -> requests.Response:
    response = requests.post(
        url=url,
        json=data,
    )
    response.raise_for_status()
    return response
