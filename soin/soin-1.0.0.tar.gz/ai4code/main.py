import logging
import time

import redis
from ai4code.reqs import kernels, kernel_versions
from soin.base import Spider
from soin.job import RedisQueue, SpiderJob
from soin.utils import download_file, retry, setup_logger, setup_root


# 定义 Custom Job
class KernelFetch(SpiderJob):

    result: bytes

    def __init__(self, spider: Spider, kernel_id : str):
        super().__init__()
        self.kernel_id = str(kernel_id)
        self.spider = spider

    @retry(5)
    def perform(self):
        versions = kernel_versions.make(data={"kernelId": self.kernel_id}).json()
        run_id = versions['items'][0]['run']['id']
        return download_file(f"https://www.kaggle.com/kernels/scriptcontent/{run_id}/download")

    def handle_result(self):
        (self.spider.root / f"{self.kernel_id}.json").write_bytes(self.result)


class TestJob(SpiderJob):

    def perform(self):
        return "xxxxxx".encode()


class Main(Spider):

    def setup(self):
        self.root = setup_root("./ai4code_data")
        self.redis_client = redis.Redis(host='localhost', port=6379)
        self.dispatch_queue = RedisQueue("dispatch_queue", self.redis_client)
        self.writeback_queue = RedisQueue("writeback_queue", self.redis_client)
        setup_logger(self.root / "log.txt", level=logging.DEBUG)

    def run(self):
        while True:
            if self.stop:
                break
            time.sleep(3)
            logging.info("main is running")
            self.dispatch_queue.push(TestJob())


# # 全局 setup
# root = setup_root("./ai4code_data")
# setup_logger(root / "log.txt", level=logging.DEBUG)
# redis_client = redis.Redis(host='localhost', port=6379)
# queue = RedisQueue("test_task", redis_client)


# # 定义 Custom Job
# class KernelFetch(SpiderJob):

#     result: bytes

#     queue = queue

#     def __init__(self, kernel_id : str):
#         super().__init__()
#         self.kernel_id = str(kernel_id)

#     @retry(5)
#     def perform(self):
#         versions = kernel_versions.make(data={"kernelId": self.kernel_id}).json()
#         run_id = versions['items'][0]['run']['id']
#         return download_file(f"https://www.kaggle.com/kernels/scriptcontent/{run_id}/download")

#     def handle_result(self):
#         (root / f"{self.kernel_id}.json").write_bytes(self.result)


# # 爬虫的主逻辑
# def main():
#     response = kernels.make(data={"page": 1})
#     kernel_ids = response.json()["kernelIds"]

#     versions = kernel_versions.make(data={"kernelId": kernel_ids[0]}).json()
#     run_id = versions['items'][0]['run']['id']
#     download_file(f"https://www.kaggle.com/kernels/scriptcontent/{run_id}/download", root / "test.ipynb")
