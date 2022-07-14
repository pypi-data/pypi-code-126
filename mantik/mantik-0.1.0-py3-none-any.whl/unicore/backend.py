import logging
import pathlib
import typing as t

import mantik.unicore._config as _config
import mantik.unicore._connect as _connect
import mantik.unicore.submitted_run as submitted_run
import mantik.utils as utils
import mlflow.projects as projects
import mlflow.projects._project_spec as _project_spec
import mlflow.projects.backend as mlflow_backend
import pyunicore.client as pyunicore
import spython.main

logger = logging.getLogger(__name__)


class UnicoreBackend(mlflow_backend.AbstractBackend):
    """UNICORE backend for running MLflow projects."""

    def run(
        self,
        project_uri: str,
        entry_point: str,
        params: t.Dict,
        version: t.Optional[str],
        backend_config: t.Dict,
        tracking_uri: str,
        experiment_id: str,
    ) -> projects.SubmittedRun:
        """Run an entrypoint.

        It must return a SubmittedRun object to track the execution

        Parameters
        ----------
        project_uri : str
            URI of the project to execute.
            E.g. a local filesystem path or a Git repository URI like
            https://github.com/mlflow/mlflow-example
        entry_point : str
            Entry point to run within the project.
            E.g. for a project that is defined as
            ```yaml
            entry_points:
                main:
                  parameters:
                    print: {type: "string", default: "test"}
                  command: python main.py {print}
            ```
            the `entry_point="main"`.
        params : dict
            Dict of parameters to pass to the entry point.
            For the example entrypoint as above, if the project is run as
            `mlflow run --backend unicore <project path> -P print=hi`, this
            would be `{"print": "hi"}`.
        version : str
            For git-based projects, either a commit hash or a branch name.
        backend_config : dict
            The backend config.
            By default, mlflow passes the following dict
            ```
            {
                'DOCKER_ARGS': {},
                'STORAGE_DIR': None,
                'SYNCHRONOUS': False,
                'USE_CONDA': True,
            }
            ```
            which is extended by the content given in the backend
            config of a user.
        tracking_uri : str
            URI of tracking server against which to log run information.
            E.g. for local tracking this may be
            `'file://<home path>/mantik/mlruns'`
        experiment_id : str
            ID of experiment under which to launch the run.
            E.g. `'0'` for the Default experiment that is created by mlflow..

        Returns
        -------
        mlflow.projects.SubmittedRun

        """
        project_dir, project = _load_project(
            project_uri=project_uri,
            version=version,
            entry_point=entry_point,
            parameters=params,
        )

        run_id = _create_active_run(
            project_uri=project_uri,
            experiment_id=experiment_id,
            project_dir=project_dir,
            version=version,
            entry_point=entry_point,
            parameters=params,
        )

        run = _submit_run(
            run_id=run_id,
            backend_config=backend_config,
            project_dir=project_dir,
            project=project,
            entry_point=entry_point,
            parameters=params,
        )
        return run


def _load_project(
    project_uri: str,
    entry_point: str,
    parameters: t.Dict,
    version: t.Optional[str] = None,
) -> t.Tuple[pathlib.Path, _project_spec.Project]:
    project_dir = pathlib.Path(
        projects.utils.fetch_and_validate_project(
            uri=project_uri,
            version=version,
            entry_point=entry_point,
            parameters=parameters,
        )
    )
    project = projects.utils.load_project(project_dir)
    logger.info(f"Loaded project {project.name}")
    return project_dir, project


def _create_active_run(
    project_uri: str,
    experiment_id: str,
    project_dir: pathlib.Path,
    entry_point: str,
    parameters: t.Dict,
    version: t.Optional[str] = None,
) -> str:
    active_run = projects.utils.get_or_create_run(
        run_id=None,
        uri=project_uri,
        experiment_id=experiment_id,
        work_dir=project_dir,
        version=version,
        entry_point=entry_point,
        parameters=parameters,
    )
    run_id = active_run.info.run_id
    logger.info(f"Created new active run {run_id}")
    return run_id


def _submit_run(
    run_id: str,
    backend_config: t.Dict,
    project_dir: pathlib.Path,
    project: _project_spec.Project,
    entry_point: str,
    parameters: t.Dict,
) -> projects.SubmittedRun:
    job = _prepare_job(
        backend_config=backend_config,
        project_dir=project_dir,
        project=project,
        entry_point=entry_point,
        parameters=parameters,
    )
    job = _start_job(job=job, run_id=run_id)

    submitted = submitted_run.SubmittedUnicoreRun(run_id=run_id, job=job)

    logger.info(f"Submitted run {submitted}")
    return submitted


