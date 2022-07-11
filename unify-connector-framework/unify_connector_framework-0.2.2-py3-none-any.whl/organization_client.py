# Copyright 2021 Element Analytics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A organization client includes methods needed for connectors.
"""
import logging
from enum import Enum
from unify.properties import Properties, ClusterSetting
from unify.orgadmin import OrgAdmin
from unify.sources import Sources
from unify.templates import Templates
from unify.graph import Graph
from unify.connectors import ConnStatus, LogType, ArtifactType, Connectors

import csv # TODO discuss about how to find templates updated

class DatasetOperation(Enum):
    """
    Operation class represent types of dataset operations
    """
    UPDATE = 1
    APPEND = 2

class OrganizationClient:
    """
    Common connector class
    """
    def __init__(self, user_name, password, org_id, cluster, connector_params):
        self.user_name = user_name
        self.password = password
        self.org_id = org_id
        self.cluster = cluster
        self.connector_params = connector_params

        self.app_name = 'imc'
        self.props = Properties(ClusterSetting.MEMORY)
        self.props.store_cluster(user_name, password, cluster, self.app_name)
        try:
            org_admin = OrgAdmin(self.app_name, self.props)
            token = org_admin.auth_token(
                query_params=connector_params
            )
            self.props.set_auth_token(
                token=token,
                cluster=self.app_name
            )
        except Exception as error:
            logging.error('Failed to login. %s', error)
            raise error

        try:
            self.sources = Sources(self.app_name, self.props)
            self.templates = Templates(self.app_name, self.props)
            self.connectors = Connectors(self.app_name, self.props)
        except Exception as error:
            logging.error('Failed to get organization sources client.')
            raise error

        try:
            self.templates = Templates(self.app_name, self.props)
        except Exception as error:
            logging.error('Failed to get organization templates client.')
            raise error

        try:
            self.graph = Graph(self.app_name, self.props)
        except Exception as error:
            logging.error('Failed to get organization graph client.')
            raise error

    def track_status(func):
        """
        Method used to wrap all other methods to be able to track status of the connector
        """
        def tracking_status(self, *args, **kwargs):
            try:
                self.connectors.update_connector_status(
                    self.org_id,
                    connector_id=self.connector_params['connector_id'],
                    status=ConnStatus.GOOD
                )
                result = func(self, *args, **kwargs)
            except Exception as err:
                self.connectors.update_connector_status(
                    self.org_id,
                    connector_id=self.connector_params['connector_id'],
                    status=ConnStatus.ERROR
                )
                raise
            return result
        return tracking_status

    @track_status
    def list_datasets(self):
        """
        Retrieve all datasets.
        """
        return self.sources.get_sources(org_id=self.org_id)

    @track_status
    def list_datasets_by_labels(self, labels):
        """
        Retrieve all datasets by labels.

        :type labels: list of strings
        :param labels: list of dataset labels. Example ["label1", "label2"]
        """
        return self.sources.get_sources_by_labels(org_id=self.org_id, facets=labels)

    @track_status
    def get_dataset(self, dataset_id):
        """
        Retrieve dataset contents.

        :type dataset_id: string or dict
        :param dataset_id: id of dataset
        """
        dataset_id_str = self.resolve_dataset_id(dataset_id)
        return self.sources.download_dataset_content(org_id=self.org_id, dataset_id=dataset_id_str)

    @track_status
    def create_dataset(self, name, dataset_csv):
        """
        Create a new dataset.

        :type name: string
        :param name: Name of dataset
        :type dataset_csv: string
        :param dataset_csv: Content to upload
        """
        dataset_info =  self.sources.create_api_data_set_with_content(
            name,
            self.org_id,
            content=dataset_csv
        )
        self.check_or_set_artifact(dataset_info['data_set_id'], ArtifactType.DATASET, name)
        return dataset_info

    @track_status
    def update_dataset(self, dataset_csv, dataset_name=None, dataset_id=None):
        """
        Update a dataset. If dataset does not exist, create a new dataset.

        :type dataset_csv: string
        :param dataset_csv: Content to upload
        :type dataset_name: string
        :param dataset_name: Name of dataset
        :type dataset_id: string or dict
        :param dataset_id: Existing dataset id
        """
        dataset_id_str = self.resolve_dataset_id(dataset_id)
        list_datasets = self.list_datasets()
        existing_datasets = [dataset.get("id", {}).get('id') for dataset in list_datasets]
        if dataset_id_str is None or dataset_id_str not in existing_datasets:
            response = self.create_dataset(name=dataset_name, dataset_csv=dataset_csv)
            dataset_id_str = response.get("data_set_id")
        else:
            self.truncate_dataset(dataset_id=dataset_id_str)
            self.append_dataset(dataset_id=dataset_id_str, dataset_csv=dataset_csv)
            dataset_name = [x['name'] for x in list_datasets if x['id']['id']==dataset_id_str][0]

        self.check_or_set_artifact(dataset_id_str, ArtifactType.DATASET, dataset_name)

        return dataset_id_str

    @track_status
    def truncate_dataset(self, dataset_id):
        """
        Truncate a dataset.

        :type dataset_id: string or dict
        :param dataset_id: Existing dataset id
        """
        dataset_id_str = self.resolve_dataset_id(dataset_id)
        result = self.sources.truncate_data_set(org_id=self.org_id, data_set_id=dataset_id_str)
        dataset_name = [x['name'] for x in self.list_datasets() if x['id']['id']==dataset_id_str][0]
        self.check_or_set_artifact(dataset_id_str, ArtifactType.DATASET, dataset_name)
        return result

    @track_status
    def append_dataset(self, dataset_id, dataset_csv):
        """
        Append a dataset.

        :type dataset_csv: string
        :param dataset_csv: Content to upload
        :type dataset_id: string or dict
        :param dataset_id: Existing dataset id
        """
        dataset_id_str = self.resolve_dataset_id(dataset_id)
        result = self.sources.append_dataset(
            org_id=self.org_id,
            data_set_id=dataset_id_str,
            content=dataset_csv)
        dataset_name = [x['name'] for x in self.list_datasets() if x['id']['id']==dataset_id_str][0]
        self.check_or_set_artifact(dataset_id_str, ArtifactType.DATASET, dataset_name)
        return result

    @track_status
    def update_dataset_labels(self, dataset_id, labels):
        """
        Updates labels for a dataset.

        :type dataset_id: string or dict
        :param dataset_id: Existing dataset id
        :type labels: dict
        :param labels: Labels
        """
        dataset_id_str = self.resolve_dataset_id(dataset_id)
        result = self.sources.label(self.org_id, dataset_id_str, labels)
        dataset_name = [x['name'] for x in self.list_datasets() if x['id']['id']==dataset_id_str][0]
        self.check_or_set_artifact(dataset_id_str, ArtifactType.DATASET, dataset_name)
        return result

    @track_status
    def operate_dataset(
        self,
        dataset_csv,
        dataset_id=None,
        dataset_name=None,
        operation=DatasetOperation.UPDATE
    ):
        """
        Operate dataset on given dataset_id. If dataset_id is not given, create a dataset first.
        If dataset is not valid, throw an error.

        :type dataset_csv: string
        :param dataset_csv: Content to upload
        :type dataset_name: string
        :param dataset_name: Name of dataset
        :type dataset_id: string or dict
        :param dataset_id: Existing dataset id
        :type operation: Enum
        :param operation: Operation on dataset, update or append
        """
        dataset_id_str = self.resolve_dataset_id(dataset_id)
        if dataset_id_str is None:
            dataset_id_str = self.create_dataset(dataset_name, dataset_csv)['data_set_id']
            logging.info('create dataset %s id %s to cluster: %s, organization: %d',
                dataset_name, dataset_id_str, self.cluster, self.org_id)
        else:
            # validate dataset_id
            existing_datasets = [
                dataset.get("id", {}).get('id') for dataset in self.list_datasets()
            ]
            if dataset_id_str not in existing_datasets:
                raise Exception(f'Given dataset id {dataset_id_str} does not exists.')
            if operation is DatasetOperation.UPDATE:
                self.truncate_dataset(dataset_id=dataset_id_str)
                self.append_dataset(dataset_id=dataset_id_str, dataset_csv=dataset_csv)
                logging.info('update dataset %s  to cluster: %s, organization: %d',
                    dataset_id_str, self.cluster, self.org_id)
            elif operation is DatasetOperation.APPEND:
                self.append_dataset(dataset_id_str, dataset_csv)
                logging.info('append dataset %s to cluster: %s, organization: %d',
                    dataset_id_str, self.cluster, self.org_id)
        return dataset_id_str


    @track_status
    def upload_template(self, template_csv):
        """
        Upload asset template definition csv.

        :type template_csv: string
        :param template_csv: asset template definition in csv format
        """
        result = self.templates.upload_string_content_file(self.org_id, template_csv)
        all_templates = [(x['id'], x['name']) for x in self.list_templates()]
        templates_updated = {x['Template Name'] for x in csv.DictReader(template_csv.splitlines())}
        for template in all_templates:
            if template[1] not in templates_updated:
                continue
            self.check_or_set_artifact(template[0], ArtifactType.TEMPLATE, template[1])
        
        return result

    @track_status
    def upload_template_configuration(self, config_csv):
        """
        Upload asset template configuration parameter definition csv.

        :type config_csv: string
        :param config_csv: asset template configuration parameter definition in csv format
        """
        result = self.templates.upload_config_with_content(self.org_id, config_csv)
        all_templates = [(x['id'], x['name']) for x in self.list_templates()]
        templates_updated = {x['template'] for x in csv.DictReader(config_csv.splitlines())}
        for template in all_templates:
            if template[1] not in templates_updated:
                continue
            self.check_or_set_artifact(template[0], ArtifactType.TEMPLATE, template[1])
        return result

    @track_status
    def update_template_categories(self, template_id, template_name, version, categories):
        """
        Update categories to an asset template.

        :type template_id: string
        :param template_id: Existing template id
        :type template_name: string
        :param template_name: Existing template name
        :type version: string
        :param version: Existing template id
        :type categories: dict
        :param categories: Labels
        """
        result = self.templates.category(
            self.org_id,
            template_id=template_id,
            template_name=template_name,
            version=version,
            categories=categories
        )
        self.check_or_set_artifact(template_id, ArtifactType.TEMPLATE, template_name)
        return result

    @track_status
    def list_templates(self):
        """
        Retrieve all asset templates
        """
        return self.templates.list_asset_templates(self.org_id)

    @track_status
    def list_graphs(self):
        """
        Retrieve all graphs.
        """
        return self.graph.get_graphs_list(org_id=self.org_id)

    @track_status
    def get_graph(self, graph_id, query=None):
        """
        Retrieve graph.

        :type graph_id: string
        :param graph_id: id of graph
        :type query: string
        :param query: graph cypher query
        """
        if query is None:
            query = "MATCH (source)-[relationship]->(destination) RETURN source, relationship, " \
                "destination"

        return self.graph.query_graph(org_id=self.org_id, graph=graph_id, query=query)

    @staticmethod
    def resolve_dataset_id(dataset_id):
        if dataset_id is None:
            return None
        if isinstance(dataset_id, dict):
            return dataset_id['id']
        if isinstance(dataset_id, str):
            return dataset_id
        raise ValueError(f'dataset_id {dataset_id} is not a valid value')

    def check_or_set_artifact(self, artifact_id, artifact_type, artifact_name):
        """
        Checks if the artifact is already created otherwise it will create it

        :type artifact_id: str
        :param artifact_id: Id of the artifact to be checked or created
        :type artifact_type: str
        :param artifact_type: Type of the artifact to set in case it is not created yet
        :type artifact_name: str
        :param artifact_name: Artifact name to use in case it is not created yet
        """
        artifact_id = str(artifact_id)
        artifacts = self.connectors.get_artifacts(
            self.org_id,
            connector_id=self.connector_params['connector_id']
        )
        if not any(x for x in artifacts if x['artifactId']==artifact_id):
            self.connectors.create_artifact(
                self.org_id,
                connector_id=self.connector_params['connector_id'],
                artifact_type=artifact_type,
                artifact_name=artifact_name,
                artifact_id=artifact_id
            )