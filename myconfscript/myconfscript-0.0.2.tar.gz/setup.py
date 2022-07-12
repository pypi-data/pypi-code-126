import subprocess, os
from setuptools import setup

setup(
    name='myconfscript',
    version='0.0.2',
    author='Nikolai Krivoshchapov',
    packages=['myconfscript'],
    package_data={'myconfscript': ['__init__.py', 'confpool.cpython-38-x86_64-linux-gnu.so', 'libgslcblas.so.0']}
)