def _prepare_job(
    backend_config: t.Dict,
    project_dir: pathlib.Path,
    project: _project_spec.Project,
    entry_point: str,
    parameters: t.Dict,
) -> pyunicore.Job:
    config = _config.core.Config.from_dict(backend_config)

    image = _get_singularity_image(
        config=config, project=project, project_dir=project_dir
    )
    files_to_upload = _get_files_to_upload(image=image, project_dir=project_dir)
    logger.debug(f"Prepared upload of files {files_to_upload}")

    client = _connect.create_unicore_api_connection(
        api_url=config.api_url,
        user=config.user,
        password=config.password,
    )

    entry = project.get_entry_point(entry_point)
    storage_dir = backend_config[projects.PROJECT_STORAGE_DIR]
    logger.debug(f"Writing to storage directory {storage_dir}")
    job = _submit_job_in_staging_in_and_upload_input_files(
        client=client,
        entry_point=entry,
        parameters=parameters,
        storage_dir=storage_dir,
        singularity_image=image.name,
        input_files=files_to_upload,
        config=config,
    )
    logger.debug(f"Submitted job {job.job_id} to staging in")
    return job


def _get_singularity_image(
    config: _config.core.Config,
    project: _project_spec.Project,
    project_dir: pathlib.Path,
) -> pathlib.Path:
    if not config.provides_singularity_image:
        docker_image = project.docker_env["image"]
        logger.debug(
            f"No singularity image attached, "
            f"building from docker image {docker_image}."
        )
        return _build_singularity_image(
            docker_image=docker_image,
            project_dir=project_dir,
        )
    else:
        return project_dir / config.singularity_image


def _build_singularity_image(
    docker_image: str,
    project_dir: pathlib.Path,
) -> pathlib.Path:
    """Build the Singularity image.

    Requires sudo rights, which are asked from the stdin.

    """
    if _bootstrap_not_given(docker_image):
        docker_image = f"docker-daemon://{docker_image}"
    path = spython.main.Client.build(
        recipe=docker_image,
        build_folder=project_dir,
    )
    return pathlib.Path(path)


def _bootstrap_not_given(image: str) -> bool:
    return "://" not in image


def _get_files_to_upload(image: pathlib.Path, project_dir: pathlib.Path):
    """Get all files to be uploaded via UNICORE.

    Notes
    -----
    Since MLflow docker backend mounts the MLflow project directory, all
    directory contents are uploaded here as well.

    """
    files = [file for file in project_dir.rglob("*") if file.is_file()]
    files.append(image)
    return list(set(files))


def _submit_job_in_staging_in_and_upload_input_files(
    client: pyunicore.Client,
    entry_point: _project_spec.EntryPoint,
    parameters: t.Dict,
    storage_dir: str,
    singularity_image: str,
    input_files: t.List[pathlib.Path],
    config: _config.core.Config,
) -> pyunicore.Job:
    job_description = _create_job_description(
        entry_point=entry_point,
        parameters=parameters,
        storage_dir=storage_dir,
        config=config,
        singularity_image=singularity_image,
    )

    logger.debug(f"Created job description {job_description}")

    job = client.new_job(
        job_description=job_description,
        inputs=input_files,
    )
    return job


def _create_job_description(
    entry_point: _project_spec.EntryPoint,
    parameters: t.Dict,
    storage_dir: str,
    config: _config.core.Config,
    singularity_image: str,
) -> t.Dict:
    singularity_run_command = (
        "srun singularity run "
        "--cleanenv "
        # Pass MLFLOW_TRACKING_URI variable if set, otherwise set to default
        # folder
        # TODO: this should only happen if the nodes have internet access
        # (devel queue)
        f"--env {utils.mlflow.TRACKING_URI_ENV_VAR}="
        f"${{{utils.mlflow.TRACKING_URI_ENV_VAR}:-file://$PWD/mlruns}} "
        # Pass tracking token if set
        f"{_create_optional_env_string(utils.mlflow.TRACKING_TOKEN_ENV_VAR)} "
        # Pass MLFLOW_EXPERIMENT_NAME variable if set
        f"{_create_optional_env_string(utils.mlflow.EXPERIMENT_NAME_ENV_VAR)} "
        # Pass Experiment ID if set
        f"{_create_optional_env_string(utils.mlflow.EXPERIMENT_ID_ENV_VAR)} "
        f"{singularity_image}"
    )
    arguments = _create_arguments(
        entry_point=entry_point, parameters=parameters, storage_dir=storage_dir
    )
    job_description = {
        "Executable": singularity_run_command,
        "Arguments": arguments,
        **config.to_dict(),
    }
    return job_description


def _create_optional_env_string(env_var_name: str) -> str:
    """Create a --env string for singularity command if variable is set."""
    return f"${{{env_var_name}:" f"+--env {env_var_name}=" f"${env_var_name}}}"


def _create_arguments(
    entry_point: _project_spec.EntryPoint, parameters: t.Dict, storage_dir: str
) -> str:
    command_string = (
        entry_point.compute_command(
            user_parameters=parameters,
            storage_dir=storage_dir,
        )
        + " &>>mantik.log 2>&1"
    )
    return command_string.replace(" \\\n ", "").replace("\n", "").split(" ")


def _start_job(job: pyunicore.Job, run_id: str) -> pyunicore.Job:
    job.start()
    logger.info(f"Started job {job.job_id} with run_id {run_id}")
    return job
