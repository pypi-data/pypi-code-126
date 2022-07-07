import logging
from pathlib import Path
import pickle
import signal
import threading
import time
from typing import Dict
from soin.job import JobStatus, Queue, SpiderJob
from soin.utils import while_true


class Spider:

    root: Path
    stop: bool
    failed_job_dir: Path
    dispatch_queue: Queue
    writeback_queue: Queue
    state: Dict

    def __init__(self):
        self.state_file = self.root / "spider_state.pkl"
        self.state_save_lock = threading.Lock()
        self.state_read_lock = threading.Lock()
        self.stop = False
        self.state = {}
        self.failed_job_dir = self.root / "failed_jobs"
        self.failed_job_dir.mkdir(parents=True, exist_ok=True)
        self.worker_execute_time = 0
        signal.signal(signal.SIGINT, self._handle_sig)
        signal.signal(signal.SIGTERM, self._handle_sig)
        self.setup()

    def main(self):
        try:
            self.load_state()
            self.spawn_cleanup_thread()
            self.spawn_worker_thread()
            self.run()
        finally:
            self.job_result_thread.join()
            self.job_cleanup_thread.join()
            self.cleanup()

    def run(self):
        raise NotImplementedError()

    def setup(self):
        pass

    def cleanup(self):
        self.save_state()

    def save_state(self):
        self.state_save_lock.acquire()
        self.state_file.write_bytes(pickle.dumps(self.state))
        self.state_save_lock.release()

    def load_state(self):
        self.state_read_lock.acquire()
        try:
            self.state = pickle.loads(self.state_file.read_bytes())
        except Exception as e:
            logging.warn(f"load state failed with {e}")
        self.state_read_lock.release()

    def dispatch(self, job: SpiderJob):
        self.dispatch_queue.push(job)

    def spawn_worker_thread(self):
        self.job_result_thread = threading.Thread(target=self._job_result_worker)
        self.job_result_thread.start()

    def spawn_cleanup_thread(self):
        self.job_cleanup_thread = threading.Thread(target=self._job_cleanup_worker)
        self.job_cleanup_thread.start()

    @while_true(10)
    def _job_cleanup_worker(self):
        logging.info("start to cleanup failed jobs")
        for failed_job_file in self.failed_job_dir.glob("*"):
            job = pickle.loads(failed_job_file.read_bytes())
            failed_job_file.unlink()
            logging.info(f"retry failed job {job}")
            self.dispatch(job)
            time.sleep(1)
        logging.info("cleanup done")

    @while_true(1)
    def _job_result_worker(self):
        """线程中运行"""
        job : SpiderJob = self.writeback_queue.pop()
        if job is None:
            return
        logging.info(f"get writeback job: {job}")
        if job.status == JobStatus.success:
            job.on_success()
        if job.status == JobStatus.failed:
            job.on_failed()
            logging.warn(f"job failed with message: {job.message}")
            self._save_failed_job(job)

    def _save_failed_job(self, job: SpiderJob):
        (self.failed_job_dir / job.id).write_bytes(pickle.dumps(job))

    def as_worker(self, max_step=None):
        execute_count = 0
        while True:
            time.sleep(1)
            execute_count += 1
            if self.stop:
                break
            if execute_count == max_step:
                self.stop = True
                logging.info(f"exceed max execution step {execute_count}, quit")
                break
            job : SpiderJob = self.dispatch_queue.pop()
            if job is None:
                continue
            logging.info(f"got job {job}")
            job.execute()
            self.writeback_queue.push(job)
            logging.info(f"{job} has been processed")

    def _handle_sig(self, *args):
        logging.info("about to quit")
        self.stop = True
