# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import click


def main():  # no cov
    from datadog_checks.dev.tooling.cli import ddev

    try:
        return ddev(windows_expand_args=False)
    except Exception:
        from rich.console import Console

        console = Console()
        console.print_exception(suppress=[click])
        return 1
