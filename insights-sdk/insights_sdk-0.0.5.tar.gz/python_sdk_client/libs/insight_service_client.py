from pprint import pprint

import insights_python_client
from insights_python_client import Configuration, configuration
from insights_python_client.rest import ApiException

from python_sdk_client.libs.abstract_client import AbstractClient
from python_sdk_client.libs.batch_processor import handle
from python_sdk_client.libs.client_cfg import InsightServiceCfg
from python_sdk_client.clients_enum import EnvType
from python_sdk_client.libs.cropin_exceptions import InvalidInputError

"""
Insights Service Client
-----------------------

class to validate the inputs and set the env, endpoint and other env specific details.
"""


class InsightServiceClient(AbstractClient):
    """
    Initialising the env and base url
    """

    def __init__(self, tenant: str, username: str, password: str, env: EnvType) -> None:
        super(InsightServiceClient, self).__init__(tenant, username, password, env)

        self.tenant_type = 'SMARTFARM_PLUS'
        if env == EnvType.PROD:
            self.base_url = InsightServiceCfg.prod_base_url
        elif env == EnvType.QA:
            self.base_url = InsightServiceCfg.qa_base_url

        self.configuration = Configuration()
        # set base url
        self.configuration.host = self.base_url
        # set auth token
        self.configuration.api_key['Authorization'] = self.token

    """
    Validate input for fetching plot details
    """

    def get_plot_details(self, plot_ids: str):

        boundary_api = insights_python_client.BoundaryApi(insights_python_client.ApiClient(self.configuration))
        plot_ids_resp = handle(boundary_api.list_all3, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                               batch_size=InsightServiceCfg.BATCH_SIZE)
        return plot_ids_resp

    """
    Validate inputs for satellite details
    """

    def get_satellite_details(self, plot_ids: str):

        metrics_api = insights_python_client.MetricsApi(insights_python_client.ApiClient(self.configuration))
        plot_ids_resp = handle(metrics_api.list_all2, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                               batch_size=InsightServiceCfg.BATCH_SIZE)
        return plot_ids_resp

    """
    Validate inputs for weather details
    """

    def get_weather_details(self, plot_ids: str):

        weather_api = insights_python_client.WeatherApi(insights_python_client.ApiClient(self.configuration))
        weather_api_resp = handle(weather_api.list_all1, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                                  batch_size=InsightServiceCfg.BATCH_SIZE)
        return weather_api_resp

    """ 
    Validate inputs for yield details
    """

    def get_yield_details(self, plot_ids: str):
        yield_api = insights_python_client.YieldApi(insights_python_client.ApiClient(self.configuration))
        yield_api_resp = handle(yield_api.list_all, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                                batch_size=InsightServiceCfg.BATCH_SIZE)
        return yield_api_resp

    """
    Validate inputs for download plot image
    """

    def download_image(self, plot_id: str, image_name, image_type, date):
        download_api = insights_python_client.FileApi(insights_python_client.ApiClient(self.configuration))
        file_response = download_api.get_plot_image_for_satellite_and_health_indices(self.tenant_type, self.x_api_key,
                                                                                     org_id=self.org_id,
                                                                                     image_type=image_type,
                                                                                     image_name=image_name, _date=date,
                                                                                     boundary_id=plot_id)

        return file_response
