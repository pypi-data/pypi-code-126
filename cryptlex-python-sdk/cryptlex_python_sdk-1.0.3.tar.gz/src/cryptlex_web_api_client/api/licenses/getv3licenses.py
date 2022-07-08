import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.getv_3_licenses_allowed_activations_type_1 import Getv3LicensesAllowedActivationsType1
from ...models.getv_3_licenses_allowed_deactivations_type_1 import Getv3LicensesAllowedDeactivationsType1
from ...models.getv_3_licenses_created_at_type_1 import Getv3LicensesCreatedAtType1
from ...models.getv_3_licenses_key_type_1 import Getv3LicensesKeyType1
from ...models.getv_3_licenses_metadata_key_type_1 import Getv3LicensesMetadataKeyType1
from ...models.getv_3_licenses_metadata_value_type_1 import Getv3LicensesMetadataValueType1
from ...models.getv_3_licenses_tag_type_1 import Getv3LicensesTagType1
from ...models.getv_3_licenses_total_activations_type_1 import Getv3LicensesTotalActivationsType1
from ...models.getv_3_licenses_total_deactivations_type_1 import Getv3LicensesTotalDeactivationsType1
from ...models.getv_3_licenses_user_company_type_1 import Getv3LicensesUserCompanyType1
from ...models.getv_3_licenses_user_email_type_1 import Getv3LicensesUserEmailType1
from ...models.getv_3_licenses_validity_type_1 import Getv3LicensesValidityType1
from ...models.http_error_response_dto import HttpErrorResponseDto
from ...models.license_dto import LicenseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
    product_version_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    reseller_id: Union[Unset, None, str] = UNSET,
    user_email: Union[Getv3LicensesUserEmailType1, None, Unset, str] = UNSET,
    user_company: Union[Getv3LicensesUserCompanyType1, None, Unset, str] = UNSET,
    key: Union[Getv3LicensesKeyType1, None, Unset, str] = UNSET,
    revoked: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    validity: Union[Getv3LicensesValidityType1, None, Unset, int] = UNSET,
    allowed_activations: Union[Getv3LicensesAllowedActivationsType1, None, Unset, int] = UNSET,
    allowed_deactivations: Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int] = UNSET,
    total_activations: Union[Getv3LicensesTotalActivationsType1, None, Unset, int] = UNSET,
    total_deactivations: Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int] = UNSET,
    allow_vm_activation: Union[Unset, None, bool] = UNSET,
    user_locked: Union[Unset, None, bool] = UNSET,
    expired: Union[Unset, None, bool] = UNSET,
    expiration_strategy: Union[Unset, None, str] = UNSET,
    created_at: Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    tag: Union[Getv3LicensesTagType1, None, Unset, str] = UNSET,
    metadata_key: Union[Getv3LicensesMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3LicensesMetadataValueType1, None, Unset, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/licenses".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["limit"] = limit

    params["sort"] = sort

    params["productId"] = product_id

    params["productVersionId"] = product_version_id

    params["userId"] = user_id

    params["resellerId"] = reseller_id

    json_user_email: Union[Dict[str, Any], None, Unset, str]
    if isinstance(user_email, Unset):
        json_user_email = UNSET
    elif user_email is None:
        json_user_email = None

    elif isinstance(user_email, Getv3LicensesUserEmailType1):
        json_user_email = UNSET
        if not isinstance(user_email, Unset):
            json_user_email = user_email.to_dict()

    else:
        json_user_email = user_email

    params["user.email"] = json_user_email

    json_user_company: Union[Dict[str, Any], None, Unset, str]
    if isinstance(user_company, Unset):
        json_user_company = UNSET
    elif user_company is None:
        json_user_company = None

    elif isinstance(user_company, Getv3LicensesUserCompanyType1):
        json_user_company = UNSET
        if not isinstance(user_company, Unset):
            json_user_company = user_company.to_dict()

    else:
        json_user_company = user_company

    params["user.company"] = json_user_company

    json_key: Union[Dict[str, Any], None, Unset, str]
    if isinstance(key, Unset):
        json_key = UNSET
    elif key is None:
        json_key = None

    elif isinstance(key, Getv3LicensesKeyType1):
        json_key = UNSET
        if not isinstance(key, Unset):
            json_key = key.to_dict()

    else:
        json_key = key

    params["key"] = json_key

    params["revoked"] = revoked

    params["suspended"] = suspended

    params["type"] = type

    json_validity: Union[Dict[str, Any], None, Unset, int]
    if isinstance(validity, Unset):
        json_validity = UNSET
    elif validity is None:
        json_validity = None

    elif isinstance(validity, Getv3LicensesValidityType1):
        json_validity = UNSET
        if not isinstance(validity, Unset):
            json_validity = validity.to_dict()

    else:
        json_validity = validity

    params["validity"] = json_validity

    json_allowed_activations: Union[Dict[str, Any], None, Unset, int]
    if isinstance(allowed_activations, Unset):
        json_allowed_activations = UNSET
    elif allowed_activations is None:
        json_allowed_activations = None

    elif isinstance(allowed_activations, Getv3LicensesAllowedActivationsType1):
        json_allowed_activations = UNSET
        if not isinstance(allowed_activations, Unset):
            json_allowed_activations = allowed_activations.to_dict()

    else:
        json_allowed_activations = allowed_activations

    params["allowedActivations"] = json_allowed_activations

    json_allowed_deactivations: Union[Dict[str, Any], None, Unset, int]
    if isinstance(allowed_deactivations, Unset):
        json_allowed_deactivations = UNSET
    elif allowed_deactivations is None:
        json_allowed_deactivations = None

    elif isinstance(allowed_deactivations, Getv3LicensesAllowedDeactivationsType1):
        json_allowed_deactivations = UNSET
        if not isinstance(allowed_deactivations, Unset):
            json_allowed_deactivations = allowed_deactivations.to_dict()

    else:
        json_allowed_deactivations = allowed_deactivations

    params["allowedDeactivations"] = json_allowed_deactivations

    json_total_activations: Union[Dict[str, Any], None, Unset, int]
    if isinstance(total_activations, Unset):
        json_total_activations = UNSET
    elif total_activations is None:
        json_total_activations = None

    elif isinstance(total_activations, Getv3LicensesTotalActivationsType1):
        json_total_activations = UNSET
        if not isinstance(total_activations, Unset):
            json_total_activations = total_activations.to_dict()

    else:
        json_total_activations = total_activations

    params["totalActivations"] = json_total_activations

    json_total_deactivations: Union[Dict[str, Any], None, Unset, int]
    if isinstance(total_deactivations, Unset):
        json_total_deactivations = UNSET
    elif total_deactivations is None:
        json_total_deactivations = None

    elif isinstance(total_deactivations, Getv3LicensesTotalDeactivationsType1):
        json_total_deactivations = UNSET
        if not isinstance(total_deactivations, Unset):
            json_total_deactivations = total_deactivations.to_dict()

    else:
        json_total_deactivations = total_deactivations

    params["totalDeactivations"] = json_total_deactivations

    params["allowVmActivation"] = allow_vm_activation

    params["userLocked"] = user_locked

    params["expired"] = expired

    params["expirationStrategy"] = expiration_strategy

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

    json_tag: Union[Dict[str, Any], None, Unset, str]
    if isinstance(tag, Unset):
        json_tag = UNSET
    elif tag is None:
        json_tag = None

    elif isinstance(tag, Getv3LicensesTagType1):
        json_tag = UNSET
        if not isinstance(tag, Unset):
            json_tag = tag.to_dict()

    else:
        json_tag = tag

    params["tag"] = json_tag

    json_metadata_key: Union[Dict[str, Any], None, Unset, str]
    if isinstance(metadata_key, Unset):
        json_metadata_key = UNSET
    elif metadata_key is None:
        json_metadata_key = None

    elif isinstance(metadata_key, Getv3LicensesMetadataKeyType1):
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

    elif isinstance(metadata_value, Getv3LicensesMetadataValueType1):
        json_metadata_value = UNSET
        if not isinstance(metadata_value, Unset):
            json_metadata_value = metadata_value.to_dict()

    else:
        json_metadata_value = metadata_value

    params["metadata.value"] = json_metadata_value

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[HttpErrorResponseDto, List[LicenseDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LicenseDto.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[HttpErrorResponseDto, List[LicenseDto]]]:
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
    product_version_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    reseller_id: Union[Unset, None, str] = UNSET,
    user_email: Union[Getv3LicensesUserEmailType1, None, Unset, str] = UNSET,
    user_company: Union[Getv3LicensesUserCompanyType1, None, Unset, str] = UNSET,
    key: Union[Getv3LicensesKeyType1, None, Unset, str] = UNSET,
    revoked: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    validity: Union[Getv3LicensesValidityType1, None, Unset, int] = UNSET,
    allowed_activations: Union[Getv3LicensesAllowedActivationsType1, None, Unset, int] = UNSET,
    allowed_deactivations: Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int] = UNSET,
    total_activations: Union[Getv3LicensesTotalActivationsType1, None, Unset, int] = UNSET,
    total_deactivations: Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int] = UNSET,
    allow_vm_activation: Union[Unset, None, bool] = UNSET,
    user_locked: Union[Unset, None, bool] = UNSET,
    expired: Union[Unset, None, bool] = UNSET,
    expiration_strategy: Union[Unset, None, str] = UNSET,
    created_at: Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    tag: Union[Getv3LicensesTagType1, None, Unset, str] = UNSET,
    metadata_key: Union[Getv3LicensesMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3LicensesMetadataValueType1, None, Unset, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[Union[HttpErrorResponseDto, List[LicenseDto]]]:
    """List all licenses

     Returns a list of licenses. The licenses are returned sorted by creation date in ascending order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        product_version_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        reseller_id (Union[Unset, None, str]):
        user_email (Union[Getv3LicensesUserEmailType1, None, Unset, str]):
        user_company (Union[Getv3LicensesUserCompanyType1, None, Unset, str]):
        key (Union[Getv3LicensesKeyType1, None, Unset, str]):
        revoked (Union[Unset, None, bool]):
        suspended (Union[Unset, None, bool]):
        type (Union[Unset, None, str]):
        validity (Union[Getv3LicensesValidityType1, None, Unset, int]):
        allowed_activations (Union[Getv3LicensesAllowedActivationsType1, None, Unset, int]):
        allowed_deactivations (Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int]):
        total_activations (Union[Getv3LicensesTotalActivationsType1, None, Unset, int]):
        total_deactivations (Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int]):
        allow_vm_activation (Union[Unset, None, bool]):
        user_locked (Union[Unset, None, bool]):
        expired (Union[Unset, None, bool]):
        expiration_strategy (Union[Unset, None, str]):
        created_at (Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime]):
        tag (Union[Getv3LicensesTagType1, None, Unset, str]):
        metadata_key (Union[Getv3LicensesMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3LicensesMetadataValueType1, None, Unset, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[LicenseDto]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        product_id=product_id,
        product_version_id=product_version_id,
        user_id=user_id,
        reseller_id=reseller_id,
        user_email=user_email,
        user_company=user_company,
        key=key,
        revoked=revoked,
        suspended=suspended,
        type=type,
        validity=validity,
        allowed_activations=allowed_activations,
        allowed_deactivations=allowed_deactivations,
        total_activations=total_activations,
        total_deactivations=total_deactivations,
        allow_vm_activation=allow_vm_activation,
        user_locked=user_locked,
        expired=expired,
        expiration_strategy=expiration_strategy,
        created_at=created_at,
        tag=tag,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
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
    product_version_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    reseller_id: Union[Unset, None, str] = UNSET,
    user_email: Union[Getv3LicensesUserEmailType1, None, Unset, str] = UNSET,
    user_company: Union[Getv3LicensesUserCompanyType1, None, Unset, str] = UNSET,
    key: Union[Getv3LicensesKeyType1, None, Unset, str] = UNSET,
    revoked: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    validity: Union[Getv3LicensesValidityType1, None, Unset, int] = UNSET,
    allowed_activations: Union[Getv3LicensesAllowedActivationsType1, None, Unset, int] = UNSET,
    allowed_deactivations: Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int] = UNSET,
    total_activations: Union[Getv3LicensesTotalActivationsType1, None, Unset, int] = UNSET,
    total_deactivations: Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int] = UNSET,
    allow_vm_activation: Union[Unset, None, bool] = UNSET,
    user_locked: Union[Unset, None, bool] = UNSET,
    expired: Union[Unset, None, bool] = UNSET,
    expiration_strategy: Union[Unset, None, str] = UNSET,
    created_at: Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    tag: Union[Getv3LicensesTagType1, None, Unset, str] = UNSET,
    metadata_key: Union[Getv3LicensesMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3LicensesMetadataValueType1, None, Unset, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HttpErrorResponseDto, List[LicenseDto]]]:
    """List all licenses

     Returns a list of licenses. The licenses are returned sorted by creation date in ascending order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        product_version_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        reseller_id (Union[Unset, None, str]):
        user_email (Union[Getv3LicensesUserEmailType1, None, Unset, str]):
        user_company (Union[Getv3LicensesUserCompanyType1, None, Unset, str]):
        key (Union[Getv3LicensesKeyType1, None, Unset, str]):
        revoked (Union[Unset, None, bool]):
        suspended (Union[Unset, None, bool]):
        type (Union[Unset, None, str]):
        validity (Union[Getv3LicensesValidityType1, None, Unset, int]):
        allowed_activations (Union[Getv3LicensesAllowedActivationsType1, None, Unset, int]):
        allowed_deactivations (Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int]):
        total_activations (Union[Getv3LicensesTotalActivationsType1, None, Unset, int]):
        total_deactivations (Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int]):
        allow_vm_activation (Union[Unset, None, bool]):
        user_locked (Union[Unset, None, bool]):
        expired (Union[Unset, None, bool]):
        expiration_strategy (Union[Unset, None, str]):
        created_at (Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime]):
        tag (Union[Getv3LicensesTagType1, None, Unset, str]):
        metadata_key (Union[Getv3LicensesMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3LicensesMetadataValueType1, None, Unset, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[LicenseDto]]]
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        product_id=product_id,
        product_version_id=product_version_id,
        user_id=user_id,
        reseller_id=reseller_id,
        user_email=user_email,
        user_company=user_company,
        key=key,
        revoked=revoked,
        suspended=suspended,
        type=type,
        validity=validity,
        allowed_activations=allowed_activations,
        allowed_deactivations=allowed_deactivations,
        total_activations=total_activations,
        total_deactivations=total_deactivations,
        allow_vm_activation=allow_vm_activation,
        user_locked=user_locked,
        expired=expired,
        expiration_strategy=expiration_strategy,
        created_at=created_at,
        tag=tag,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    product_id: Union[Unset, None, str] = UNSET,
    product_version_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    reseller_id: Union[Unset, None, str] = UNSET,
    user_email: Union[Getv3LicensesUserEmailType1, None, Unset, str] = UNSET,
    user_company: Union[Getv3LicensesUserCompanyType1, None, Unset, str] = UNSET,
    key: Union[Getv3LicensesKeyType1, None, Unset, str] = UNSET,
    revoked: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    validity: Union[Getv3LicensesValidityType1, None, Unset, int] = UNSET,
    allowed_activations: Union[Getv3LicensesAllowedActivationsType1, None, Unset, int] = UNSET,
    allowed_deactivations: Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int] = UNSET,
    total_activations: Union[Getv3LicensesTotalActivationsType1, None, Unset, int] = UNSET,
    total_deactivations: Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int] = UNSET,
    allow_vm_activation: Union[Unset, None, bool] = UNSET,
    user_locked: Union[Unset, None, bool] = UNSET,
    expired: Union[Unset, None, bool] = UNSET,
    expiration_strategy: Union[Unset, None, str] = UNSET,
    created_at: Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    tag: Union[Getv3LicensesTagType1, None, Unset, str] = UNSET,
    metadata_key: Union[Getv3LicensesMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3LicensesMetadataValueType1, None, Unset, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[Union[HttpErrorResponseDto, List[LicenseDto]]]:
    """List all licenses

     Returns a list of licenses. The licenses are returned sorted by creation date in ascending order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        product_version_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        reseller_id (Union[Unset, None, str]):
        user_email (Union[Getv3LicensesUserEmailType1, None, Unset, str]):
        user_company (Union[Getv3LicensesUserCompanyType1, None, Unset, str]):
        key (Union[Getv3LicensesKeyType1, None, Unset, str]):
        revoked (Union[Unset, None, bool]):
        suspended (Union[Unset, None, bool]):
        type (Union[Unset, None, str]):
        validity (Union[Getv3LicensesValidityType1, None, Unset, int]):
        allowed_activations (Union[Getv3LicensesAllowedActivationsType1, None, Unset, int]):
        allowed_deactivations (Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int]):
        total_activations (Union[Getv3LicensesTotalActivationsType1, None, Unset, int]):
        total_deactivations (Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int]):
        allow_vm_activation (Union[Unset, None, bool]):
        user_locked (Union[Unset, None, bool]):
        expired (Union[Unset, None, bool]):
        expiration_strategy (Union[Unset, None, str]):
        created_at (Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime]):
        tag (Union[Getv3LicensesTagType1, None, Unset, str]):
        metadata_key (Union[Getv3LicensesMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3LicensesMetadataValueType1, None, Unset, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[LicenseDto]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        limit=limit,
        sort=sort,
        product_id=product_id,
        product_version_id=product_version_id,
        user_id=user_id,
        reseller_id=reseller_id,
        user_email=user_email,
        user_company=user_company,
        key=key,
        revoked=revoked,
        suspended=suspended,
        type=type,
        validity=validity,
        allowed_activations=allowed_activations,
        allowed_deactivations=allowed_deactivations,
        total_activations=total_activations,
        total_deactivations=total_deactivations,
        allow_vm_activation=allow_vm_activation,
        user_locked=user_locked,
        expired=expired,
        expiration_strategy=expiration_strategy,
        created_at=created_at,
        tag=tag,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
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
    product_version_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    reseller_id: Union[Unset, None, str] = UNSET,
    user_email: Union[Getv3LicensesUserEmailType1, None, Unset, str] = UNSET,
    user_company: Union[Getv3LicensesUserCompanyType1, None, Unset, str] = UNSET,
    key: Union[Getv3LicensesKeyType1, None, Unset, str] = UNSET,
    revoked: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    validity: Union[Getv3LicensesValidityType1, None, Unset, int] = UNSET,
    allowed_activations: Union[Getv3LicensesAllowedActivationsType1, None, Unset, int] = UNSET,
    allowed_deactivations: Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int] = UNSET,
    total_activations: Union[Getv3LicensesTotalActivationsType1, None, Unset, int] = UNSET,
    total_deactivations: Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int] = UNSET,
    allow_vm_activation: Union[Unset, None, bool] = UNSET,
    user_locked: Union[Unset, None, bool] = UNSET,
    expired: Union[Unset, None, bool] = UNSET,
    expiration_strategy: Union[Unset, None, str] = UNSET,
    created_at: Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime] = UNSET,
    tag: Union[Getv3LicensesTagType1, None, Unset, str] = UNSET,
    metadata_key: Union[Getv3LicensesMetadataKeyType1, None, Unset, str] = UNSET,
    metadata_value: Union[Getv3LicensesMetadataValueType1, None, Unset, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HttpErrorResponseDto, List[LicenseDto]]]:
    """List all licenses

     Returns a list of licenses. The licenses are returned sorted by creation date in ascending order.

    Args:
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):
        product_id (Union[Unset, None, str]):
        product_version_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        reseller_id (Union[Unset, None, str]):
        user_email (Union[Getv3LicensesUserEmailType1, None, Unset, str]):
        user_company (Union[Getv3LicensesUserCompanyType1, None, Unset, str]):
        key (Union[Getv3LicensesKeyType1, None, Unset, str]):
        revoked (Union[Unset, None, bool]):
        suspended (Union[Unset, None, bool]):
        type (Union[Unset, None, str]):
        validity (Union[Getv3LicensesValidityType1, None, Unset, int]):
        allowed_activations (Union[Getv3LicensesAllowedActivationsType1, None, Unset, int]):
        allowed_deactivations (Union[Getv3LicensesAllowedDeactivationsType1, None, Unset, int]):
        total_activations (Union[Getv3LicensesTotalActivationsType1, None, Unset, int]):
        total_deactivations (Union[Getv3LicensesTotalDeactivationsType1, None, Unset, int]):
        allow_vm_activation (Union[Unset, None, bool]):
        user_locked (Union[Unset, None, bool]):
        expired (Union[Unset, None, bool]):
        expiration_strategy (Union[Unset, None, str]):
        created_at (Union[Getv3LicensesCreatedAtType1, None, Unset, datetime.datetime]):
        tag (Union[Getv3LicensesTagType1, None, Unset, str]):
        metadata_key (Union[Getv3LicensesMetadataKeyType1, None, Unset, str]):
        metadata_value (Union[Getv3LicensesMetadataValueType1, None, Unset, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[Union[HttpErrorResponseDto, List[LicenseDto]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            sort=sort,
            product_id=product_id,
            product_version_id=product_version_id,
            user_id=user_id,
            reseller_id=reseller_id,
            user_email=user_email,
            user_company=user_company,
            key=key,
            revoked=revoked,
            suspended=suspended,
            type=type,
            validity=validity,
            allowed_activations=allowed_activations,
            allowed_deactivations=allowed_deactivations,
            total_activations=total_activations,
            total_deactivations=total_deactivations,
            allow_vm_activation=allow_vm_activation,
            user_locked=user_locked,
            expired=expired,
            expiration_strategy=expiration_strategy,
            created_at=created_at,
            tag=tag,
            metadata_key=metadata_key,
            metadata_value=metadata_value,
            query=query,
        )
    ).parsed
