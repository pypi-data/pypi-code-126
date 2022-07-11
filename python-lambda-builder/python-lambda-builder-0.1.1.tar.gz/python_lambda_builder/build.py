import os
import shutil
from pathlib import Path

import typer

from python_lambda_builder.enums import PackageManager
from python_lambda_builder.pip_build import pip_build
from python_lambda_builder.poetry_build import poetry_build
from python_lambda_builder.utils import relative_to_absolute

app = typer.Typer()


@app.command()
def build(
    func_src: str = typer.Option(
        ..., help="Relative or absolute directory of the lambda function source code."
    ),
    build_dest: str = typer.Option(
        "./dist", help="Relative or absolute directory of the build destination."
    ),
    manager: PackageManager = typer.Option(
        PackageManager.POETRY, help="poetry OR pip"
    ),
    pyproject_path: str = typer.Option(
        "./pyproject.toml",
        help="Relative or absolute path to the poetry pyproject.toml."),
    requirements_path: str = typer.Option(
        "./requirements.txt",
        help="Relative or absolute path to the pip requirements.txt file."
    ),
) -> None:
    """
    This builds the package and its python dependencies into a destination folder specified.
    """
    func_src = relative_to_absolute(func_src)
    build_dest = relative_to_absolute(build_dest)
    pyproject_path = relative_to_absolute(pyproject_path) if pyproject_path else pyproject_path
    requirements_path = (
        relative_to_absolute(requirements_path) if requirements_path else pyproject_path
    )

    if not os.path.exists(func_src):
        raise FileNotFoundError(f"{func_src} is not a valid code source directory.")

    if os.path.exists(build_dest):
        shutil.rmtree(build_dest, ignore_errors=True)

    typer.echo(f"Creating directory at {build_dest} for build")
    os.mkdir(build_dest)

    if manager == PackageManager.POETRY:
        poetry_build(build_dest, pyproject_path)
    elif manager == PackageManager.PIP:
        pip_build(build_dest, requirements_path)

    typer.echo("Copying function source...")
    func_src_folder_name = os.path.normpath(func_src).split(os.path.sep)[-1]
    shutil.copytree(func_src, Path(build_dest, func_src_folder_name), dirs_exist_ok=True)
    typer.secho(f"Done. Your project files can be found in"
                f" {Path(build_dest, func_src_folder_name)}.")


def run() -> None:
    app()
