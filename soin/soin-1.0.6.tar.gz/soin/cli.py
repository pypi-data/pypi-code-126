import importlib
import logging
import os
import sys
import click

import soin

quit = False

@click.group()
def cli():
    pass


@cli.command()
@click.argument("module")
@click.option("-w", "--worker", is_flag=True, default=False, help="spawn as worker")
@click.option("-s", "--steps", default=None, help="max step for a worker to run")
def start(module, worker, steps=None):
    steps = int(steps) if steps else None
    sys.path.insert(0, os.getcwd())
    module = importlib.import_module(module)
    spider : soin.Spider = module.Main()
    if worker:
        spider.as_worker(steps)
    else:
        spider.main()
    logging.info("Gracefully existed!")


if __name__ == "__main__":
    cli()
