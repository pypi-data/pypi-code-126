# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._data_masking_rules_operations import build_create_or_update_request, build_list_by_database_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DataMaskingRulesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.aio.SqlManagementClient`'s
        :attr:`data_masking_rules` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        data_masking_rule_name: str,
        parameters: _models.DataMaskingRule,
        **kwargs: Any
    ) -> _models.DataMaskingRule:
        """Creates or updates a database data masking rule.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param database_name: The name of the database.
        :type database_name: str
        :param data_masking_rule_name: The name of the data masking rule.
        :type data_masking_rule_name: str
        :param parameters: The required parameters for creating or updating a data masking rule.
        :type parameters: ~azure.mgmt.sql.models.DataMaskingRule
        :keyword api_version: Api Version. Default value is "2014-04-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword data_masking_policy_name: The name of the database for which the data masking rule
         applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingRule, or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.DataMaskingRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2014-04-01"))  # type: str
        data_masking_policy_name = kwargs.pop('data_masking_policy_name', "Default")  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataMaskingRule]

        _json = self._serialize.body(parameters, 'DataMaskingRule')

        request = build_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            server_name=server_name,
            database_name=database_name,
            data_masking_rule_name=data_masking_rule_name,
            api_version=api_version,
            data_masking_policy_name=data_masking_policy_name,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('DataMaskingRule', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('DataMaskingRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules/{dataMaskingRuleName}"}  # type: ignore


    @distributed_trace
    def list_by_database(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.DataMaskingRuleListResult]:
        """Gets a list of database data masking rules.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param database_name: The name of the database.
        :type database_name: str
        :keyword api_version: Api Version. Default value is "2014-04-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword data_masking_policy_name: The name of the database for which the data masking rule
         applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DataMaskingRuleListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.sql.models.DataMaskingRuleListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2014-04-01"))  # type: str
        data_masking_policy_name = kwargs.pop('data_masking_policy_name', "Default")  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataMaskingRuleListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_database_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    database_name=database_name,
                    api_version=api_version,
                    data_masking_policy_name=data_masking_policy_name,
                    template_url=self.list_by_database.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_database_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    database_name=database_name,
                    api_version=api_version,
                    data_masking_policy_name=data_masking_policy_name,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DataMaskingRuleListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_database.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules"}  # type: ignore
