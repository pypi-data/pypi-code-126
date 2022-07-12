from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

# Read requirements.txt file into array for 'install_requires'
with open(this_directory / "requirements.txt") as f:
    required = f.read().splitlines()

# read the contents of README file

long_description = (this_directory / "README.md").read_text()

setup(
    name="py_wrike_v4",
    version="0.12",
    license="MIT",
    author="Govinda Hosein",
    author_email="raziel619dev@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/Raziel619/py_wrike_v4",
    keywords="wrike",
    install_requires=required,
)
