from dataclasses import dataclass


@dataclass
class Endpoint:
    name: str
    url: str
    version: str


class EndpointRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EndpointRegistry, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self._databases = dict()

    @classmethod
    def instance(cls):
        """Returns the singleton instance of the endpoiunt register."""
        if cls._instance is None:
            cls._instance = EndpointRegistry()

        return cls._instance

    def __getitem__(self, name: str) -> Endpoint:
        return self._instance._databases[name]

    def add(self, endpoint: Endpoint):
        """Adds a database configuration item."""
        self._instance._databases[endpoint.name] = endpoint
        return self


endpoint_registry = EndpointRegistry.instance()

endpoint_registry.add(Endpoint(
    name='destatis',
    url='https://www-genesis.destatis.de/genesisWS/rest/2020/',
    version='GENESIS V4.4.1 - 2022'))

endpoint_registry.add(Endpoint(
    name='ldb_nrw',
    url='https://www.landesdatenbank.nrw.de/ldbnrwws/rest/2020/',
    version='GENESIS V4.3.3 - 2021'))
