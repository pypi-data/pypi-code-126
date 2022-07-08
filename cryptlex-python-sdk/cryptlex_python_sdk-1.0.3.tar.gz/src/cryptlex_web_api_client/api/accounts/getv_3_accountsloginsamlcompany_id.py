from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.http_error_response_dto import HttpErrorResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    client: Client,
    return_url: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/accounts/login/saml/{companyId}".format(client.base_url, companyId=company_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["returnUrl"] = return_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HttpErrorResponseDto]]:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302
    if response.status_code == 404:
        response_404 = HttpErrorResponseDto.from_dict(response.json())

        return response_404
    if response.status_code == 429:
        response_429 = HttpErrorResponseDto.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = HttpErrorResponseDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HttpErrorResponseDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: Client,
    return_url: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, HttpErrorResponseDto]]:
    """Initiate SAML SSO login

     Redirects to the identity provider's SSO login page.

    Args:
        company_id (str):
        return_url (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        return_url=return_url,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    company_id: str,
    *,
    client: Client,
    return_url: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, HttpErrorResponseDto]]:
    """Initiate SAML SSO login

     Redirects to the identity provider's SSO login page.

    Args:
        company_id (str):
        return_url (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        return_url=return_url,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: Client,
    return_url: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, HttpErrorResponseDto]]:
    """Initiate SAML SSO login

     Redirects to the identity provider's SSO login page.

    Args:
        company_id (str):
        return_url (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        return_url=return_url,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    company_id: str,
    *,
    client: Client,
    return_url: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, HttpErrorResponseDto]]:
    """Initiate SAML SSO login

     Redirects to the identity provider's SSO login page.

    Args:
        company_id (str):
        return_url (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            return_url=return_url,
        )
    ).parsed
