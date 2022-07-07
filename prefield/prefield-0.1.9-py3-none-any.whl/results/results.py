from types import FunctionType
from typing import Callable, Optional, Union

from prefect.engine.results import LocalResult, S3Result
from prefect.engine.serializers import Serializer


def construct_local_or_s3_result(
    env: str,
    local_dir: str,
    bucket: str,
    location: Union[str, Callable],
    serializer: Optional[Serializer] = None,
) -> Union[LocalResult, S3Result]:
    """
    A method returning a Prefect LocalResult or S3Result object according to:
      - LocalResult when env variable ENV="local"
      - S3Result otherwise

    Parameters
    ----------
    - env (str): one of local/dev/prod
    - local_dir: dir where local results will be saved as loc
    - dir_or_bucket (str): top level directory for LocalResult, s3 bucket for S3Result
    - location (str): filepath (excluding local_dir) or s3 key
    - serializer (prefect.engine.serializers.Serializer) for loading/ saving result

    Returns
    -------
    prefect.engine.results LocalResult or S3Result object
    """
    if env == "local":
        # if name template is a string (not a function) add the bucket at the beginning
        # of the string
        if not isinstance(location, FunctionType):
            location = f"{bucket}/{location}"
        return LocalResult(dir=local_dir, location=location, serializer=serializer)
    else:
        return S3Result(
            bucket=bucket,
            location=location,
            serializer=serializer,
        )
