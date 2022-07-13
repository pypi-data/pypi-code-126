#!/bin/env python
# -*- coding: utf-8 -*-
"""
File Information:
-----------------
setuptools script for aestimo project
"""
from setuptools import setup
import os, sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(  name='aestimo',
        version='3.0.0',
        description='1D Semiconductor QW bandstructure simulator',
        long_description_content_type='text/markdown',
        long_description= """# Aestimo 1D Self-consistent Schrödinger-Poisson Solver\n\n Aestimo is a simple 1-dimensional (1-D) simulator for educational and research. Please do not hesitate to contact us in case of any bugs found.""",
        classifiers=[
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Programming Language :: Python :: 3",
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Science/Research",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Topic :: Scientific/Engineering :: Physics",
          "Topic :: Scientific/Engineering"
           ],
        author='sblisesivdin',
        author_email='sblisesivdin@gmail.com',
        url='http://www.aestimosolver.org',
        license='GPLv3',
        keywords='quantum well semiconductor nanostructure optical transitions',
        package_dir = {'aestimo': ''},
        packages=['aestimo'],
        package_data={'aestimo':['CODE_OF_CONDUCT.md','README.md','COPYING.md',
                                 'aeslibs/*.py',
                                 'tutorials/*','examples/*.py']},
        install_requires=['numpy>1.7.0','matplotlib','scipy'],
        zip_safe=False, #we want users to be able to easily see and edit the scripts
        #setup_requires=['numpy'], #causes problems with pip?
        )
