"""
Send message to topic Kafka, specify by topic

Usage:

>>> import socket
>>> config = {
>>>    'bootstrap.servers': "<host>:<port>",
>>>    'client.id': socket.gethostname(),
>>>    'message.max.bytes': 1024 * 1024 * 50
>>> }

>>> producer = KafkaProducer(config=config)
>>> producer.produce(msg="Hello World", topic="tests")


"""
import json
import socket
import sys
from typing import Optional
from confluent_kafka import Producer

# Create logger
from vunv79_utilities.libs.helpers.metaclass import SingletonMeta
from vunv79_utilities.libs.logger.setup import init_logging

logger = init_logging(name="kafka_producer")


class KafkaProducer(metaclass=SingletonMeta):
    def __init__(self, config, debug=False):
        self.producer = Producer(config)
        self.debug = debug
        logger.debug("Initial kafka producer")

    def acked(self, err, msg):
        if err is not None:
            logger.error("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            if self.debug:
                logger.debug("Message produced: %s" % (str(msg)))

    def produce(self, msg, topic: str, key: Optional[str] = None):
        try:
            data_encode = json.dumps(msg,
                                     default=str).encode('utf-8')
            message_bytes = sys.getsizeof(data_encode)  # Get size of data
            self.producer.produce(topic=topic,
                                  key=key,
                                  value=data_encode,
                                  callback=self.acked)
            logger.info(f"Produce message successful to topic: |{topic}| - Key: {key} Bytes: {message_bytes}")
        except Exception as ex:
            logger.error(f"kafka_producer :: produce :: Ex -> {ex}")
        self.producer.poll(1)
