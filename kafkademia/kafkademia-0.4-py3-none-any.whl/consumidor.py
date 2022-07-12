from kafka import KafkaConsumer

class Consumidor(object):
    def __init__(self, bootstrap_servers:str, topico:str):
        self.bootstrap_servers = bootstrap_servers
        self.topico = topico
        # Esto permite instanciar el consumidor de Kafka con la lista de
        # bootstrap_servers y el topico. Mas parámetros se pueden encontrar en:
        #  https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#
        self.consumidor = KafkaConsumer(
            topico,
            bootstrap_servers=bootstrap_servers.split(","),
            auto_offset_reset='earliest', # Trae todos los mensajes disponibles
            enable_auto_commit=False
        )

    def consumir(self):
        for msg in self.consumidor:
            print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition,
                                          msg.offset, msg.key,
                                          msg.value))