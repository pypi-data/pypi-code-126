#!/usr/bin/env python3
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'pyil-bin',
    version = '0.1',
    description = 'Embed python expressions in bash',
    long_description = readme,
    long_description_content_type='text/markdown',
    author = "Lumi Akimova",
    author_email = 'q@wolph.in',
    url = 'https://gitlab.com/qwolphin/pyil',
    py_modules = ['pyil_bin'],
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'pyil = pyil_bin:main',
        ]
    },
)
