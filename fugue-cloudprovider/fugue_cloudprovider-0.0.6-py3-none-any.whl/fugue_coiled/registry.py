from typing import Any

from coiled import Cluster
from dask.distributed import Client, get_client
from fugue import register_execution_engine
from fugue_dask import DaskExecutionEngine
from triad import assert_or_throw


def register() -> None:
    register_execution_engine(
        "coiled",
        validate_coiled_client,
        on_dup="ignore",
    )
    register_execution_engine(
        Cluster,
        create_coiled_client,
        on_dup="ignore",
    )
    register_execution_engine(
        Client,
        lambda client, conf: DaskExecutionEngine(conf=conf),
        on_dup="ignore",
    )


def validate_coiled_client(conf: Any) -> DaskExecutionEngine:
    client = get_client()
    assert_or_throw(
        isinstance(client.cluster, Cluster),
        ValueError("the current Dask client is not a Coiled client"),
    )
    return DaskExecutionEngine()


def create_coiled_client(cluster: Cluster, conf: Any) -> DaskExecutionEngine:
    Client(cluster)
    return DaskExecutionEngine()
