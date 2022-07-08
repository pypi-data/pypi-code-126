from gettext import install
from setuptools import setup, find_packages

from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='datapro-learning',
    version="1.0",
    description="learning common data structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["datapro"],
    include_package_data=True,
    install_requires=['pandas','numpy','pythainlp','scipy','openpyxl'],
)