import datetime
import os
import subprocess
from types import ModuleType
from typing import Any, Dict, List, Union

import click
import pandas as pd

from .helpers import clean_flow_name, get_path, split_params

NAME_ARG_HELP = """Prefect Flow Name"""
LABEL_ARG_HELP = """Prefect Agent Label"""
PROJECT_ARG_HELP = """Prefect Project Name to register on Prefect Server/Cloud"""
TARGET_ENV_ARG_HELP = """Defines if results should be written locally or the
corresponding AWS resources"""
EXECUTION_ENV_ARG_HELP = """How to run the flow"""
S3_BUCKET_ARG_HELP = """S3 Bucket to store flow script file when registering flow"""
ECS_TASK_NAME_ARG_HELP = """ECS Task Name that should be used when executing the flow
using a Fargate Agent"""
SERVER_ARG_HELP = """Where flow should be registered: local docker server or on Prefect
Cloud"""
PARAMS_ARG_HELP = """Specify extra parameters that you want to pass
to the context initializer. Items must be separated by comma, keys - by colon,
example: param1:value1,param2:value2. Each parameter is split by the first comma,
so parameter values are allowed to contain colons, parameter keys are not."""
SCHEDULE_ARG_HELP = """If the flow's schedule should be used in the run"""
DATE_PARAM_ARG_HELP = """Name of Prefect Parameter that can be used as the target date
when running a Flow back-fill"""
START_DATE_ARG_HELP = """Date to start back-filling from"""
END_DATE_ARG_HELP = """Date to finish back-filling to (defaults to yesterday)"""
PUSH_ARG_HELP = """Bool denoting if docker image should be pushed to ECR"""
WEEKDAYS_ARG_HELP = """Bool denoting if date range should only include week
days"""


def create_flows_context() -> Dict[str, Dict[str, Union[str, Any]]]:
    """Return a dict {<flow_name>: {path: <flow_file_path>, flow: <flow>}}"""

    flows_path = os.getenv("FLOWS_PATH", "src")
    flows_list: List[ModuleType] = __import__(flows_path).__all_flows__

    return {
        clean_flow_name(getattr(m, "flow")): {
            "path": get_path(m),
            "flow": getattr(m, "flow"),
        }
        for m in flows_list
    }


@click.group(help="Util for viz/registering/running/back-filling flows")
def flow():
    pass


@flow.command()
@click.option("--name", required=True, type=str, help=NAME_ARG_HELP)
def visualize(name):
    click.echo(f"Visualizing flow: {name}")
    flows = create_flows_context()
    flow_dict: dict = flows.get(name)
    f = flow_dict.get("flow")
    f.visualize()


@flow.command()
@click.option("--name", required=True, type=str, help=NAME_ARG_HELP)
@click.option(
    "--env",
    required=False,
    type=click.Choice(["local", "dev", "qa", "prod"], case_sensitive=False),
    default="local",
    show_default=True,
    help=TARGET_ENV_ARG_HELP,
)
@click.option(
    "--server",
    required=False,
    type=click.Choice(["server", "cloud"], case_sensitive=False),
    default="server",
    show_default=True,
    help=SERVER_ARG_HELP,
)
@click.option(
    "--project",
    type=click.Choice(["dev", "prod", "gatewayplatform-qa", "gatewayplatform-prod"], case_sensitive=False),
    default="qa",
    show_default=True,
    help=PROJECT_ARG_HELP,
)
@click.option(
    "--agent",
    required=False,
    type=click.Choice(["local", "fargate"], case_sensitive=False),
    default="local",
    help=EXECUTION_ENV_ARG_HELP,
)
@click.option(
    "--label",
    required=False,
    type=str,
    default="local",
    help=LABEL_ARG_HELP
)
@click.option(
    "--s3-bucket",
    required=False,
    type=str,
    default="platform-default-prefect-task-storage",
    help=S3_BUCKET_ARG_HELP,
)
@click.option(
    "--ecs-task-name",
    required=False,
    type=str,
    default="platform-default-prefect-flow",
    help=ECS_TASK_NAME_ARG_HELP,
)
@click.option(
    "--schedule", required=False, is_flag=True, default=False, help=SCHEDULE_ARG_HELP
)
def register(name, env, server, project, agent, label, s3_bucket, ecs_task_name, schedule):
    os.environ["ENV"] = env
    click.echo(f"Registering `{name}` under project={project} with execution={env} and agent label={label}")

    api_key = None
    if server == "cloud":
        click.echo("NOTE: this will register the flow with Prefect Cloud")
        api_key = os.getenv("PREFECT__CLOUD__API_KEY")
        os.environ["PREFECT__BACKEND"] = "cloud"

    flows = create_flows_context()
    flow_dict: dict = flows.get(name)
    flow_path: str = flow_dict.get("path")
    f = flow_dict.get("flow")

    if agent == "local":
        # registering local flows allowed only for dev and testing
        # forbid registering on prod project or on Prefect Cloud
        if project == "prod" or server == "cloud":
            raise ValueError(
                "Registering flows with LocalRun config allowed only for dev and "
                "testing purposes on project=dev and server=server "
                "(local docker-compose)"
            )
        from prefect.run_configs import LocalRun
        from prefect.storage.local import Local

        f.run_config = LocalRun(env={"ENV": env}, labels=[label])
        f.storage = Local(stored_as_script=True, path=flow_path)
        f.state_handlers = None
    else:
        from prefect.storage.s3 import S3

        f.storage = S3(
            bucket=s3_bucket,
            key=f"{env}/{name}",
            stored_as_script=True,
            local_script_path=flow_path,
        )
        if agent == "fargate":
            if server != "cloud" or project not in ["dev", "prod", "gatewayplatform-qa", "gatewayplatform-prod"]:
                raise ValueError(
                    "Registering flows with ECSRun config allowed only for dev and "
                    "testing purposes on project={dev, prod} and server=cloud"
                )
            region = os.getenv("AWS_REGION")
            account_id = os.getenv("AWS_ACCOUNT_ID")
            task_definition_arn = (
                f"arn:aws:ecs:{region}:{account_id}:task-definition/{ecs_task_name}"
            )
            from prefect.run_configs import ECSRun

            f.run_config = ECSRun(
                task_definition_arn=task_definition_arn,
                env={"ENV": env},
                labels=[label],
            )

    from prefect.client import Client

    prefect_client = Client(api_key=api_key)

    prefect_client.register(
        flow=f,
        project_name=project,
        build=True,  # will push py script to s3 bucket
        set_schedule_active=schedule,
        idempotency_key=f.serialized_hash(),
    )


