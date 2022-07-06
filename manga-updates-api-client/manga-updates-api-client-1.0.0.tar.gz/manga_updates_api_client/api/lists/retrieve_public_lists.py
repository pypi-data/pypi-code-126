from typing import Any, Dict, List, Optional, cast

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lists/public/{user_id}".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Any]]:
    if response.status_code == 200:
        response_200 = cast(List[Any], response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Any]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[List[Any]]:
    """retrieve list of user lists

    Args:
        user_id (int):

    Returns:
        Response[List[Any]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[List[Any]]:
    """retrieve list of user lists

    Args:
        user_id (int):

    Returns:
        Response[List[Any]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[List[Any]]:
    """retrieve list of user lists

    Args:
        user_id (int):

    Returns:
        Response[List[Any]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[List[Any]]:
    """retrieve list of user lists

    Args:
        user_id (int):

    Returns:
        Response[List[Any]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
