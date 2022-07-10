from pprint import pformat
from typing import List, Optional, Union

import click
import sqlalchemy as sa
from click.core import Group
from dotenv import dotenv_values
from sqlalchemy.dialects import postgresql
from tqdm import tqdm

from . import tables
from .containers import create_container_from_db, remove_docker_container
from .systemd import create_scheduled_service_from_db, remove_service
from .tables import SCHEMA_NAME, container_config_table, container_env_table
from .utils import (
    get_engine,
    get_existing_task_names,
    get_file_task_name,
    get_scheduled_names,
    get_tasks_systemd_files,
)

cli = Group("task-flows", chain=True)


@cli.command()
def init_db():
    """Create any tables that do not currently exist in the database."""
    with get_engine().begin() as conn:
        if not conn.dialect.has_schema(conn, schema=SCHEMA_NAME):
            click.echo(click.style(f"Creating schema '{SCHEMA_NAME}'", fg="cyan"))
            conn.execute(sa.schema.CreateSchema(SCHEMA_NAME))
        for table in (
            tables.timer_options_table,
            tables.container_config_table,
            tables.container_env_table,
            tables.container_volumes_table,
            tables.container_ulimits_table,
            tables.task_runs_table,
            tables.task_errors_table,
        ):
            click.echo(click.style(f"Checking table: {table.name}", fg="cyan"))
            table.create(conn, checkfirst=True)
    click.echo(click.style("Done!✅", fg="green"))


@cli.command()
@click.argument("file")
@click.argument("task_names", nargs=-1, required=False)
@click.option("--remove_existing", "-r", is_flag=True)
def load_env_file(
    file: str,
    task_names: Optional[Union[str, List[str]]] = None,
    remove_existing: bool = False,
):
    """Load an environmental variable file to the database.

    Args:
        file (str): The path to the file.
        task_names (Optional[Union[str, List[str]]], optional): Names of tasks the env vars should be used for. Defaults to all tasks.
        remove_existing (bool, optional): Remove all existing env vars for task(s) before loading the file. Defaults to False.
    """
    if not task_names:
        with get_engine().begin() as conn:
            task_names = list(
                conn.execute(
                    sa.select(container_config_table.c.task_name.distinct())
                ).scalars()
            )
    elif isinstance(task_names, str):
        task_names = [task_names]

    if remove_existing:
        with get_engine().begin() as conn:
            conn.execute(
                sa.delete(container_env_table).where(
                    container_env_table.c.task_name.in_(task_names)
                )
            )
    env = dotenv_values(file)
    click.echo(
        click.style(
            f"Loading env for {len(task_names)} tasks:\n{pformat(task_names)}:\n{pformat(env)}",
            fg="cyan",
        )
    )
    values = [
        {"task_name": n, "variable": k, "value": v}
        for n in task_names
        for k, v in env.items()
    ]
    statement = postgresql.insert(container_env_table).values(values)
    statement = statement.on_conflict_do_update(
        index_elements=["task_name", "variable"],
        set_={"value": statement.excluded["value"]},
    )
    with get_engine().begin() as conn:
        conn.execute(statement)
    click.echo(click.style("Done!✅", fg="green"))


@cli.command()
@click.option("-t", "--task", "tasks", multiple=True)
@click.option("--recreate", "-r", is_flag=True)
def create(tasks: Optional[List[str]] = None, recreate: bool = False):
    """Create scheduled tasks for task configurations in the database.

    Args:
        recreate (bool, optional): Recreate already existing tasks. Defaults to False.
    """
    names_to_create = tasks or get_scheduled_names()
    if not recreate and (existing_task_names := get_existing_task_names()):
        click.echo(
            click.style(
                f"Ignoring {len(existing_task_names)} existing tasks (not recreating).",
                fg="cyan",
            )
        )
        names_to_create.difference_update(existing_task_names)
    click.echo(
        click.style(f"Creating {len(names_to_create)} scheduled task(s).", fg="cyan")
    )
    for task_name in tqdm(names_to_create):
        create_container_from_db(task_name)
        create_scheduled_service_from_db(task_name)
    click.echo(click.style("Done!✅", fg="green"))


@cli.command()
def clean():
    """Remove files from tasks that have been deleted from the database."""
    scheduled_names = get_scheduled_names()
    to_remove = [
        ((task_name := get_file_task_name(file)), file)
        for file in get_tasks_systemd_files()
        if task_name not in scheduled_names
    ]
    if to_remove:
        for task_name, file in to_remove:
            click.echo(
                click.style(f"Removing files from deleted task: {task_name}", fg="cyan")
            )
            remove_service(file)
            remove_docker_container(task_name)
        click.echo(click.style("Done!✅", fg="green"))
    else:
        click.echo(click.style(f"No task files to remove.", fg="yellow"))
