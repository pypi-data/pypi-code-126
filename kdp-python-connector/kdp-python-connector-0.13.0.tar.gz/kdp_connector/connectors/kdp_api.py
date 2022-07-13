import kdp_api as kdp_api_client
from kdp_api.api.datasets_api import DatasetsApi
from kdp_api.api.workspaces_api import WorkspacesApi
from kdp_api.api.indexes_api import IndexesApi
from kdp_api.api.jobs_api import JobsApi
from kdp_api.api.users_api import UsersApi

class KdpApi(object):

    @staticmethod
    def create_dataset(config, name: str, workspace_id: str, description: str = '', auto_create_indexes: bool = True,
                       schema: str = '{}', search_any_field: bool = True, record_count: int = 0):

        with kdp_api_client.ApiClient(config) as api_client:
            request_body = {
                    'name': name,
                    'record_count': record_count,
                    'description': description,
                    'auto_create_indexes': auto_create_indexes,
                    'schema': schema,
                    'search_any_field': search_any_field,
                    'workspace_id': workspace_id
                }

            datasets_api = DatasetsApi(api_client)
            return datasets_api.datasets_post(create_dataset=request_body)

    @staticmethod
    def create_workspace(config, name: str, workspace_id: str = None):

        with kdp_api_client.ApiClient(config) as api_client:

            request_body = {
                'name': name,
                'id': workspace_id if workspace_id is not None else name
            }
            workspaces_api = WorkspacesApi(api_client)
            return workspaces_api.workspaces_post(workspace1=request_body)

    @staticmethod
    def delete_workspace(config, workspace_id: str):

        with kdp_api_client.ApiClient(config) as api_client:

            workspaces_api = WorkspacesApi(api_client)
            return workspaces_api.workspaces_id_delete(workspace_id)


    @staticmethod
    def get_workspace(config, workspace_id: str):

        with kdp_api_client.ApiClient(config) as api_client:

            workspaces_api = WorkspacesApi(api_client)
            return workspaces_api.workspaces_id_get(workspace_id)

    @staticmethod
    def get_dataset(config, dataset_id: str):

        with kdp_api_client.ApiClient(config) as api_client:

            datasets_api = DatasetsApi(api_client)
            return datasets_api.datasets_id_get(dataset_id)


    @staticmethod
    def patch_dataset(config, dataset_id: str, payload: object):
        with kdp_api_client.ApiClient(config) as api_client:
            datasets_api = DatasetsApi(api_client)
            return datasets_api.datasets_id_patch(id=dataset_id, patch_dataset=payload)


    @staticmethod
    def get_indexes(config, dataset_id: str, limit: int = 10):
        with kdp_api_client.ApiClient(config) as api_client:
            indexes_api = IndexesApi(api_client)
            return indexes_api.indexes_get(dataset_id=dataset_id, limit=limit)

    @staticmethod
    def get_index(config, index_id: str):
        with kdp_api_client.ApiClient(config) as api_client:
            indexes_api = IndexesApi(api_client)
            return indexes_api.indexes_id_get(id=index_id)

    @staticmethod
    def get_jobs(config, dataset_id: str, **kwargs):
        with kdp_api_client.ApiClient(config) as api_client:
            jobs_api = JobsApi(api_client)
            return jobs_api.jobs_get(dataset_id=dataset_id, **kwargs)


    @staticmethod
    def delete_user(config, user_id: str):
        with kdp_api_client.ApiClient(config) as api_client:
            user_api = UsersApi(api_client)
            return user_api.users_id_delete(user_id)
