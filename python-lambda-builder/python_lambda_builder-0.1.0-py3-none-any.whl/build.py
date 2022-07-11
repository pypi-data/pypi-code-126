import os
import shutil

import typer

from python_lambda_builder.enums import PackageManager
from python_lambda_builder.pip_build import pip_build
from python_lambda_builder.poetry_build import poetry_build
from python_lambda_builder.utils import relative_to_absolute


def main(
    func_src: str,
    build_dest: str = "./dest",
    manager: PackageManager = PackageManager.POETRY,
    pyproject_path: str = "./pyproject.toml",
    requirements_path: str = "./requirements.txt",
) -> None:
    """
    :param func_src: Relative or absolute directory of the lambda function source code
    :param build_dest: Relative or absolute directory of the build destination, default is "dest"
    in the current work directory
    :param manager: poetry OR pip
    :param pyproject_path: Relative or absolute path to the poetry pyproject.toml, defaults to
    "pyproject.toml" in current work directory.
    :param requirements_path: Relative or absolute path to the pip requirements.txt file,
    default to "requirements.txt" in current work directory.
    :return:
    """
    func_src = relative_to_absolute(func_src)
    build_dest = relative_to_absolute(build_dest)
    pyproject_path = relative_to_absolute(pyproject_path) if pyproject_path else pyproject_path
    requirements_path = (
        relative_to_absolute(requirements_path) if requirements_path else pyproject_path
    )

    if os.path.exists(build_dest):
        shutil.rmtree(build_dest, ignore_errors=True)

    typer.echo(f"Creating directory at {build_dest} for build")
    os.mkdir(build_dest)

    if manager == PackageManager.POETRY:
        poetry_build(build_dest, pyproject_path)
    elif manager == PackageManager.PIP:
        pip_build(build_dest, requirements_path)

    typer.echo("Copying function source...")
    shutil.copytree(func_src, build_dest, dirs_exist_ok=True)


if __name__ == "__main__":
    typer.run(main)
