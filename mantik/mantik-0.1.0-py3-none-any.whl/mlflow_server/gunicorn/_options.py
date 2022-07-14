import argparse
import multiprocessing
import typing as t


def create_gunicorn_options(args: argparse.Namespace) -> t.Dict:
    """Create the options for the gunicorn app."""
    return {
        "bind": f"{args.host}:{args.port}",
        "workers": _number_of_workers(),
    }


def _number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1
