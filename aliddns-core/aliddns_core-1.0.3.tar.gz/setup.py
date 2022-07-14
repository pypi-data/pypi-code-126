# -*- coding: utf-8 -*-
import re

from setuptools import setup

from aliddns_core.version import __version__

setup(
    name='aliddns_core',
    version=__version__,
    description='Python library for aliyun ddns core',
    long_description=
    'Python library for aliyun ddns core',
    url='https://github.com/heculess/aliddns_core',
    author='heculess lau',
    author_email='heculess@hotmail.com',
    license='Apache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='aliyun ddns',
    packages=["aliddns_core"],
    python_requires='>=3.5',
    install_requires=[
        'attrs',
    ])
