#!/usr/bin/env python
from os.path import dirname, realpath
from setuptools import setup, find_packages, Distribution
import pypcreate

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name="pypcreate",
    version=pypcreate.__version__,
    packages=find_packages(),
    package_data={"":["*.yaml"]},
    author="Zhaoliang Zheng",
    author_email="zhz03@g.ucla.edu",
    description="Python Package creation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GENERAL PUBLIC LICENSE V3",
    url="https://github.com/zhz03/PyPCreate",
    install_requires=[
        "argparse",
        "pyyaml",
        "requests"
        ],
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["pypcreate=pypcreate.create:main"]},
)
