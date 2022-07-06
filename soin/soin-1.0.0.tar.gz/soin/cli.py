import importlib
import logging
import click

import soin

quit = False

@click.group()
def cli():
    pass


@cli.command()
@click.argument("module")
@click.option("-w", "--worker", is_flag=True, default=False, help="spawn as worker")
def start(module, worker):
    module = importlib.import_module(module)
    spider : soin.Spider = module.Main()
    spider.setup()
    if worker:
        spider.as_worker()
    else:
        spider.spawn_worker_thread()
        spider.run()
    logging.info("Gracefully existed!")


if __name__ == "__main__":
    cli()
