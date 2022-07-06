from datetime import datetime, timedelta
import enum
import os
import pickle
import typing
import soin

import redis


class JobStatus(enum.Enum):
    success: 0
    failed: 1


class SpiderJob:

    # 爬虫
    if typing.TYPE_CHECKING:
        spider: soin.Spider

    # perform 完成后对该 Job 设置 result
    result: typing.Any

    # 任务状态
    status: JobStatus

    # 任务运行时间
    execution_time: timedelta

    # 节点
    hostname: str

    def __init__(self):
        self.result = None
        self.status = None
        self.execution_time = None

    def execute(self):
        self.hostname = os.uname().nodename
        before_execute = datetime.now()
        self.result = self.perform()
        self.execution_time = datetime.now() - before_execute

    def perform(self):
        """运行在子节点 worker 中的逻辑
        """
        pass

    def handle_result(self):
        """运行在主节点 worker 中的逻辑
        """
        pass


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
        return pickle.loads(results[1])
