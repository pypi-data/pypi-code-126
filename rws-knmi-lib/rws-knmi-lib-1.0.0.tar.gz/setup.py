#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number,
# edit rws_knmi_lib/__init__.py


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="rws-knmi-lib",
    extras_require={
        "dev": [
            "bandit",
            "black",
            "flake8",
            "flake8-bugbear",
            "flake8-comprehensions",
            "flake8-docstrings",
            "flake8-polyfill",
            "isort",
            "mypy",
            "pre-commit",
            "pylint",
            "pylint[prospector]",
            "radon",
            "safety",
        ],
    },
    tests_require=["pytest", "pytest-cov"],
    test_suite="tests",
    version=find_version("rws_knmi_lib", "__init__.py"),
    license="Apache Software License 2.0",
    description="Library voor communicatie met KNMI weer data.",
    long_description=readme + "\n\n",
    author="Rijkswaterstaat Datalab",
    author_email="datalab.codebase@rws.nl",
    url="https://gitlab.com/rwsdatalab/public/codebase/tools/rws-knmi-lib",
    packages=["rws_knmi_lib"],
    include_package_data=True,
    package_data={"rws_knmi_lib": ["py.typed"]},
    zip_safe=False,
    keywords="rws-knmi-lib",
    license_files=["LICENSE"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "mpu",
        "pandas",
        "requests",
        "types-requests",
    ],
    setup_requires=[
        # dependency for `python setup.py test`
        "pytest-runner",
        "mpu",
        "pandas",
        # dependencies for `python setup.py build_sphinx`
        "sphinx",
        "sphinxcontrib-pdfembed @ https://github.com/SuperKogito/sphinxcontrib-pdfembed",
        "pydata-sphinx-theme",
    ],
)
