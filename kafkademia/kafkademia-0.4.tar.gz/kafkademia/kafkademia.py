__version__="0.4"

import argparse
import json
from .productor import Productor
from .consumidor import Consumidor
from .utils import validar_args

def init(
    topico:str,
    bootstrap_servers:str,
    productor:bool, 
    atm:bool,
    ventas:bool, 
    consumidor:bool
) -> None:
    validar_args(topico, bootstrap_servers, productor, atm, ventas, consumidor)
    args = {
        "topico": topico,
        "bootstrap_servers": bootstrap_servers,
        "productor": productor,
        "atm": atm,
        "ventas": ventas,
        "consumidor": consumidor
    }

    print("Los parametros con los cuales se está corriendo kafkademia son los siguientes:\n\n{}".format(json.dumps(args, indent=4, separators=(',', ': '))))

    if productor:
        p = Productor(bootstrap_servers=bootstrap_servers, topico=topico)
        p.producir(atm, ventas, delay=True)
    
    if consumidor:
        c = Consumidor(bootstrap_servers=bootstrap_servers, topico=topico)
        c.consumir()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topico", type=str)
    parser.add_argument("--bootstrap_servers", type=str)
    ## Si seteamos productor, se tiene que setear atm o ventas
    parser.add_argument("--productor", action="store_true")
    parser.add_argument("--atm", action="store_true")
    parser.add_argument("--ventas", action="store_true")
    parser.add_argument("--consumidor", action="store_true")
    args = vars(parser.parse_args())

    init(**args)