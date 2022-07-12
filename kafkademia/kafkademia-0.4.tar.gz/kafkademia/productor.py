from .ejemplos import ATM, Venta
import json
from kafka import KafkaProducer
import random
from time import sleep, time

class Productor(object):
    def __init__(self, bootstrap_servers:str, topico:str):
        self.bootstrap_servers = bootstrap_servers
        self.topico = topico
        # Esto permite instanciar el productor de Kafka con la lista de
        # bootstrap_servers. Mas parámetros se pueden encontrar en:
        #  https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html#
        self.productor = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            # Los mensajes se serializan en formato JSON
            value_serializer=lambda m: json.dumps(m).encode("utf-8"),
        )

    def producir(self, atm, ventas, delay=True):
        if atm:
            ej = ATM()
        elif ventas:
            ej = Venta()
        
        while True:
            if delay:
                # Esperamos entre 1 y 5 segundos para producir un mensaje.
                sleep(random.randint(1, 5))
            mensaje = ej.generar_mensaje()
            print(json.dumps(mensaje))
            self.productor.send(
                self.topico,
                mensaje
            )