import os
from pathlib import Path
from typing import Union

import typer


def pip_build(build_dest: Union[Path, str], requirements_path: Union[Path, str]) -> None:
    typer.echo("Installing packages to build directory", color=True)
    os.system(f"pip install -r {requirements_path} -t {build_dest}")
