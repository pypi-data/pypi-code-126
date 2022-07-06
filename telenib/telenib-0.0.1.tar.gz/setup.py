import os
from setuptools import setup, find_packages
from telenib import __version__

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT_DIR, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="telenib",
    version=__version__,
    author="Xiao Gui",
    author_email="xgui3783@gmail.com",
    description="Fetch metadata from remote (https) nifti (gzipped or not).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(
        include=["telenib"]
    ),
    install_requires=[
        "requests>=2.26.0",
        'nibabel>=4.0.1',
    ],
    url="https://github.com/xgui3783/telenib",
)
