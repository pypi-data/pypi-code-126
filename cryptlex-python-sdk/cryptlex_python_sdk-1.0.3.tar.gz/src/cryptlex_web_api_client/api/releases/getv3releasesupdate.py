from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.http_error_response_dto import HttpErrorResponseDto
from ...models.release_dto import ReleaseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    platform: str,
    product_id: str,
    channel: Union[Unset, None, str] = UNSET,
    version: str,
    key: str,
) -> Dict[str, Any]:
    url = "{}/v3/releases/update".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["platform"] = platform

    params["productId"] = product_id

    params["channel"] = channel

    params["version"] = version

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HttpErrorResponseDto, ReleaseDto]]:
    if response.status_code == 200:
        response_200 = ReleaseDto.from_dict(response.json())

        return response_200
    if response.status_code == 429:
        response_429 = HttpErrorResponseDto.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = HttpErrorResponseDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HttpErrorResponseDto, ReleaseDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    platform: str,
    product_id: str,
    channel: Union[Unset, None, str] = UNSET,
    version: str,
    key: str,
) -> Response[Union[HttpErrorResponseDto, ReleaseDto]]:
    """Check for an update

     Checks whether a new release is available by comparing with the provided release version.

    Args:
        platform (str):
        product_id (str):
        channel (Union[Unset, None, str]):
        version (str):
        key (str):

    Returns:
        Response[Union[HttpErrorResponseDto, ReleaseDto]]
    """

    kwargs = _get_kwargs(
        client=client,
        platform=platform,
        product_id=product_id,
        channel=channel,
        version=version,
        key=key,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    platform: str,
    product_id: str,
    channel: Union[Unset, None, str] = UNSET,
    version: str,
    key: str,
) -> Optional[Union[HttpErrorResponseDto, ReleaseDto]]:
    """Check for an update

     Checks whether a new release is available by comparing with the provided release version.

    Args:
        platform (str):
        product_id (str):
        channel (Union[Unset, None, str]):
        version (str):
        key (str):

    Returns:
        Response[Union[HttpErrorResponseDto, ReleaseDto]]
    """

    return sync_detailed(
        client=client,
        platform=platform,
        product_id=product_id,
        channel=channel,
        version=version,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    platform: str,
    product_id: str,
    channel: Union[Unset, None, str] = UNSET,
    version: str,
    key: str,
) -> Response[Union[HttpErrorResponseDto, ReleaseDto]]:
    """Check for an update

     Checks whether a new release is available by comparing with the provided release version.

    Args:
        platform (str):
        product_id (str):
        channel (Union[Unset, None, str]):
        version (str):
        key (str):

    Returns:
        Response[Union[HttpErrorResponseDto, ReleaseDto]]
    """

    kwargs = _get_kwargs(
        client=client,
        platform=platform,
        product_id=product_id,
        channel=channel,
        version=version,
        key=key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    platform: str,
    product_id: str,
    channel: Union[Unset, None, str] = UNSET,
    version: str,
    key: str,
) -> Optional[Union[HttpErrorResponseDto, ReleaseDto]]:
    """Check for an update

     Checks whether a new release is available by comparing with the provided release version.

    Args:
        platform (str):
        product_id (str):
        channel (Union[Unset, None, str]):
        version (str):
        key (str):

    Returns:
        Response[Union[HttpErrorResponseDto, ReleaseDto]]
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            product_id=product_id,
            channel=channel,
            version=version,
            key=key,
        )
    ).parsed
