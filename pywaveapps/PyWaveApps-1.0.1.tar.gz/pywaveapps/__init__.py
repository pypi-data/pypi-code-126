from __future__ import annotations
from gql.transport.aiohttp import AIOHTTPTransport
from gql import Client
from .query import Query
from .mutation import Mutation


__version__ = '1.0.1'


class WaveApps:
    ENDPOINT = "https://gql.waveapps.com/graphql/public"

    def __init__(self, api_token) -> None:
        # Select your transport with a defined url endpoint
        self.transport = AIOHTTPTransport(url=self.ENDPOINT, headers={'Authorization': 'Bearer ' + api_token})

        # Create a GraphQL client using the defined transport
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

        # Create the 'query' object for the WaveApps.query.{{ENDPOINT}} syntax
        self.query = Query(self)

        # Create the 'mutate' object for the WaveApps.mutate.{{endpoint}} syntax
        self.mutate = Mutation(self)
