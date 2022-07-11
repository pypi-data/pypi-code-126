#!/usr/bin/env python

from setuptools import setup

setup(name='hfradarcsv',
      version='0.1',
      description='Convert Diagnostic (only .rdt files) and .tuv totals file to csv files',
      author='VishalJain_NIOT',
      author_email='vishaljain9516@gmail.com',
      packages=['hfradarcsv'],
      install_requires=['pandas'])

