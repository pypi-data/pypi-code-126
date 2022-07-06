# pylint: disable=unused-argument


import typer
from typer import Typer

from ... import gql, ui
from ...config_utils import dagster_cloud_options

app = Typer(help="Manage branch deployments for your organization.")


@app.command(name="create-or-update")
@dagster_cloud_options(allow_empty=True, requires_url=True)
def create_or_update(
    organization: str,
    url: str,
    api_token: str,
    repo_name: str = typer.Option(
        ..., "--git-repo-name", "--repo-name", help="The name of the git repository."
    ),
    branch_name: str = typer.Option(
        ..., "--branch-name", help="The name of the version control branch."
    ),
    commit_hash: str = typer.Option(..., help="The latest commit hash."),
    timestamp: float = typer.Option(..., help="The latest commit timestamp."),
    branch_url: str = typer.Option(None, help="The URL of the version control branch."),
    pull_request_url: str = typer.Option(
        None,
        "--code-review-url",
        "--pull-request-url",
        help="The URL to review this code, e.g. a Pull Request or Merge Request.",
    ),
    pull_request_status: str = typer.Option(None, help="The status of the pull request"),
    pull_request_number: str = typer.Option(
        None,
        "--code-review-id",
        "--pull-request-id",
        help="An identifier for the code review for this branch, e.g. a Pull Request number.",
    ),
    commit_message: str = typer.Option(None, help="The commit message for the latest commit."),
    author_name: str = typer.Option(None, help="The author name for the latest commit."),
    author_email: str = typer.Option(None, help="The author email for the latest commit."),
    author_avatar_url: str = typer.Option(
        None, help="The URL for the avatar of the author for the latest commit, if any."
    ),
) -> None:
    """
    Sets up or updates the branch deployment for the given git branch.
    """
    if not url and not organization:
        raise ui.error("Must provide either organization name or URL.")
    if not url:
        url = gql.url_from_config(organization=organization)

    with gql.graphql_client_from_url(url, api_token) as client:
        ui.print(
            gql.create_or_update_branch_deployment(
                client,
                repo_name=repo_name,
                branch_name=branch_name,
                commit_hash=commit_hash,
                timestamp=timestamp,
                branch_url=branch_url,
                pull_request_url=pull_request_url,
                pull_request_status=pull_request_status,
                pull_request_number=pull_request_number,
                commit_message=commit_message,
                author_name=author_name,
                author_email=author_email,
                author_avatar_url=author_avatar_url,
            )
        )