@flow.command()
@click.option(
    "--env",
    required=False,
    type=click.Choice(["local", "dev", "qa", "prod"], case_sensitive=False),
    default="local",
    show_default=True,
    help=TARGET_ENV_ARG_HELP,
)
@click.option(
    "--server",
    required=False,
    type=click.Choice(["server", "cloud"], case_sensitive=False),
    default="server",
    show_default=True,
    help=SERVER_ARG_HELP,
)
@click.option(
    "--project",
    type=click.Choice(["dev", "prod", "gatewayplatform-qa", "gatewayplatform-prod"], case_sensitive=False),
    default="dev",
    show_default=True,
    help=PROJECT_ARG_HELP,
)
@click.option(
    "--agent",
    required=False,
    type=click.Choice(["local", "docker", "fargate"], case_sensitive=False),
    default="local",
    help=EXECUTION_ENV_ARG_HELP,
)
@click.option(
    "--label",
    required=False,
    type=str,
    default="local",
    help=LABEL_ARG_HELP
)
@click.option(
    "--s3-bucket",
    required=False,
    type=str,
    default="terraform-uk-prefect-flows-storage",
    help=S3_BUCKET_ARG_HELP,
)
@click.option(
    "--ecs-task-name",
    required=False,
    type=str,
    default="prefect-flows",
    help=ECS_TASK_NAME_ARG_HELP,
)
@click.option(
    "--schedule", required=False, is_flag=True, default=False, help=SCHEDULE_ARG_HELP
)
@click.pass_context
def register_all(ctx, env, server, project, agent, label, s3_bucket, ecs_task_name, schedule):
    click.echo(
        f"Retrieving all flows defined within flows_context under "
        f"project={project} with execution={env} and agent label={label}"
    )
    flows = create_flows_context()
    for f in flows.keys():
        ctx.invoke(
            register,
            name=f,
            env=env,
            project=project,
            server=server,
            agent=agent,
            label=label,
            s3_bucket=s3_bucket,
            ecs_task_name=ecs_task_name,
            schedule=schedule,
        )


