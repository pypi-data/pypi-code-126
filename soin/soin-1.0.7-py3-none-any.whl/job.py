from datetime import datetime, timedelta
import enum
import logging
import os
import pickle
import typing
from uuid import uuid4
import soin

import redis


class JobStatus(enum.Enum):
    success = 0
    failed = 1


class SpiderJob:

    # 爬虫
    if typing.TYPE_CHECKING:
        spider: soin.Spider

    # perform 完成后对该 Job 设置 result
    result: typing.Any

    # 任务状态
    status: JobStatus

    # 任务执行结果信息
    message: str

    # 任务运行时间
    execution_time: timedelta

    # 节点
    hostname: str

    def __init__(self):
        self.id = uuid4().hex
        self.result = None
        self.status = None
        self.message = None
        self.hostname = None
        self.execution_time = None

    def __repr__(self) -> str:
        return f"SpiderJob@{self.id} status:{self.status} message:{self.message} hostname:{self.hostname}"

    __str__ = __repr__

    def set_spider(self, spider: "soin.Spider"):
        self.spider = spider

    def execute(self):
        self.hostname = os.uname().nodename
        before_execute = datetime.now()
        self.status = JobStatus.success
        self.message = "ok"
        try:
            self.result = self.perform()
        except Exception as e:
            self.status = JobStatus.failed
            self.message = str(e)
        self.execution_time = datetime.now() - before_execute

    def perform(self):
        """运行在子节点 worker 中的逻辑
        """
        raise NotImplementedError()

    def on_failed(self):
        raise NotImplementedError()

    def on_success(self):
        """运行在主节点 worker 中的逻辑
        """
        raise NotImplementedError()


class Queue:

    def push(self):
        pass

    def pop(self):
        pass


class RedisQueue(Queue):

    def __init__(self, queue_name, redis: redis.Redis):
        self.queue_name = queue_name
        self.redis = redis

    def push(self, job: SpiderJob):
        job_bytes = pickle.dumps(job)
        self.redis.lpush(self.queue_name, job_bytes)

    def pop(self) -> SpiderJob:
        results = self.redis.brpop(self.queue_name, timeout=3)
        if not results:
            return None
        try:
            return pickle.loads(results[1])
        except Exception as e:
            logging.error(f"pickle job failed: {e}")
            return None
