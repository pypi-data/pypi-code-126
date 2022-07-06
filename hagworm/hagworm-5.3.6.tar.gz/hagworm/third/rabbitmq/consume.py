# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import aio_pika


class RabbitMQConsumer(aio_pika.RobustConnection):
    """RabbitMQ消费者
    """

    def __init__(self, url, **kwargs):

        super().__init__(url, **kwargs)

        self._channel = None
        self._queue = None

    @property
    def current_channel(self):

        return self._channel

    @property
    def current_queue(self):

        return self._queue

    async def initialize(self, queue_name, consume_qos=1, *, queue_config=None):

        await self.connect()
        await self.ready()

        self._channel = await self.channel()
        await self._channel.set_qos(prefetch_count=consume_qos)

        if queue_config is None:
            self._queue = await self._channel.declare_queue(queue_name)
        else:
            self._queue = await self._channel.declare_queue(queue_name, **queue_config)

    async def release(self):

        await self._channel.close()
        await super().close()

    async def get(self, *, no_ack=False, timeout=1):

        await self._queue.get(no_ack=no_ack, timeout=timeout)

    async def consume(self, consume_func, *, no_ack=False):

        await self._queue.consume(consume_func, no_ack=no_ack)


class RabbitMQConsumerForExchange(RabbitMQConsumer):
    """RabbitMQ注册到交换机的消费者(默认生成排它队列注册)
    """

    def __init__(self, url, **kwargs):
        
        super().__init__(url, **kwargs)

        self._exchange = None

    @property
    def current_exchange(self):

        return self._exchange

    async def initialize(self, exchange_name, consume_qos=1, *, queue_config=None, routing_key=None):

        await self.connect()
        await self.ready()

        self._channel = await self.channel()
        await self._channel.set_qos(prefetch_count=consume_qos)

        if queue_config is None:
            self._queue = await self._channel.declare_queue(exclusive=True)
        else:
            self._queue = await self._channel.declare_queue(**queue_config)

        self._exchange = await self._channel.get_exchange(exchange_name)

        await self._queue.bind(self._exchange, routing_key)
