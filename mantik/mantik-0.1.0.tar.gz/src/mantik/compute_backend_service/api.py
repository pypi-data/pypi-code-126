"""API routes for compute backend service."""
import io
import json
import typing as t

import fastapi
import mantik.compute_backend_service._bearer as _bearer
import mantik.compute_backend_service.backend as backend
import mantik.compute_backend_service.models as models

TOKEN_VERIFIER = _bearer.JWTBearer()

SUBMIT_PATH = "/submit"

router = fastapi.APIRouter(dependencies=[fastapi.Depends(TOKEN_VERIFIER)])


@router.post(f"{SUBMIT_PATH}/{{experiment_id}}", status_code=201)
async def submit_run(
    experiment_id: str,
    entry_point: str = fastapi.Form(...),
    mlflow_parameters: t.Optional[str] = fastapi.Form(None),
    unicore_user: str = fastapi.Form(...),
    unicore_project: str = fastapi.Form(...),
    unicore_password: str = fastapi.Form(...),
    unicore_backend_config_path: str = fastapi.Form("unicore-config.json"),
    mlflow_tracking_uri: str = fastapi.Form(...),
    mlflow_tracking_token: str = fastapi.Form(...),
    mlproject_zip: fastapi.UploadFile = fastapi.File(...),
) -> models.SubmitRunResponse:
    """
    Submit a run for execution.

    Parameters
    ----------
    experiment_id: Experiment ID.
    entry_point: Mlflow project entry point.
    mlflow_parameters: Mlflow project parameters as string holding json.
    unicore_user: UNICORE username.
    unicore_project: UNICORE compute project.
    unicore_password: UNICORE password.
    unicore_backend_config_path: Path to UNICORE backend config in zip file.
    mlproject_zip: Zipped Mlflow project directory.

    Returns
    -------
    RunSubmitResponse.

    Notes
    -----
    Credentials for UNICORE are submitted here. They are protected iff https
      is enabled, since form data are encrypted.
    Since we have no build service (so far) only zipped directories can be
      submitted.
    """
    parameters_json = json.loads(mlflow_parameters)
    zipped = await mlproject_zip.read()
    response = backend.handle_submit_run_request(
        experiment_id=experiment_id,
        entry_point=entry_point,
        mlflow_parameters=parameters_json,
        unicore_user=unicore_user,
        unicore_project=unicore_project,
        unicore_password=unicore_password,
        unicore_backend_config_path=unicore_backend_config_path,
        mlflow_tracking_uri=mlflow_tracking_uri,
        mlflow_tracking_token=mlflow_tracking_token,
        mlproject_zip=io.BytesIO(zipped),
    )
    return response
