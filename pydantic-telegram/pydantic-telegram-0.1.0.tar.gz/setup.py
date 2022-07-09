"""Defines the setup fro creating pip package."""

import io
import os

from setuptools import setup, find_packages

__version__ = "0.1.0"
NAME = "pydantic-telegram"
AUTHOR = "Daniel Miller"
AUTHOR_EMAIL = "danielmiller20@gmail.com"
DESCRIPTION = "Pydantic classes creating telegram bots."
LICENSE = "MIT"

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf8") as f:
        LONG_DESCRIPTION = "\n" + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name=NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    packages=find_packages(exclude=["test", "docs", "contrib"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "pydantic>=1.8.2",
    ],

)
