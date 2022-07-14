#!/usr/bin/env python3

# This is a simple command-line client for the OctoML Platform.

import json
from collections.abc import Iterator

import click
import google.protobuf.json_format
import requests

import octomizer.client as client

print_as_json = False


def print_cli_result(result):
    """Prints an OctoML object or a collection of OctoML objects, optionally
    using the JSON representation of the backing protobuf message."""
    if print_as_json:
        # Convert the result to a JSON-serializable value.
        def convert(result):
            if isinstance(result, Iterator):
                # Recursively convert the contents.
                return list(map(convert, result))
            elif hasattr(result, "proto"):
                # Treat it as an object that has an associated protobuf message.
                return google.protobuf.json_format.MessageToDict(result.proto)
            else:
                # Assume it's already a protobuf message.
                return google.protobuf.json_format.MessageToDict(result)

        click.echo(json.dumps(convert(result)))
    else:
        if isinstance(result, Iterator):
            for x in result:
                click.echo(x)
        else:
            click.echo(result)


# Top-level options.
@click.group()
@click.option(
    "--server_host",
    envvar="OCTOMIZER_API_HOST",
    default="api.octoml.ai",
    help="OctoML API server hostname.",
)
@click.option(
    "--server_port",
    envvar="OCTOMIZER_API_PORT",
    type=int,
    default=443,
    help="OctoML API server port.",
)
@click.option(
    "--insecure",
    default=False,
    is_flag=True,
    help="Use an insecure connection to the API server.",
)
@click.option(
    "--access_token",
    envvar="OCTOMIZER_API_TOKEN",
    help="OctoML API access token.",
)
@click.option("--json", default=False, is_flag=True, help="Print the results as JSON.")
@click.pass_context
def cli(ctx, server_host, server_port, insecure, access_token, json):
    global print_as_json
    print_as_json = json
    ctx.obj = client.OctomizerClient(server_host, server_port, insecure, access_token)


# Model-related commands.
@cli.command(help="Get the model with the specified UUID")
@click.argument(
    "model_uuid",
)
@click.pass_context
def get_model(ctx, model_uuid):
    model = ctx.obj.get_model(model_uuid)
    print_cli_result(model)


@cli.command(help="Delete the model with the specified UUID")
@click.argument(
    "model_uuid",
)
@click.option(
    "--yes", default=False, is_flag=True, help="Confirm action without prompting."
)
@click.pass_obj
def delete_model(client, model_uuid, yes):
    model = client.get_model(model_uuid)
    model_variants = len(list(model.list_model_variants()))
    workflows = len(list(model.list_workflows()))
    if not yes:
        click.confirm(
            f"Delete model {model_uuid}: This will delete {model_variants} model variants\n"
            f"and {workflows} workflows. This cannot be undone. Are you sure?",
            abort=True,
        )
    client.delete_model(model_uuid)
    click.echo("Done.")


@cli.command(help="List models")
@click.pass_obj
def list_models(client):
    print_cli_result(client.list_models())


# ModelVariant-related commands.
@cli.command(help="Get the model variant with the specified UUID")
@click.argument(
    "model_variant_uuid",
)
@click.pass_obj
def get_model_variant(client, model_variant_uuid):
    model_variant = client.get_model_variant(model_variant_uuid)
    print_cli_result(model_variant)


@cli.command(help="List model variants for a given model UUID")
@click.argument(
    "model_uuid",
)
@click.pass_obj
def list_model_variants(client, model_uuid):
    model = client.get_model(model_uuid)
    print_cli_result(model.list_model_variants())


# Workflow-related commands.
@cli.command(help="List workflows for a given model UUID")
@click.argument(
    "model_uuid",
)
@click.pass_obj
def list_workflows(client, model_uuid):
    model = client.get_model(model_uuid)
    print_cli_result(model.list_workflows())


@cli.command(help="Get the workflow with the specified UUID")
@click.argument(
    "workflow_uuid",
)
@click.option(
    "--poll_interval",
    type=int,
    help="If set, poll the Workflow status every --poll_interval seconds.",
)
@click.option(
    "--timeout",
    type=int,
    help="If set, poll until the Workflow completes or this many seconds have elapsed.",
)
@click.pass_obj
def get_workflow(client, workflow_uuid, poll_interval, timeout):
    workflow = client.get_workflow(workflow_uuid)
    if poll_interval is not None:
        workflow.wait(timeout, poll_interval, lambda wf: print_cli_result(wf))
    else:
        workflow = client.get_workflow(workflow_uuid)
        print_cli_result(workflow)


@cli.command(help="Cancel the workflow with the specified UUID")
@click.argument(
    "workflow_uuid",
)
@click.pass_obj
def cancel_workflow(client, workflow_uuid):
    workflow = client.cancel_workflow(workflow_uuid)
    print_cli_result(workflow)


# User- and Account-related commands.
@cli.command(help="Get the currently-authenticated user")
@click.pass_obj
def current_user(client):
    user = client.get_current_user()
    print_cli_result(user)


@cli.command(help="Get the user with the specified UUID")
@click.argument(
    "user_uuid",
)
@click.pass_obj
def get_user(client, user_uuid):
    user = client.get_user(user_uuid)
    print_cli_result(user)


@cli.command(help="Get the account with the specified UUID")
@click.argument(
    "account_uuid",
)
@click.pass_obj
def get_account(client, account_uuid):
    account = client.get_account(account_uuid)
    print_cli_result(account)


@cli.command(help="Get the users of the account with the specified account UUID")
@click.argument(
    "account_uuid",
)
@click.pass_obj
def get_account_users(client, account_uuid):
    members = client.get_account_users(account_uuid)
    print_cli_result(members)


@cli.command(help="Download the dataref with the specified UUID")
@click.argument("dataref_uuid")
@click.option(
    "--output_file",
    default="contents.onnx",
    help="File where the downloaded contents should be stored. Defaults to contents.onnx",
)
@click.pass_obj
def download_dataref(client, dataref_uuid, output_file):
    dataref = client.get_dataref(dataref_uuid)
    print(f"Downloading {dataref.size} bytes from url {dataref.url}")

    with requests.get(dataref.url) as response:
        with open(output_file, "wb") as of:
            of.write(response.content)

    print(f"Downloaded dataref contents to {output_file}")


if __name__ == "__main__":
    cli()
