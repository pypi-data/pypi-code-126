#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name="pytest-sharkreport",
    version="1.0.1",
    author="qiuxiaohui",
    author_email="15007968334@163.com",
    description="this is pytest report plugin. ",
    long_description=open("README.rst").read(),
    license="MIT",
    keywords="py.test pytest report",
    python_requires=">=3.6",
    url="https://pypi.org/project/pytest-sharkreport/",
    packages=['SharkReportPlugin'],
    install_requires=["pytest>=3.5"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
    package_data={"SharkReportPlugin": ["reports/*"]},
    # the following makes a plugin available to pytest
    py_modules=['SharkReportPlugin.sharkReport'],
    entry_points={
        "pytest11": ["sharkreport = SharkReportPlugin.sharkReport"]
    },
)
