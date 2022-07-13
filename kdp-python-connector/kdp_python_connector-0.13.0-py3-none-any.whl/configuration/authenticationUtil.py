import kdp_api
from kdp_api.api.authentication_api import AuthenticationApi
from kdp_api.api.authentication_api import Authentication


class AuthenticationUtil(object):

    @staticmethod
    def create_authentication_token(config, email: str, password: str, workspace_id: str, strategy: str = 'local'):

        with kdp_api.ApiClient(config) as api_client:
            api_instance = AuthenticationApi(api_client)

            authentication = Authentication(strategy=strategy, email=email, password=password, workspaceId=workspace_id)
            return api_instance.authentication_post(authentication=authentication)