@flow.command(help="Run flow locally with LocalRun")
@click.option("--name", required=True, type=str, help=NAME_ARG_HELP)
@click.option(
    "--env",
    required=False,
    type=click.Choice(["local", "dev", "qa", "prod"], case_sensitive=False),
    default="local",
    show_default=True,
    help=TARGET_ENV_ARG_HELP,
)
@click.option(
    "--log-level",
    type=click.Choice(["INFO", "WARNING", "ERROR"], case_sensitive=False),
    default="INFO",
    show_default=True,
)
@click.option(
    "--params", type=str, default="", callback=split_params, help=PARAMS_ARG_HELP
)
@click.option(
    "--schedule/--no-schedule", default=False, show_default=True, help=SCHEDULE_ARG_HELP
)
@click.pass_context
def local_run(ctx, name, env, log_level, params, schedule):
    env_vars_filter = [
        "PREFECT__FLOWS__CHECKPOINTING",
        "PREFECT__LOGGING__EXTRA_LOGGERS",
        "PREFECT__CLOUD__API_KEY",
        "FLOWS_CACHE_BUCKET",
        # "AWS_PROFILE",
        "AWS_REGION",
    ]
    env_vars = {k: os.getenv(k) for k in env_vars_filter}
    env_vars["ENV"] = env
    os.environ["ENV"] = env
    os.environ["PREFECT__LOGGING__LEVEL"] = log_level

    flows = create_flows_context()
    flow_dict: dict = flows.get(name)
    flow_path: str = flow_dict.get("path")
    f = flow_dict.get("flow")

    from prefect.executors.dask import LocalDaskExecutor
    from prefect.run_configs import LocalRun
    from prefect.storage.local import Local

    f.run_config = LocalRun(env=env_vars, labels=["local"])
    f.storage = Local(stored_as_script=True, path=flow_path)
    executor = LocalDaskExecutor(scheduler="processes", num_workers=12)
    f.executor = executor
    click.echo(
        f"Running flow:`{name}` locally with flow params={params}, "
        f"target={env}, storage={f.storage}",
        nl=False,
    )
    f.run(parameters=params, run_on_schedule=schedule)
    # executor._interrupt_pool()
    # executor._pool = None


@flow.command()
@click.option("--name", required=True, type=str, help=NAME_ARG_HELP)
@click.option(
    "--env",
    required=False,
    type=click.Choice(["local", "dev", "qa", "prod"], case_sensitive=False),
    default="local",
    show_default=True,
    help=TARGET_ENV_ARG_HELP,
)
@click.option("--date-param", required=True, type=str, help=DATE_PARAM_ARG_HELP)
@click.option(
    "--start-date",
    required=True,
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help=START_DATE_ARG_HELP,
)
@click.option(
    "--end-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    default=str((datetime.datetime.today() - datetime.timedelta(days=1)).date()),
    help=END_DATE_ARG_HELP,
)
@click.option(
    "--log-level",
    type=click.Choice(["INFO", "WARNING", "ERROR"], case_sensitive=False),
    default="INFO",
    show_default=True,
)
@click.option("--weekdays/--all-days", default=False, help=WEEKDAYS_ARG_HELP)
@click.option(
    "--params", type=str, default="", callback=split_params, help=PARAMS_ARG_HELP
)
@click.pass_context
def local_backfill(
    ctx, name, env, date_param, start_date, end_date, log_level, weekdays, params
):
    # generate target dates to run flow for
    target_dates = [
        (start_date + datetime.timedelta(days=x)).date()
        for x in range(0, (end_date - start_date).days + 1)
    ]
    if weekdays:
        target_dates = pd.date_range(start_date, end_date, freq="b")

    click.echo(
        f"Back-filling flow `{name}` targeting ENV=`{env}`"
        f"using `{date_param}` from "
        f"{min(target_dates).strftime('%Y-%m-%d')} "
        f"to {max(target_dates).strftime('%Y-%m-%d')} "
        f"with weekdays only={weekdays}"
    )

    for target_date in target_dates:
        params_ = {**params, date_param: target_date.strftime("%Y-%m-%d")}
        # ctx.invoke(local_run, name=name, env=env, log_level=log_level, params=params_)
        params_cmd = ",".join([f"{k}:{v}" for k, v in params_.items()])
        cmd = (
            f"prefield flow local-run --name={name} "
            f"--env={env} --log-level={log_level} --params={params_cmd}"
        )
        p = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        for line in p.stdout.readlines():
            click.echo(line)


@flow.command()
@click.option("--image-name", required=False, type=str, default="uk-prefect-flows")
@click.option(
    "--env",
    required=False,
    type=click.Choice(["dev", "qa", "prod"], case_sensitive=False),
    default="dev",
    show_default=True,
    help="Targeting dev/prod image to push to ECR",
)
@click.option("--image-tag", required=False, type=str, default="latest")
@click.option("--push/--no-push", default=False, help=PUSH_ARG_HELP)
def docker_build(image_name, env, image_tag, push):
    image_name = f"{image_name}-{env.lower()}"

    registry_url = None
    if push:
        # aws_credentials = aws_credentials_dict(env_vars.pop("AWS_PROFILE"))
        # docker_ecr_login(aws_credentials)
        # construct ECR repo url using account id and region
        aws_account_id = os.getenv("AWS_ACCOUNT_ID")
        aws_region = os.getenv("AWS_REGION")
        registry_url = f"{aws_account_id}.dkr.ecr.{aws_region}.amazonaws.com/"
        click.echo(f"push={push} -> will push image to {registry_url} after build")

    from prefect.storage.docker import Docker

    storage = Docker(
        registry_url=registry_url,
        image_name=image_name,
        image_tag=image_tag,
        dockerfile="Dockerfile",
    )
    click.echo(f"Building flows image {image_name}:{image_tag}")
    storage.build(push=push)
