import click

from qplay_cli.broker.zerodha.z_broker import ZBroker
from quantplay.brokerage.angelone.angel_broker import AngelBroker


@click.group()
def broker():
    pass

@broker.command()
@click.option('--broker_name', default=None)
def generate_token(broker_name):
    if broker_name == None:
        print("--broker_name [Zerodha/AngelOne] argument is missing")
        exit(1)
    if broker_name not in ["Zerodha", "AngelOne"]:
        print("broker_name must be in [Zerodha/AngelOne]")
        exit(1)

    if broker_name == "Zerodha":
        ZBroker().generate_token()
    elif broker_name == "AngelOne":
        angle_one = AngelBroker(["minute"], None)

    