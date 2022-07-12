from sys import api_version
import kdp_api
from kdp_api.api import query_api

class QueryApi(object):

    def post_lucene_query(self, config, dataset_id: str, expression: str, limit: int = 5, offset: int = 0):
        with kdp_api.ApiClient(config) as api_client:
            api_instance = query_api.QueryApi(api_client)

            query = {}
            query['datasetId'] = dataset_id
            query['expression'] = expression
            query['limit'] = limit
            query['offset'] = offset

            return api_instance.lucene_query(query)

