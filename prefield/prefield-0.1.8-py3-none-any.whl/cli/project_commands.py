import os

import click


@click.group(help="Util for creating local/Prefect cloud projects")
def project():
    pass


@project.command()
@click.option(
    "--name", required=False, default="dev", type=str, help="Prefect Project Name"
)
@click.option(
    "--description",
    required=False,
    type=str,
    help="Prefect Project Description visible in the UI",
)
def create_local(name: str, description: str):
    from prefect.client import Client

    prefect_client = Client()
    prefect_client.create_project(project_name=name, project_description=description)


@project.command()
@click.option(
    "--name", required=False, default="dev", type=str, help="Prefect Project Name"
)
@click.option(
    "--description",
    required=False,
    type=str,
    help="Prefect Project Description visible in the UI",
)
def create_cloud(name: str, description: str):
    API_KEY = os.getenv("PREFECT_CLOUD_API_KEY")
    os.environ["PREFECT__BACKEND"] = "cloud"
    from prefect.client import Client

    prefect_client = Client(api_key=API_KEY)
    prefect_client.create_project(project_name=name, project_description=description)
