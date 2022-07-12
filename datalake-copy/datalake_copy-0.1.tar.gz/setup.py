import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="datalake_copy",
    version="0.01",
    description="A library for datalake copying to databricks",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Eric Schles",
    packages=["datalake_copy"],
    include_package_data=True,
    install_requires=["requests"],
)
