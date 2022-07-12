from gql import gql

from navability.common.mutations import GQL_SOLVESESSION
from navability.entities.client import Client
from navability.entities.navabilityclient import MutationOptions, NavAbilityClient
from navability.entities.solve import SolveOptions


async def solveSession(
    navAbilityClient: NavAbilityClient,
    client: Client,
    solveOptions: SolveOptions = None,
):
    payload = {
        "client": client.dump(),
    }
    if solveOptions is not None:
        payload["options"] = solveOptions.dump()
    print(payload)
    result = await navAbilityClient.mutate(
        MutationOptions(
            gql(GQL_SOLVESESSION),
            payload,
        )
    )
    return result["solveSession"]
