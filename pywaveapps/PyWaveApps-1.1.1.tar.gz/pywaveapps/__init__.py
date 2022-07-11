from __future__ import annotations
from gql.transport.aiohttp import AIOHTTPTransport
from gql import Client
from .query import Query
from .mutation import Mutation
import logging

__version__ = '1.1.1'


_logger = logging.Logger("PyWaveApps")
streamFormatter = logging.Formatter("[PyWaveApps] %(levelname)s: %(message)s")
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.DEBUG)
streamHandler.setFormatter(streamFormatter)
_logger.addHandler(streamHandler)


class WaveApps:

    ENDPOINT = "https://gql.waveapps.com/graphql/public"

    __instances__: list = []

    def __new__(cls, api_token, *args, **kwargs):
        for instance in cls.__instances__:
            if instance.api_token == api_token:
                _logger.warning("attempted to initialize a WaveApps instance with an already-in-use api_token; WaveApps instances must have unique api_tokens (returning the existing WaveApps instance with requested api_token)")
                return instance
        _logger.info(f"creating new WaveApps connection (instance)")
        instance = super(WaveApps, cls).__new__(cls, *args, **kwargs)
        WaveApps.__instances__.append(instance)
        return instance

    def __init__(self, api_token) -> None:
        # use api_token to identify the connection
        self.api_token = api_token

        # Select your transport with a defined url endpoint
        self.transport = AIOHTTPTransport(url=self.ENDPOINT, headers={'Authorization': 'Bearer ' + api_token})

        # Create a GraphQL client using the defined transport
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

        # Create the 'query' object for the WaveApps.query.{{ENDPOINT}} syntax
        self.query = Query(self)

        # Create the 'mutate' object for the WaveApps.mutate.{{endpoint}} syntax
        self.mutate = Mutation(self)
