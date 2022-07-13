from kdp_connector.configuration.configurationUtil import ConfigurationUtil
from kdp_connector.configuration.authenticationUtil import AuthenticationUtil
from kdp_connector.connectors.ingest import IngestApi
from kdp_connector.connectors.ingest_job_api import IngestJobApi
from kdp_connector.connectors.read import ReadApi
from kdp_connector.connectors.kdp_api import KdpApi
from kdp_connector.connectors.query import QueryApi
from kdp_connector.connectors.index_management import IndexManagementApi
from kdp_connector.connectors.upload import UploadApi
from kdp_api.model.authentication import Authentication

class KdpConn(object):

    def __init__(self, path_to_ca_file: str = '', host: str = 'https://api.dev.koverse.com',
                 discard_unknown_keys: bool = True):
        self.path_to_ca_file = path_to_ca_file
        self.host = host
        self.discard_unknown_keys = discard_unknown_keys

    def create_configuration(self, jwt: str):
        config = ConfigurationUtil()
        return config.create_configuration(self.host, jwt, self.path_to_ca_file, self.discard_unknown_keys)

    # Auth
    def create_authentication_token(self, email: str, password: str, workspace_id: str, strategy: str = 'local') -> object:
        config = self.create_configuration('')

        auth_util = AuthenticationUtil()
        auth_response = auth_util.create_authentication_token(config, email, password, workspace_id, strategy)
        return auth_response

    # INGEST
    def batch_ingest(self, dataframe, dataset_id: str, jwt: str, batch_size: int = 100):
        ingest_api = IngestApi()
        config = self.create_configuration(jwt)
        return ingest_api.batch_ingest(config=config, dataset_id=dataset_id, dataframe=dataframe, batch_size=batch_size)

    def create_url_ingest_job(self, workspace_id: str, dataset_id: str, url_list, jwt: str) -> str :
        config = self.create_configuration(jwt)
        ingest_job_api = IngestJobApi(configuration=config)
        return ingest_job_api.create_url_ingest_job(workspace_id=workspace_id, dataset_id=dataset_id, url_list=url_list)

    # Query
    def post_lucene_query(self, dataset_id: str, jwt: str, expression: str = '', limit: int = 5, offset: int = 0):
        query_api = QueryApi()
        config = self.create_configuration(jwt)
        return query_api.post_lucene_query(config, dataset_id=dataset_id, expression=expression, limit=limit, offset=offset)

    # READ
    def read_dataset_to_dictionary_list(self, dataset_id: str, jwt: str,
                                        starting_record_id: str = '', batch_size: int = 100000):
        read_api = ReadApi()
        config = self.create_configuration(jwt)
        return read_api.read_dataset_to_dictionary_list(config, dataset_id, starting_record_id,
                                                        batch_size)

    def read_dataset_to_pandas_dataframe(self, dataset_id: str, jwt: str,
                                         starting_record_id: str = '', batch_size: int = 100000):
        read_api = ReadApi()
        config = self.create_configuration(jwt)
        return read_api.read_dataset_to_pandas_dataframe(config, dataset_id, starting_record_id,
                                                         batch_size)

    def get_splits(self, dataset_id: str, jwt: str):
        read_api = ReadApi()
        config = self.create_configuration(jwt)
        return read_api.get_splits(config=config, dataset_id=dataset_id)


    def read_batch(self, dataset_id: str, starting_record_id: str, ending_record_id:str,
        exclude_starting_record_id: bool, batch_size: int, jwt: str):
        read_api = ReadApi()
        config = self.create_configuration(jwt)
        return read_api.read_batch(config=config, dataset_id=dataset_id, starting_record_id=starting_record_id,
            ending_record_id=ending_record_id, exclude_starting_record_id=exclude_starting_record_id)


    # dataset
    def create_dataset(self, name: str, workspace_id: str, jwt: str, description: str = '',
                       auto_create_indexes: bool = True, schema: str = '{}', search_any_field: bool = True,
                       record_count: int = 0):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.create_dataset(config, name, workspace_id, description, auto_create_indexes, schema,
                                      search_any_field, record_count)

    def get_dataset(self, dataset_id, jwt):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.get_dataset(config, dataset_id)

    def patch_dataset(self, dataset_id, payload, jwt):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.patch_dataset(config, dataset_id, payload)

    # workspace
    def get_workspace(self, workspace_id, jwt):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.get_workspace(config, workspace_id)

    def create_workspace(self, name, jwt):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.create_workspace(config, name)

    def delete_workspace(self, workspace_id, jwt):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.delete_workspace(config, workspace_id)

    # indexes
    def get_indexes(self, dataset_id: str, jwt: str, limit: int = 10):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.get_indexes(config, dataset_id, limit)

    # modify index
    def modify_indexes(self, dataset_id: str, create: list, remove: list,
            autoCreateIndexes: bool, searchAnyField: bool, jwt: str) -> object :
        config = self.create_configuration(jwt)
        index_management_api = IndexManagementApi(configuration=config)
        return index_management_api.modify_indexes(dataset_id=dataset_id, create=create, remove=remove,
            autoCreateIndexes=autoCreateIndexes, searchAnyField=searchAnyField)


    # Jobs
    def get_jobs(self, dataset_id: str, jwt: str, **kwargs):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.get_jobs(config, dataset_id, kwargs)

    # Upload
    def upload(self, dataset_id: str, file_config: object, jwt: str):
        config = self.create_configuration(jwt)
        upload_api = UploadApi(configuration=config)
        return upload_api.upload(dataset_id=dataset_id, file_config=file_config)

    # User
    def delete_user(self, user_id: str, jwt: str):
        kdp_api = KdpApi()
        config = self.create_configuration(jwt)
        return kdp_api.delete_user(config, user_id)
