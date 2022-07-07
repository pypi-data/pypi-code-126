import json
import os


def fargate_secret(name: str = "val", key: str = "value"):
    """Retrieve secret from SecretsManager that was injected when creating a Fargate
    task using Terraform. During injection of env variable the name is the original
    name that was used in the secrets list, but SecretsManager still accepts
    key:value pairs. Our notation will be to use {value: <value>} when setting the
    value of the secret on AWS console"""
    s: dict = json.loads(os.getenv(name, "{}"))

    return s.get(key)
