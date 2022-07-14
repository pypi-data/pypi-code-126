#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

with open('README.rst', 'r') as readme:
    long_description = readme.read()

setup(
    name='wagtail-rps-template',
    version='1.0.0',
    author='Manuel Schiegg',
    author_email='office@red-pepper.at',
    packages=find_packages(exclude=("tests")),
    url='https://github.com/red-pepper-services/wagtail-rps-template',
    license='MIT',
    description="Wagtail Admin customising for red pepper Customer",
    long_description=long_description,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Wagtail',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)