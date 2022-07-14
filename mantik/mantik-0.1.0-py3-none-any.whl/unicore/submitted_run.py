import logging
import typing as t

import mlflow.entities as entities
import mlflow.projects as projects
import pyunicore.client as pyunicore

logger = logging.getLogger(__name__)


class SubmittedUnicoreRun(projects.SubmittedRun):
    """A run that was submitted through the UNICORE interface.

    This class encapsulates a UNICORE job.

    Parameters
    ----------
    run_id : str
        MLflow run ID.
    job : pyunicore.client.Job
        The UNICORE job.

    """

    def __init__(self, run_id: str, job: pyunicore.Job):
        self._id = run_id
        self._job = job

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"run_id={self.run_id}, "
            f"job={self._job_id}"
            ")"
        )

    @property
    def _status(self) -> str:
        status = self._job.properties["status"]
        logger.debug(f"UNICORE status of {self} is {status}")
        return status

    @property
    def _job_id(self) -> str:
        return self._job.job_id

    @property
    def properties(self) -> str:
        """Return the UNICORE job properties."""
        properties = self._job.properties
        logger.debug(f"Job properties for {self}: {properties}")
        return properties

    @property
    def working_directory(self) -> pyunicore.PathDir:
        """Return the UNICORE working directory of the job."""
        return self._job.working_dir

    @property
    def logs(self) -> t.List[str]:
        """Return the UNICORE job logs."""
        return self.properties["log"]

    @property
    def run_id(self) -> str:
        """Return the run's ID."""
        return self._id

    def wait(self) -> bool:
        """Wait for the run to finish.

        Returns
        -------
        bool
            `True` if the run has finished successfully, `False` otherwise.

        """
        logger.info(f"Waiting for {self} to finish")
        self._job.poll()
        return self._status == _UnicoreJobStatus.SUCCESSFUL

    def get_status(self) -> entities.RunStatus:
        """Return the status of the run."""
        status = _MLFLOW_STATUS_MAPPING[self._status]
        logger.debug(f"Status of {self} is {status}")
        return status

    def cancel(self) -> None:
        """Cancel the run and wait until it was successfully terminated."""
        logger.debug(f"Cancelling UNICORE job for {self}")
        self._job.abort()

    def read_file_from_working_directory(self, filename: str) -> str:
        """Read a file from the job's working directory."""
        logger.debug(f"Reading '{filename}' from working directory of {self}")
        file = self.working_directory.stat(filename)
        content = file.raw().read()
        return content


class _UnicoreJobStatus:
    """Job statuses returned by the UNICORE API."""

    STAGING_IN = "STAGINGIN"
    READY = "READY"
    QUEUED = "QUEUED"
    STAGING_OUT = "STAGINGOUT"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


_MLFLOW_STATUS_MAPPING = {
    _UnicoreJobStatus.STAGING_IN: entities.RunStatus.SCHEDULED,
    _UnicoreJobStatus.READY: entities.RunStatus.SCHEDULED,
    _UnicoreJobStatus.QUEUED: entities.RunStatus.SCHEDULED,
    _UnicoreJobStatus.STAGING_OUT: entities.RunStatus.RUNNING,
    _UnicoreJobStatus.SUCCESSFUL: entities.RunStatus.FINISHED,
    _UnicoreJobStatus.FAILED: entities.RunStatus.FAILED,
    _UnicoreJobStatus.UNKNOWN: entities.RunStatus.RUNNING,
}
