import os

import click

from .helpers import aws_credentials_dict

QUIET_ARG_HELP = """Flag denoting if docker build/push commands should be printed"""
CACHE_ARG_HELP = """If cached images should be used when building the docker image"""
PUSH_ARG_HELP = """Bool denoting if docker image should be pulled from ECR"""
TYPE_ARG_HELP = """Agent type to run locally"""
IMAGE_NAME_HELP = """Docker image name. Should be matching an ECR repo"""
AGENT_NAME_HELP = """Prefect Agent name to show in the Prefect Cloud UI. Note that this
                will be suffixed by -{ENV}"""


@click.group(help="Util creating Docker Image for Fargate Agents and pushing to ECR")
def agent():
    pass


@agent.command(help="For executing flows with ECSRun()")
@click.option(
    "--image-name",
    required=False,
    type=str,
    default="uk-prefect-agent",
    show_default=True,
    help=IMAGE_NAME_HELP,
)
@click.option(
    "--agent-name",
    required=False,
    type=str,
    default="fargate-agent",
    show_default=True,
    help=AGENT_NAME_HELP,
)
@click.option(
    "--env",
    required=False,
    type=click.Choice(["dev", "qa", "prod"], case_sensitive=False),
    default="dev",
    show_default=True,
    help="AWS/Prefect environment",
)
@click.option(
    "--quiet", is_flag=True, default=False, show_default=True, help=QUIET_ARG_HELP
)
@click.option("--cache/--no-cache", default=True, help=CACHE_ARG_HELP)
@click.option("--push/--no-push", default=False, show_default=True, help=PUSH_ARG_HELP)
def docker_build(image_name, agent_name, env, quiet, cache, push):
    click.echo(f"Building docker image `{image_name}` for agent `{agent_name}-{env}`")
    from pathlib import Path

    from docker import client

    docker_client = client.from_env()
    image, build_logs = docker_client.images.build(
        path=os.path.join(Path(__file__).parents[1].absolute(), "agent"),
        tag=image_name,
        quiet=quiet,
        nocache=not cache,
        buildargs={"ENV": env, "AGENT_NAME": agent_name},
    )
    if not quiet:
        for chunk in build_logs:
            if "stream" in chunk:
                for line in chunk["stream"].splitlines():
                    click.echo(line)
    click.echo(f"Image with tag {image.tags[0]} successfully built")

    if push:
        from .helpers import docker_ecr_login

        aws_credentials = aws_credentials_dict(os.getenv("AWS_PROFILE"))
        docker_ecr_login(aws_credentials)
        # construct ECR repo url using account id and region
        aws_account_id = os.getenv("AWS_ACCOUNT_ID")
        aws_region = os.getenv("AWS_REGION")
        registry_url = f"{aws_account_id}.dkr.ecr.{aws_region}.amazonaws.com/"
        click.echo(f"push={push} -> will push image {image.tags[0]} to {registry_url}")

        ecr_repo_name = os.path.join(registry_url, image_name)
        image.tag(ecr_repo_name, tag="latest")
        # push image to AWS ECR
        push_log = docker_client.images.push(
            ecr_repo_name, tag="latest", stream=True, decode=True
        )
        if not quiet:
            for line in push_log:
                status = line.get("status")
                progress = line.get("progress")
                id_ = line.get("id")
                objs = [i for i in (status, progress, id_) if i]
                print_ = ": ".join(objs)
                click.echo(print_)
