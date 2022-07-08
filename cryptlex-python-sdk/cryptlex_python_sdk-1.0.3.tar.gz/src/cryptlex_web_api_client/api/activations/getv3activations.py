import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.activation_dto import ActivationDto
from ...models.getv_3_activations_created_at_type_1 import Getv3ActivationsCreatedAtType1
from ...models.getv_3_activations_last_synced_at_type_1 import Getv3ActivationsLastSyncedAtType1
from ...models.getv_3_activations_metadata_key_type_1 import Getv3ActivationsMetadataKeyType1
from ...models.getv_3_activations_metadata_value_type_1 import Getv3ActivationsMetadataValueType1
from ...models.http_error_response_dto import HttpErrorResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
    license_id: Union[Unset, None, str] = UNSET,
    metadata_key: Union[Getv3ActivationsMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3ActivationsMetadataValueType1, None, Unset, str] = UNSET,
    created_at: Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    last_synced_at: Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/activations".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["limit"] = limit

    params["sort"] = sort

    params["productId"] = product_id

    params["licenseId"] = license_id

    json_metadata_key: Union[Dict[str, Any], None, Unset, str]
    if isinstance(metadata_key, Unset):
        json_metadata_key = UNSET
    elif metadata_key is None:
        json_metadata_key = None

    elif isinstance(metadata_key, Getv3ActivationsMetadataKeyType1):
        json_metadata_key = UNSET
        if not isinstance(metadata_key, Unset):
            json_metadata_key = metadata_key.to_dict()

    else:
        json_metadata_key = metadata_key

    params["metadata.key"] = json_metadata_key

    json_metadata_value: Union[Dict[str, Any], None, Unset, str]
    if isinstance(metadata_value, Unset):
        json_metadata_value = UNSET
    elif metadata_value is None:
        json_metadata_value = None

    elif isinstance(metadata_value, Getv3ActivationsMetadataValueType1):
        json_metadata_value = UNSET
        if not isinstance(metadata_value, Unset):
            json_metadata_value = metadata_value.to_dict()

    else:
        json_metadata_value = metadata_value

    params["metadata.value"] = json_metadata_value

    json_created_at: Union[Dict[str, Any], None, Unset, str]
    if isinstance(created_at, Unset):
        json_created_at = UNSET
    elif created_at is None:
        json_created_at = None

    elif isinstance(created_at, datetime.datetime):
        json_created_at = UNSET
        if not isinstance(created_at, Unset):
            json_created_at = created_at.isoformat()

    else:
        json_created_at = UNSET
        if not isinstance(created_at, Unset):
            json_created_at = created_at.to_dict()

    params["createdAt"] = json_created_at

    json_last_synced_at: Union[Dict[str, Any], None, Unset, str]
    if isinstance(last_synced_at, Unset):
        json_last_synced_at = UNSET
    elif last_synced_at is None:
        json_last_synced_at = None

    elif isinstance(last_synced_at, datetime.datetime):
        json_last_synced_at = UNSET
        if not isinstance(last_synced_at, Unset):
            json_last_synced_at = last_synced_at.isoformat()

    else:
        json_last_synced_at = UNSET
        if not isinstance(last_synced_at, Unset):
            json_last_synced_at = last_synced_at.to_dict()

    params["lastSyncedAt"] = json_last_synced_at

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[HttpErrorResponseDto, List[ActivationDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ActivationDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[HttpErrorResponseDto, List[ActivationDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
    license_id: Union[Unset, None, str] = UNSET,
    metadata_key: Union[Getv3ActivationsMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3ActivationsMetadataValueType1, None, Unset, str] = UNSET,
    created_at: Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    last_synced_at: Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[Union[HttpErrorResponseDto, List[ActivationDto]]]:
    """List all activations

     Returns a list of activations. The activations are returned sorted by creation date in ascending
    order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        license_id (Union[Unset, None, str]):
        metadata_key (Union[Getv3ActivationsMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3ActivationsMetadataValueType1, None, Unset, str]):
        created_at (Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime]):
        last_synced_at (Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[ActivationDto]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        product_id=product_id,
        license_id=license_id,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
        created_at=created_at,
        last_synced_at=last_synced_at,
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
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
    license_id: Union[Unset, None, str] = UNSET,
    metadata_key: Union[Getv3ActivationsMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3ActivationsMetadataValueType1, None, Unset, str] = UNSET,
    created_at: Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    last_synced_at: Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HttpErrorResponseDto, List[ActivationDto]]]:
    """List all activations

     Returns a list of activations. The activations are returned sorted by creation date in ascending
    order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        license_id (Union[Unset, None, str]):
        metadata_key (Union[Getv3ActivationsMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3ActivationsMetadataValueType1, None, Unset, str]):
        created_at (Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime]):
        last_synced_at (Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[ActivationDto]]]
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        product_id=product_id,
        license_id=license_id,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
        created_at=created_at,
        last_synced_at=last_synced_at,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
    license_id: Union[Unset, None, str] = UNSET,
    metadata_key: Union[Getv3ActivationsMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3ActivationsMetadataValueType1, None, Unset, str] = UNSET,
    created_at: Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    last_synced_at: Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[Union[HttpErrorResponseDto, List[ActivationDto]]]:
    """List all activations

     Returns a list of activations. The activations are returned sorted by creation date in ascending
    order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        license_id (Union[Unset, None, str]):
        metadata_key (Union[Getv3ActivationsMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3ActivationsMetadataValueType1, None, Unset, str]):
        created_at (Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime]):
        last_synced_at (Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[ActivationDto]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        product_id=product_id,
        license_id=license_id,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
        created_at=created_at,
        last_synced_at=last_synced_at,
        query=query,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
    license_id: Union[Unset, None, str] = UNSET,
    metadata_key: Union[Getv3ActivationsMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3ActivationsMetadataValueType1, None, Unset, str] = UNSET,
    created_at: Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    last_synced_at: Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HttpErrorResponseDto, List[ActivationDto]]]:
    """List all activations

     Returns a list of activations. The activations are returned sorted by creation date in ascending
    order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        license_id (Union[Unset, None, str]):
        metadata_key (Union[Getv3ActivationsMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3ActivationsMetadataValueType1, None, Unset, str]):
        created_at (Union[Getv3ActivationsCreatedAtType1, None, Unset, datetime.datetime]):
        last_synced_at (Union[Getv3ActivationsLastSyncedAtType1, None, Unset, datetime.datetime]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[ActivationDto]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            sort=sort,
            product_id=product_id,
            license_id=license_id,
            metadata_key=metadata_key,
            metadata_value=metadata_value,
            created_at=created_at,
            last_synced_at=last_synced_at,
            query=query,
        )
    ).parsed
