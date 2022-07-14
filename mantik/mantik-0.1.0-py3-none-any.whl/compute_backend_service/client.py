import dataclasses
import json
import logging
import pathlib
import typing as t

import mantik
import mantik.compute_backend_service.api as api
import mantik.tracking._server.tokens as _tokens
import mantik.tracking.track as track
import mantik.unicore._config.core as core
import mantik.utils as utils
import requests

logger = logging.getLogger(__name__)

_DEFAULT_COMPUTE_BACKEND_API_PATH = "/compute-backend"


@dataclasses.dataclass
class ComputeBackendClient:
    """Client for the compute backend.

    Parameters
    ----------
    compute_backend_url : str
        URL of the compute backend API.
    unicore_username : str
        UNICORE username.
    unicore_password : str
        Password for the respective UNICORE user.
    unicore_project : str
        Project to use for the compute budget.
    mlflow_tracking_uri : str
        URI of the MLflow tracking server.
    mlflow_tracking_token : str
        Authentication token for the MLflow tracking server.
    api_path : str, default="/compute-backend"
        API path of the compute backend.
        E.g. if `compute_backend_url="https://<host>.com"`, but the actual API
        listens at `https://<host>.com/any/path`, this path can be given here,
        i.e. `api_path=/any/path`.

    """

    compute_backend_url: str
    unicore_username: str
    unicore_password: str
    unicore_project: str
    mlflow_tracking_uri: str
    mlflow_tracking_token: str
    api_path: str = _DEFAULT_COMPUTE_BACKEND_API_PATH

    @classmethod
    def from_env(
        cls, api_path: str = _DEFAULT_COMPUTE_BACKEND_API_PATH
    ) -> "ComputeBackendClient":
        """Create from environment variables."""
        unicore_username = mantik.utils.env.get_required_env_var(
            core._USERNAME_ENV_VAR
        )
        unicore_password = mantik.utils.env.get_required_env_var(
            core._PASSWORD_ENV_VAR
        )
        unicore_project = mantik.utils.env.get_required_env_var(
            core._PROJECT_ENV_VAR
        )
        mlflow_tracking_uri = mantik.utils.env.get_required_env_var(
            utils.mlflow.TRACKING_URI_ENV_VAR
        )
        mantik.tracking.track.init_tracking()
        tokens = _tokens.Tokens.from_file(track._MANTIK_TOKEN_FILE)
        return cls(
            compute_backend_url=mlflow_tracking_uri,
            unicore_username=unicore_username,
            unicore_password=unicore_password,
            unicore_project=unicore_project,
            mlflow_tracking_uri=mlflow_tracking_uri,
            mlflow_tracking_token=tokens.access_token,
            api_path=api_path,
        )

    @property
    def url(self) -> str:
        """Return the API URL of the compute backend."""
        return utils.urls.ensure_https_and_remove_double_slashes_from_path(
            f"{self.compute_backend_url}{self.api_path}"
        )

    @property
    def submit_url(self) -> str:
        """Return the API URL for the submit endpoint."""
        return utils.urls.ensure_https_and_remove_double_slashes_from_path(
            f"{self.url}{api.SUBMIT_PATH}"
        )

    def submit_run(
        self,
        experiment_id: int,
        mlproject_path: pathlib.Path,
        mlflow_parameters: t.Dict,
        backend_config_path: str,
        entry_point: str = "main",
    ) -> requests.Response:
        """Submit a run.

        Parameters
        ----------
        experiment_id : int
            ID of the tracking experiment.
        mlproject_path : pathlib.Path
            Path to the MLproject directory.
        mlflow_parameters : dict
            Parameters to pass to the MLproject.
        backend_config_path : str
            Path within the MLproject directory to the backend config.
            E.g. `backend-config.json`.
        entry_point : str, default="main"
            Name of the entry point to execute.

        Returns
        -------
        requests.Response
            The response of the compute backend.

        """
        logger.debug(
            "Submitting MLproject %s for experiment %s",
            mlproject_path,
            experiment_id,
        )
        data = self._generate_request_data(
            entry_point=entry_point,
            mlflow_parameters=mlflow_parameters,
            unicore_backend_config_path=backend_config_path,
        )
        logger.debug("Sending request to compute backend %s", self.submit_url)
        return requests.post(
            url=f"{self.submit_url}/{experiment_id}",
            headers=self._generate_headers(),
            data=data,
            files=_generate_request_files(mlproject_path),
        )

    def _generate_headers(self):
        return {
            "Authorization": f"Bearer {self.mlflow_tracking_token}",
            "Accept": "application/json",
        }

    def _generate_request_data(
        self,
        entry_point: str,
        mlflow_parameters: t.Dict,
        unicore_backend_config_path: str,
    ) -> t.Dict:
        return {
            "entry_point": entry_point,
            "mlflow_parameters": json.dumps(mlflow_parameters),
            "unicore_user": self.unicore_username,
            "unicore_password": self.unicore_password,
            "unicore_project": self.unicore_project,
            "unicore_backend_config": unicore_backend_config_path,
            "mlflow_tracking_uri": self.mlflow_tracking_uri,
            "mlflow_tracking_token": self.mlflow_tracking_token,
        }


def _generate_request_files(mlproject_path: pathlib.Path) -> t.Dict:
    logger.debug("Zipping MLproject directory")
    zipped = utils.zip.zip_directory(mlproject_path)
    return {"mlproject_zip": zipped.read()}
