from setuptools import setup, find_packages
from pathlib import Path


# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="py_wrike_v4",
    version="0.14",
    license="MIT",
    author="Govinda Hosein",
    author_email="raziel619dev@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/Raziel619/py_wrike_v4",
    keywords="wrike",
    install_requires=[
        "certifi==2022.6.15",
        "charset-normalizer==2.0.12",
        "idna==3.3",
        "requests==2.28.0",
        "urllib3==1.26.9",
    ],
)
