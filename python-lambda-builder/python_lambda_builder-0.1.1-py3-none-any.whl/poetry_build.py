import os
import shutil
import tempfile
import uuid
from pathlib import Path
from typing import Union

import toml
import typer

from python_lambda_builder.utils import get_command_output


def poetry_build(build_dest: Union[Path, str], pyproject_path: Union[Path, str]) -> None:
    tmp_dir = tempfile.gettempdir()
    run_key = str(uuid.uuid4())

    pyproject = toml.load(pyproject_path)
    # Modify the project name so that it does not override environment for the actual project

    project_name = pyproject["tool"]["poetry"]["name"]
    alt_project_name = f"{pyproject['tool']['poetry']['name']}-{run_key}"
    pyproject["tool"]["poetry"]["name"] = alt_project_name

    op_dir = Path(tmp_dir, project_name)
    shutil.rmtree(op_dir, ignore_errors=True)
    os.makedirs(op_dir)
    toml.dump(pyproject, open(os.path.join(op_dir, "pyproject.toml"), "w+"))
    os.chdir(op_dir)

    typer.echo("Installing pyproject requirements...")
    os.system("poetry install --no-dev")
    packages_dir = get_command_output("poetry env info -p")
    python_minor_version = packages_dir.split("-")[-1].lstrip("py")
    packages_folder = Path(packages_dir, "lib", f"python{python_minor_version}", "site-packages")
    # Remove the destination if it already exists
    # Copy the packages and actual source code to folder
    typer.echo("Copying installed packages...")
    shutil.copytree(packages_folder, build_dest, dirs_exist_ok=True)
    typer.echo("Removing temporary poetry init directory..")
    shutil.rmtree(packages_dir, ignore_errors=True)
