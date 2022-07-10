#!/usr/bin/env python
from os.path import dirname, realpath
from setuptools import setup, find_packages, Distribution
import package_name

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name="package_name",
    version=package_name.__version__,
    packages=find_packages(),
    package_data={"":["*.yaml"]},
    author="Zhaoliang Zheng",
    author_email="zhz03@g.ucla.edu",
    description="Description of an example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GENERAL PUBLIC LICENSE V3",
    url="https://github.com/xxxxx",
    install_requires=[
        "xxx",
        "xxx"
        ],
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["cmd=package_name.py_name:function_name"]},
)
