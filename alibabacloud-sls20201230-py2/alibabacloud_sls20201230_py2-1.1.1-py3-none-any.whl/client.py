# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_sls.client import Client as GatewayClientClient
from alibabacloud_sls20201230 import models as sls_20201230_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client = None  # type: SPIClient

    def __init__(self, config):
        super(Client, self).__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-southeast-1': 'sls.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou': 'sls.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'sls.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'sls.cn-huhehaote.aliyuncs.com',
            'cn-shanghai': 'sls.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'sls.cn-shenzhen.aliyuncs.com',
            'cn-zhangjiakou': 'sls.cn-zhangjiakou.aliyuncs.com',
            'eu-central-1': 'sls.eu-central-1.aliyuncs.com'
        }

    def create_consumer_group(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(project, logstore, request, headers, runtime)

    def create_consumer_group_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def create_index(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(project, logstore, request, headers, runtime)

    def create_index_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateIndexResponse(),
            self.execute(params, req, runtime)
        )

    def create_log_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_log_store_with_options(project, request, headers, runtime)

    def create_log_store_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    def create_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateProjectResponse(),
            self.execute(params, req, runtime)
        )

    def create_saved_search(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_saved_search_with_options(project, request, headers, runtime)

    def create_saved_search_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def delete_consumer_group(self, project, logstore, consumer_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(project, logstore, consumer_group, headers, runtime)

    def delete_consumer_group_with_options(self, project, logstore, consumer_group, headers, runtime):
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        consumer_group = OpenApiUtilClient.get_encode_param(consumer_group)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def delete_index(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(project, logstore, headers, runtime)

    def delete_index_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteIndexResponse(),
            self.execute(params, req, runtime)
        )

    def delete_log_store(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_log_store_with_options(project, logstore, headers, runtime)

    def delete_log_store_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def delete_project(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project, headers, runtime)

    def delete_project_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectResponse(),
            self.execute(params, req, runtime)
        )

    def get_context_logs(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_context_logs_with_options(project, logstore, request, headers, runtime)

    def get_context_logs_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        query = {}
        if not UtilClient.is_unset(request.back_lines):
            query['back_lines'] = request.back_lines
        if not UtilClient.is_unset(request.forward_lines):
            query['forward_lines'] = request.forward_lines
        if not UtilClient.is_unset(request.pack_id):
            query['pack_id'] = request.pack_id
        if not UtilClient.is_unset(request.pack_meta):
            query['pack_meta'] = request.pack_meta
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContextLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetContextLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_cursor(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        shard_id = OpenApiUtilClient.get_encode_param(shard_id)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursor',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorResponse(),
            self.execute(params, req, runtime)
        )

    def get_cursor_time(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_time_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_time_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        shard_id = OpenApiUtilClient.get_encode_param(shard_id)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['cursor'] = request.cursor
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursorTime',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorTimeResponse(),
            self.execute(params, req, runtime)
        )

    def get_histograms(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_histograms_with_options(project, logstore, request, headers, runtime)

    def get_histograms_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetHistogramsResponse(),
            self.execute(params, req, runtime)
        )

    def get_index(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(project, logstore, headers, runtime)

    def get_index_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetIndexResponse(),
            self.execute(params, req, runtime)
        )

    def get_log_store(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_with_options(project, logstore, headers, runtime)

    def get_log_store_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def get_logs(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logs_with_options(project, logstore, request, headers, runtime)

    def get_logs_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            query['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            query['reverse'] = request.reverse
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_project(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project, headers, runtime)

    def get_project_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectResponse(),
            self.execute(params, req, runtime)
        )

    def get_project_logs(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_logs_with_options(project, request, headers, runtime)

    def get_project_logs_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_saved_search(self, project, savedsearch_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_saved_search_with_options(project, savedsearch_name, headers, runtime)

    def get_saved_search_with_options(self, project, savedsearch_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        savedsearch_name = OpenApiUtilClient.get_encode_param(savedsearch_name)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def list_consumer_group(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_with_options(project, logstore, headers, runtime)

    def list_consumer_group_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def list_log_stores(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_stores_with_options(project, request, headers, runtime)

    def list_log_stores_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogStoresResponse(),
            self.execute(params, req, runtime)
        )

    def list_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    def list_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.project_name):
            query['projectName'] = request.project_name
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListProjectResponse(),
            self.execute(params, req, runtime)
        )

    def list_saved_search(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_saved_search_with_options(project, request, headers, runtime)

    def list_saved_search_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def list_shards(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shards_with_options(project, logstore, headers, runtime)

    def list_shards_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShards',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShardsResponse(),
            self.execute(params, req, runtime)
        )

    def merge_shards(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.merge_shards_with_options(project, logstore, shard_id, request, headers, runtime)

    def merge_shards_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        shard_id = OpenApiUtilClient.get_encode_param(shard_id)
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MergeShards',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.MergeShardsResponse(),
            self.execute(params, req, runtime)
        )

    def split_shard(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.split_shard_with_options(project, logstore, shard_id, request, headers, runtime)

    def split_shard_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        shard_id = OpenApiUtilClient.get_encode_param(shard_id)
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.shard_count):
            query['shardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SplitShard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.SplitShardResponse(),
            self.execute(params, req, runtime)
        )

    def update_consumer_group(self, project, logstore, consumer_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(project, logstore, consumer_group, request, headers, runtime)

    def update_consumer_group_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        consumer_group = OpenApiUtilClient.get_encode_param(consumer_group)
        body = {}
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def update_index(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_with_options(project, logstore, request, headers, runtime)

    def update_index_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateIndexResponse(),
            self.execute(params, req, runtime)
        )

    def update_log_store(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_with_options(project, logstore, request, headers, runtime)

    def update_log_store_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        logstore = OpenApiUtilClient.get_encode_param(logstore)
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def update_project(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project, request, headers, runtime)

    def update_project_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateProjectResponse(),
            self.execute(params, req, runtime)
        )

    def update_saved_search(self, project, savedsearch_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_saved_search_with_options(project, savedsearch_name, request, headers, runtime)

    def update_saved_search_with_options(self, project, savedsearch_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        savedsearch_name = OpenApiUtilClient.get_encode_param(savedsearch_name)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )
