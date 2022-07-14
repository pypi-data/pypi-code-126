import argparse

import mlflow.server as server
import mlflow.utils.server_cli_utils as server_cli_utils


def initialize_backend_stores(args: argparse.Namespace) -> None:
    """Initialize the backend stores.

    Notes
    -----
    For reference see `mlflow.cli.server`.

    """
    if not args.testing:
        default_artifact_root = server_cli_utils.resolve_default_artifact_root(
            serve_artifacts=args.serve_artifacts,
            default_artifact_root=None,
            backend_store_uri=args.backend_store_uri,
        )
        server.handlers.initialize_backend_stores(
            args.backend_store_uri, default_artifact_root
        )
