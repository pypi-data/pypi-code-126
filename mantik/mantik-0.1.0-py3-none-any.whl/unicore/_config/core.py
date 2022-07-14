import dataclasses
import os
import re
import typing as t

import mantik.unicore._config._base as _base
import mantik.unicore._config._utils as _utils
import mantik.unicore._config.resources as _resources
import mantik.utils.env as env

_USERNAME_ENV_VAR = "MANTIK_UNICORE_USERNAME"
_PASSWORD_ENV_VAR = "MANTIK_UNICORE_PASSWORD"
_PROJECT_ENV_VAR = "MANTIK_UNICORE_PROJECT"
_MLFLOW_ENV_VAR_PREFIX = "MLFLOW_"


@dataclasses.dataclass
class Config(_base.ConfigObject):
    """The backend config for the UNICORE MLflow backend."""

    api_url: str
    user: str
    password: str
    project: str
    resources: _resources.Resources
    singularity_image: t.Optional[str] = None
    environment: t.Optional[dict] = None

    @classmethod
    def _from_dict(cls, config: t.Dict) -> "Config":
        api_url = _utils.get_required_config_value(
            name="UnicoreApiUrl",
            value_type=str,
            config=config,
        )
        user = env.get_required_env_var(_USERNAME_ENV_VAR)
        password = env.get_required_env_var(_PASSWORD_ENV_VAR)
        project = env.get_required_env_var(_PROJECT_ENV_VAR)
        resources = _resources.Resources.from_dict(
            _utils.get_required_config_value(
                name="Resources",
                value_type=dict,
                config=config,
            )
        )
        singularity_image = _utils.get_optional_config_value(
            name="SingularityImage",
            value_type=str,
            config=config,
        )
        environment = _utils.get_optional_config_value(
            name="Environment",
            value_type=dict,
            config=config,
        )
        return cls(
            api_url=api_url,
            user=user,
            password=password,
            project=project,
            resources=resources,
            singularity_image=singularity_image,
            environment=environment,
        )

    def __post_init__(self):
        """Add all MLflow environment variables to the environment."""
        self.environment = _add_mlflow_env_vars(self.environment)

    @property
    def provides_singularity_image(self) -> bool:
        """Return if the config provides the path to a Singularity image."""
        return self.singularity_image is not None

    def _to_dict(self) -> t.Dict:
        key_values = {
            "Project": self.project,
            "Resources": self.resources,
            "Environment": self.environment,
        }
        return _utils.create_dict_with_not_none_values(**key_values)


def _add_mlflow_env_vars(environment: t.Optional[t.Dict]) -> t.Optional[t.Dict]:
    mlflow_env_vars = _get_mlflow_env_vars()
    if mlflow_env_vars:
        if environment is None:
            return mlflow_env_vars
        return {**mlflow_env_vars, **environment}
    return environment


def _get_mlflow_env_vars() -> t.Dict:
    pattern = re.compile(rf"{_MLFLOW_ENV_VAR_PREFIX}\w+")
    return {
        key: value for key, value in os.environ.items() if pattern.match(key)
    }
