import os
import tempfile
import shutil

import requests
from typing import Any, Dict
import typer
from rich import print as rprint
from rich.layout import Layout

import faas.util as util


cli = typer.Typer()
server_url = "http://192.168.1.167"
server_port = 8000


@cli.command()
def invoke(func: str):
    """
    Invoke a function
    """
    typer.echo(f"Invoking function {func}")


@cli.command()
def deploy(func_dir: str):
    """
    func_dir: path to the directory containing the function code.
    func_dir/
        config.yaml
        script.py
    """
    global server_url
    global server_port
    deploy_url = f"{server_url}:{server_port}/deploy"
    full_func_dir = os.path.join(os.getcwd(), func_dir)

    # read the config file
    config_path = os.path.join(full_func_dir, "config.yaml")
    config = util.load_yaml(config_path)
    func_name = config["name"]

    # zip the function directory
    typer.echo(f"Packing function: {func_name}")
    tmp_dir = tempfile.mkdtemp()
    zip_dir = os.path.join(tmp_dir, f"{func_name}")
    func_zip_file_path = shutil.make_archive(zip_dir, 'zip', full_func_dir)

    # upload the zip file
    typer.echo(f"Uploading to the remote server at {server_url}:{server_port}")
    files = [
        ("func_zip", (f"{func_name}.zip", open(func_zip_file_path, "rb"), "application/zip"))
    ]
    response = requests.request("POST", deploy_url, files=files)
    deployment_id = response.json().get("deploymentId", "")
    func_port = response.json().get("port", 0)
    typer.echo(f"Upload success with deployment id {deployment_id}")
    typer.echo(f"Deployment progress: {server_url}:{server_port}/deployment/{deployment_id}")
    typer.echo(f"API url: {server_url}:{func_port}")


@cli.command()
def login(url: str):
    """
    Login to a server
    """
    typer.echo(f"Logging to the server: {url}")


@cli.command()
def server(config: str):
    """
    Initiate a server
    """
    typer.echo(f"Starting server with config: {config}")


@cli.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Default behavior
    """
    # only run without a command specified
    if ctx.invoked_subcommand is not None:
        return

    layout = Layout()
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    layout["lower"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )
    rprint(layout)
