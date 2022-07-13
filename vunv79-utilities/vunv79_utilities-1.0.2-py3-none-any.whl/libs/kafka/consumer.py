"""
Consume message from topic specify

Usage:

>>> import socket
>>> import json
>>> CONSUMER_CONFIG = {
>>>    'bootstrap.servers': "<host>:<port>",
>>>    'group.id': "[DetectBruteForce]-save",
>>>    "client.id": socket.gethostname(),
>>>    'auto.offset.reset': 'latest'
>>>}
>>>

>>> class DetectBruteForce(BaseConsumer):
>>>    def __init__(self):
>>>        super().__init__(config=CONSUMER_CONFIG)

>>>    def process_msg(self, msg):
>>>        logger.info("Consumed event from topic |{topic}|".format(
>>>            topic=msg.topic()))
>>>        message_text = msg.value().decode('utf-8')
>>>        payload: dict = json.loads(message_text)
>>>        ... # Continue handle
"""
from confluent_kafka import Consumer


# Create logger
from vunv79_utilities.libs.logger.setup import init_logging

logger = init_logging(name="kafka_consumer")


class BaseConsumer:
    def __init__(self, config):
        self.config = config
        self._consumer = Consumer(self.config)

    @staticmethod
    def print_assignment(consumer, partitions):
        logger.info(f'Assignment: {consumer}, {partitions}')

    def process_msg(self, *args, **kwargs):
        ...

    def consume(self, topics):
        try:
            self._consumer.subscribe(topics, on_assign=self.print_assignment)
            while True:
                msg = self._consumer.poll(timeout=1.0)
                if msg is None:
                    continue

                if msg is None:
                    logger.info("Waiting...")
                elif msg.error():
                    logger.info("ERROR: %s".format(msg.error()))
                else:
                    self.process_msg(msg)

        finally:
            # Close down consumer to commit final offsets.
            self._consumer.close()
