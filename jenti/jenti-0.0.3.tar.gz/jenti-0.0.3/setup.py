import os
import sys
from setuptools import find_packages, setup
from pathlib import Path

# Reference: https://github.com/pypa/pip/blob/c0fb4bf1ad21d6f764085de132d25f834db1da90/setup.py#L15

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="jenti",
    version=get_version("F:\Python_package_generation\PATCH_AND_MERGE\jenti\__init__.py"),
    description="To create/merge 2D or 3D patches.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/mrinal054/patch_and_merge",

    author="Mrinal Kanti Dhar",
    author_email="mrinal054@gmail.com",
    package_dir={"": "jenti"},
    packages= find_packages(
        where="jenti",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),

    python_requires=">=3.7",
    include_package_data = True,
)