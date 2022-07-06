# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Runtime REST adapter."""

import logging
from datetime import datetime
from typing import Dict, Any, List, Union, Optional
import json

from .base import RestAdapterBase
from .program import Program
from .program_job import ProgramJob
from .runtime_session import RuntimeSession
from ...utils import RuntimeEncoder
from ...utils.converters import local_to_utc
from .cloud_backend import CloudBackend

logger = logging.getLogger(__name__)


class Runtime(RestAdapterBase):
    """Rest adapter for Runtime base endpoints."""

    URL_MAP = {
        "programs": "/programs",
        "jobs": "/jobs",
        "backends": "/backends",
    }

    def program(self, program_id: str) -> "Program":
        """Return an adapter for the program.

        Args:
            program_id: ID of the program.

        Returns:
            The program adapter.
        """
        return Program(self.session, program_id)

    def program_job(self, job_id: str) -> "ProgramJob":
        """Return an adapter for the job.

        Args:
            job_id: Job ID.

        Returns:
            The program job adapter.
        """
        return ProgramJob(self.session, job_id)

    def runtime_session(self, session_id: str) -> "RuntimeSession":
        """Return an adapter for the session.

        Args:
            session_id: Job ID of the first job in a session.

        Returns:
            The session adapter.
        """
        return RuntimeSession(self.session, session_id)

    def list_programs(self, limit: int = None, skip: int = None) -> Dict[str, Any]:
        """Return a list of runtime programs.

        Args:
            limit: The number of programs to return.
            skip: The number of programs to skip.

        Returns:
            A list of runtime programs.
        """
        url = self.get_url("programs")
        payload: Dict[str, int] = {}
        if limit:
            payload["limit"] = limit
        if skip:
            payload["offset"] = skip
        return self.session.get(url, params=payload).json()

    def create_program(
        self,
        program_data: str,
        name: str,
        description: str,
        max_execution_time: int,
        is_public: Optional[bool] = False,
        spec: Optional[Dict] = None,
    ) -> Dict:
        """Upload a new program.

        Args:
            program_data: Program data (base64 encoded).
            name: Name of the program.
            description: Program description.
            max_execution_time: Maximum execution time.
            is_public: Whether the program should be public.
            spec: Backend requirements, parameters, interim results, return values, etc.

        Returns:
            JSON response.
        """
        url = self.get_url("programs")
        payload = {
            "name": name,
            "data": program_data,
            "cost": max_execution_time,
            "description": description,
            "is_public": is_public,
        }
        if spec is not None:
            payload["spec"] = spec
        data = json.dumps(payload)
        return self.session.post(url, data=data).json()

    def program_run(
        self,
        program_id: str,
        backend_name: Optional[str],
        params: Dict,
        image: Optional[str] = None,
        hub: Optional[str] = None,
        group: Optional[str] = None,
        project: Optional[str] = None,
        log_level: Optional[str] = None,
        session_id: Optional[str] = None,
        job_tags: Optional[List[str]] = None,
        max_execution_time: Optional[int] = None,
        start_session: Optional[bool] = False,
    ) -> Dict:
        """Execute the program.

        Args:
            program_id: Program ID.
            backend_name: Name of the backend.
            params: Program parameters.
            image: Runtime image.
            hub: Hub to be used.
            group: Group to be used.
            project: Project to be used.
            log_level: Log level to use.
            session_id: ID of the first job in a runtime session.
            job_tags: Tags to be assigned to the job.
            max_execution_time: Maximum execution time in seconds.
            start_session: Set to True to explicitly start a runtime session. Defaults to False.

        Returns:
            JSON response.
        """
        url = self.get_url("jobs")
        payload: Dict[str, Any] = {
            "program_id": program_id,
            "params": params,
        }
        if image:
            payload["runtime"] = image
        if log_level:
            payload["log_level"] = log_level
        if backend_name:
            payload["backend"] = backend_name
        if session_id:
            payload["session_id"] = session_id
        if job_tags:
            payload["tags"] = job_tags
        if max_execution_time:
            payload["cost"] = max_execution_time
        if start_session:
            payload["start_session"] = start_session
        if all([hub, group, project]):
            payload["hub"] = hub
            payload["group"] = group
            payload["project"] = project
        data = json.dumps(payload, cls=RuntimeEncoder)
        return self.session.post(url, data=data).json()

    def jobs_get(
        self,
        limit: int = None,
        skip: int = None,
        pending: bool = None,
        program_id: str = None,
        hub: str = None,
        group: str = None,
        project: str = None,
        job_tags: Optional[List[str]] = None,
        session_id: Optional[str] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        descending: bool = True,
    ) -> Dict:
        """Get a list of job data.

        Args:
            limit: Number of results to return.
            skip: Number of results to skip.
            pending: Returns 'QUEUED' and 'RUNNING' jobs if True,
                returns 'DONE', 'CANCELLED' and 'ERROR' jobs if False.
            program_id: Filter by Program ID.
            hub: Filter by hub - hub, group, and project must all be specified.
            group: Filter by group - hub, group, and project must all be specified.
            project: Filter by project - hub, group, and project must all be specified.
            job_tags: Filter by tags assigned to jobs. Matched jobs are associated with all tags.
            session_id: Job ID of the first job in a runtime session.
            created_after: Filter by the given start date, in local time. This is used to
                find jobs whose creation dates are after (greater than or equal to) this
                local date/time.
            created_before: Filter by the given end date, in local time. This is used to
                find jobs whose creation dates are before (less than or equal to) this
                local date/time.
            descending: If ``True``, return the jobs in descending order of the job
                creation date (i.e. newest first) until the limit is reached.

        Returns:
            JSON response.
        """
        url = self.get_url("jobs")
        payload: Dict[str, Union[int, str, List[str]]] = {}
        if limit:
            payload["limit"] = limit
        if skip:
            payload["offset"] = skip
        if pending is not None:
            payload["pending"] = "true" if pending else "false"
        if program_id:
            payload["program"] = program_id
        if job_tags:
            payload["tags"] = job_tags
        if session_id:
            payload["session_id"] = session_id
        if created_after:
            payload["created_after"] = local_to_utc(created_after).isoformat()
        if created_before:
            payload["created_before"] = local_to_utc(created_before).isoformat()
        if descending is False:
            payload["sort"] = "ASC"
        if all([hub, group, project]):
            payload["provider"] = f"{hub}/{group}/{project}"
        return self.session.get(url, params=payload).json()

    # IBM Cloud only functions

    def backend(self, backend_name: str) -> CloudBackend:
        """Return an adapter for the IBM Cloud backend.

        Args:
            backend_name: Name of the backend.

        Returns:
            The backend adapter.
        """
        return CloudBackend(self.session, backend_name)

    def backends(self, timeout: Optional[float] = None) -> Dict[str, List[str]]:
        """Return a list of IBM Cloud backends.

        Args:
            timeout: Number of seconds to wait for the request.

        Returns:
            JSON response.
        """
        url = self.get_url("backends")
        return self.session.get(url, timeout=timeout).json()
