from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.http_error_response_dto import HttpErrorResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    product_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/licenses/export".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["productId"] = product_id

    params["userId"] = user_id

    params["email"] = email

    params["query"] = query

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
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 401:
        response_401 = HttpErrorResponseDto.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = HttpErrorResponseDto.from_dict(response.json())

        return response_403
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
    *,
    client: Client,
    product_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, HttpErrorResponseDto]]:
    """Export all licenses

     Exports all licenses in the csv format.

    Args:
        product_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    kwargs = _get_kwargs(
        client=client,
        product_id=product_id,
        user_id=user_id,
        email=email,
        query=query,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    product_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, HttpErrorResponseDto]]:
    """Export all licenses

     Exports all licenses in the csv format.

    Args:
        product_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    return sync_detailed(
        client=client,
        product_id=product_id,
        user_id=user_id,
        email=email,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    product_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, HttpErrorResponseDto]]:
    """Export all licenses

     Exports all licenses in the csv format.

    Args:
        product_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    kwargs = _get_kwargs(
        client=client,
        product_id=product_id,
        user_id=user_id,
        email=email,
        query=query,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    product_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, HttpErrorResponseDto]]:
    """Export all licenses

     Exports all licenses in the csv format.

    Args:
        product_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, HttpErrorResponseDto]]
    """

    return (
        await asyncio_detailed(
            client=client,
            product_id=product_id,
            user_id=user_id,
            email=email,
            query=query,
        )
    ).parsed
