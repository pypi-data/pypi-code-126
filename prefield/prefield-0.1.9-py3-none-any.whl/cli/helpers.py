import base64
import configparser
import os
import pathlib
import re
from types import ModuleType
from typing import List, Union

import boto3
import click
import docker


def split_string(s: str) -> List[str]:
    """Split string by comma."""
    return [item.strip() for item in s.split(",") if item.strip()]


def _try_convert_to_numeric(s: str) -> Union[str, float, int]:
    try:
        value = float(s)
    except ValueError:
        return s
    return int(value) if value.is_integer() else value


def split_params(
    ctx: click.Context, param: click.Parameter, value: Union[dict, str]
) -> dict:
    if isinstance(value, dict):
        return value
    else:
        result = {}
        items = split_string(value)
        for item in items:
            parts: List[str] = item.split(":", 1)
            if len(parts) != 2:
                ctx.fail(
                    f"Invalid format of `{param.name}` option: "
                    f"Item `{parts[0]}` must contain "
                    f"a key and a value separated by `:`."
                )
            key = parts[0].strip()
            if not key:
                ctx.fail(
                    f"Invalid format of `{param.name}` option: Parameter key "
                    f"cannot be an empty string."
                )
            value = parts[1].strip()
            result[key] = _try_convert_to_numeric(value)
        return result


def clean_flow_name(flow) -> str:
    """replace all punctuation and spaces with '-'"""
    return re.sub("[^0-9a-zA-Z]+", "-", flow.name).lower()


def get_path(m: ModuleType) -> str:
    module_filepath = m.__file__
    if not module_filepath:
        raise RuntimeError(f"Cannot resolve filepath for {m}")
    path_ = os.path.abspath(module_filepath)
    if isinstance(path_, bytes):
        return path_.decode("utf-8")
    elif isinstance(path_, str):
        return path_
    else:
        raise NotImplementedError(f"method cannot handle path of type {type(path_)}")


def aws_credentials_dict(aws_profile: str) -> dict:
    # pop AWS_PROFILE and load credentials directly
    path = pathlib.PosixPath("~/.aws/credentials")
    config = configparser.RawConfigParser()
    config.read(path.expanduser())

    click.echo(f"Extracting AWS credentials for `{aws_profile}` as a dict")
    aws_access_key_id = config.get(aws_profile, "aws_access_key_id")
    aws_secret_access_key = config.get(aws_profile, "aws_secret_access_key")
    aws_session_token = config.get(aws_profile, "aws_session_token")
    sts = boto3.client(
        "sts",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
    )
    try:
        sts.get_caller_identity()
    except Exception:
        raise EnvironmentError(f"AWS credentials for {aws_profile} expired")

    return {
        "AWS_ACCESS_KEY_ID": aws_access_key_id,
        "AWS_SECRET_ACCESS_KEY": aws_secret_access_key,
        "AWS_SESSION_TOKEN": aws_session_token,
    }


def docker_ecr_login(aws_credentials: dict) -> None:
    ecr = boto3.client(
        "ecr",
        aws_access_key_id=aws_credentials.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=aws_credentials.get("AWS_SECRET_ACCESS_KEY"),
        aws_session_token=aws_credentials.get("AWS_SESSION_TOKEN"),
    )

    # login to AWS ECR in order to be able to push the image
    ecr_resp = ecr.get_authorization_token()
    token = ecr_resp["authorizationData"][0]["authorizationToken"]
    registry = ecr_resp["authorizationData"][0]["proxyEndpoint"]
    registry_url = registry.replace("https://", "")

    token = base64.b64decode(token).decode()
    ecr_username, ecr_password = token.split(":")

    docker_client = docker.client.from_env()
    _ = docker_client.login(
        username=ecr_username, password=ecr_password, registry=registry_url
    )
