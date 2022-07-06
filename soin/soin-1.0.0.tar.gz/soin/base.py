import logging
from pathlib import Path
import signal
import threading
import time
from soin.job import Queue


class Spider:

    root: Path
    dispatch_queue: Queue
    writeback_queue: Queue
    stop: bool

    def __init__(self):
        self.stop = False

        signal.signal(signal.SIGINT, self._handle_sig)
        signal.signal(signal.SIGTERM, self._handle_sig)

    def main(self):
        raise NotImplementedError()

    def spawn_worker_thread(self):
        self.job_result_thread = threading.Thread(target=self._job_result_worker)
        self.job_result_thread.start()

    def _job_result_worker(self):
        """线程中运行"""
        while True:
            if self.stop:
                break
            job = self.writeback_queue.pop()
            logging.info(f"get writeback job: {job}")
            if job is None:
                continue
            job.handle_result()
            time.sleep(1)

    def as_worker(self):
        while True:
            if self.stop:
                break
            job = self.dispatch_queue.pop()
            if job is None:
                continue
            logging.info(f"got job {job}")
            try:
                job.perform()
            except Exception as e:
                logging.error(f"unexpected error from job: {e}")
            self.writeback_queue.push(job)
            logging.info(f"{job} has been successfully processed")
            time.sleep(1)

    def _handle_sig(self, *args):
        logging.info("about to quit")
        self.stop = True
