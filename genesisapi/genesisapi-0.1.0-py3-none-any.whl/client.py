import json
from urllib.parse import urljoin, urlencode

import requests
from typeguard import typechecked

from .endpoint import EndpointRegistry
from .datatypes import JSON, Language
from .services.catalogue import CatalogueService
from .services.data import DataService
from .services.find import FindService
from .services.helloworld import HelloworldService
from .services.metadata import MetadataService
from .services.profile import ProfileService


class GenesisClient:
    # base_url: str = 'https://www.landesdatenbank.nrw.de/ldbnrwws/rest/2020/'
    # base_url: str = 'https://www-genesis.destatis.de/genesisWS/rest/2020/'

    @typechecked
    def __init__(
            self,
            username: str = None,
            password: str = None,
            language: Language = None,
            config_file: str = './config.json',
            registry: EndpointRegistry = None
    ):
        """

        :param username:
        :param password:
        :param language:
        :param config_file:
        """
        if config_file is not None:
            with open('config.json', 'r') as config_file:
                config = json.load(config_file)

        username = username if username else config['username']
        password = password if password else config['password']
        language = language if language else config['language']

        if username is None:
            raise ValueError('The parameter `username` is none.')

        if password is None:
            raise ValueError('The parameter `password` is none.')

        if registry is None:
            self.registry = EndpointRegistry.instance()

        self.base_url = self.registry['destatis'].url
        print(self.base_url)

        self.query_params = {
            'username': username,
            'password': password,
            'language': language
        }

        self.headers = {'Content-Type': 'application/json'}

        self.helloworld_service = HelloworldService(self)
        self.find_service = FindService(self)
        self.catalogue_service = CatalogueService(self)
        self.data_service = DataService(self)
        self.metadata_service = MetadataService(self)
        self.profile_service = ProfileService(self)

    @property
    def helloworld(self) -> HelloworldService:
        """Gets the helloworld service."""
        return self.helloworld_service

    @property
    def find(self) -> FindService:
        """Gets the find service."""
        return self.find_service

    @property
    def catalogue(self) -> CatalogueService:
        """Gets the catalogue service."""
        return self.catalogue_service

    @property
    def data(self) -> DataService:
        """Gets the data service."""
        return self.data_service

    @property
    def metadata(self) -> MetadataService:
        """Gets the metadata service."""
        return self.metadata_service

    @property
    def profile(self) -> ProfileService:
        """Gets the profile service."""
        return self.profile_service

    @typechecked
    def language(
        self,
        language: Language
    ):
        self.update_params(language=language)
        return self

    def page(self, length):
        self.update_params(pagelength=length)
        return self

    def criterion(self, search, sort):
        self.update_params(
            searchcriterion=str(search),
            sortcriterion=str(sort))
        return self

    def category(self, category):
        self.update_params(
            category=str(category))
        return self

    def selection(self, name):
        self.update_params(selection=name)
        return self

    def area(self, name):
        self.update_params(area=name)
        return self

    def object_type(self, object_type):
        self.update_params(type=object_type)
        return self

    def update_params(self, **kwargs):
        for kw in kwargs:
            self.query_params[kw] = kwargs[kw] or self.query_params.get(kw)
        return self

    def get_url(self, service, method, **kwargs):
        """Creates the url from the given service, method and query parameters."""

        kwargs = kwargs | {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        path = f"{service}/{method}"
        query = '?' + urlencode(self.query_params | kwargs)

        return urljoin(self.base_url, path + query)

    def get_json_result(
            self,
            url: str
    ) -> JSON:
        """"""
        response = requests.get(url)
        self.check_response(response)
        return response.json()

    @staticmethod
    def check_response(response):
        if not response.ok:
            raise Exception()
