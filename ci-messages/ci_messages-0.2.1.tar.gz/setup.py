# Copyright Red Hat
#
# This file is part of python-ci_messages.
#
# python-ci_messages is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Adam Williamson <awilliam@redhat.com>

"""Setuptools configuration."""

from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
try:
    with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
        LONGDESC = f.read()
except TypeError:
    with open(path.join(HERE, "README.md")) as f:
        LONGDESC = f.read()

setup(
    name="ci_messages",
    version="0.2.1",
    description="Python wrapper for CI Messages schemas",
    license="GPLv3+",
    author="Adam Williamson",
    author_email="awilliam@redhat.com",
    url="https://pagure.io/fedora-ci/python-ci_messages",
    # Possible options are at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=open("install.requires").read().splitlines(),
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4",
    long_description=LONGDESC,
    long_description_content_type="text/markdown",
    packages=["ci_messages"],
    package_dir={"": "src"},
    entry_points={
        "fedora.messages": [
            "ci_messages.CIMessageV1=ci_messages.schema:CIMessageV1",
        ],
    },
)


# vim: set textwidth=120 ts=8 et sw=4:
