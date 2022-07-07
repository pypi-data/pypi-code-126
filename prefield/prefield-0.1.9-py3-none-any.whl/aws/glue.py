import logging
import time
import timeit
from typing import List

import boto3

logger = logging.getLogger(__name__)


class GluePartition:
    @property
    def values(self):
        return list(self.__dict__.values())

    @property
    def field_types(self) -> List[str]:
        return [field.__name__ for field in self.__annotations__.values()]


def run_crawler(
    crawler: str, _await: bool = True, timeout_mins: int = 2, refresh_sec: int = 15
) -> dict:
    """
    Run an AWS Glue Crawler to detect a table and/or add partitions

    Parameters
    ----------
    crawler : str
        name of crawler to run

    _await : bool, True
        wait until the outcome of the run is received to complete the task

    timeout_mins : int
        max wait time before a TimeoutError is raised

    refresh_sec : int
        frequency to poll status

    Returns
    -------
    boto3 response as a dictionary

    """
    glue = boto3.client("glue")

    response: dict = glue.start_crawler(Name=crawler)

    if _await:
        timeout_seconds = timeout_mins * 60
        start_time = timeit.default_timer()
        abort_time = start_time + timeout_seconds

        while True:
            state = glue.get_crawler(Name=crawler)["Crawler"]["State"]
            if state == "READY":  # Other known states: RUNNING, STOPPING
                break
            if timeit.default_timer() > abort_time:
                raise TimeoutError(
                    f"Failed to crawl {crawler}. The allocated time of {timeout_mins:,}"
                    f" minutes has elapsed."
                )

            logger.info(f"Crawler:{crawler} in state: {state}")
            time.sleep(refresh_sec)

        logger.info(f"Crawler:{crawler} in state: {state}")
    return response


def run_glue_job(
    job: str,
    bookmark_enabled: bool = True,
    worker_type: str = "Standard",
    n_workers: int = 5,
    timeout_mins: int = 10,
    refresh_sec: int = 15,
) -> dict:
    """
    Run an AWS Glue job

    Parameters
    ----------
    job : str
        name of Glue job to run

    bookmark_enabled : bool, True
        bookmark used to keep track of changed files

    worker_type : str
        The type of predefined worker that is allocated when a job runs. Accepts a
        value of Standard, G.1X, or G.2X.

    n_workers : int
        The number of workers of a defined workerType that are allocated when a job runs

    timeout_mins : int
        max wait time before a TimeoutError is raised

    refresh_sec : int
        frequency to poll status


    Returns
    -------
    boto3 response as a dictionary

    """
    glue = boto3.client("glue")

    job_args = {
        "--enable-continuous-cloudwatch-log": "true",
        "--enable-continuous-log-filter": "true",
    }
    if bookmark_enabled:
        job_args["--job-bookmark-option"] = "job-bookmark-enable"

    response: dict = glue.start_job_run(
        JobName=job,
        # MaxCapacity=n_dpus,
        NumberOfWorkers=n_workers,
        Timeout=timeout_mins,
        WorkerType=worker_type,
        Arguments=job_args,
    )

    while True:
        job_run_id = response["JobRunId"]
        status = glue.get_job_run(JobName=job, RunId=job_run_id)
        state = status["JobRun"]["JobRunState"]
        if state == "SUCCEEDED":
            break
        if state == "FAILED":
            raise RuntimeError(f"Job {job} failed: {status['ErrorMessage']}")
        if state in ["STOPPED", "FAILED", "TIMEOUT"]:
            raise RuntimeError(
                f"Failed to complete {job}. The allocated time of {timeout_mins:,}"
                f" minutes has elapsed."
            )

        logger.info(f"Glue Job:{job} in state: {state}")
        time.sleep(refresh_sec)

    return response


def get_partitions(dbname: str, tblname: str) -> List[dict]:
    """
    Returns the partitions of a Glue table

    Parameters
    ----------
    dbname : str
        name of Glue db

    tblname : str
        name of table

    Returns
    -------
    List of dictionaries, each dictionary representing a single partition

    """
    glue = boto3.client("glue")
    response = glue.get_partitions(DatabaseName=dbname, TableName=tblname)
    partitions = response["Partitions"]
    if partitions:
        next_token = response["NextToken"]
        while next_token:
            response = glue.get_partitions(
                DatabaseName=dbname, TableName=tblname, NextToken=next_token
            )
            next_token = response.get("NextToken")
            partitions += response["Partitions"]

    return partitions
