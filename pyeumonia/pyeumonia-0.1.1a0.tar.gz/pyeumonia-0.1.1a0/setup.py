#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import platform


def rm_rf(file_name):
	if platform.system() == 'Windows':
		os.system(f'rd /s /q {file_name}')
	else:
		os.system(f'rm -rf {file_name}')


rm_rf('dist')
rm_rf('build')
rm_rf('pyeumonia.egg-info')


with open('README.md', 'r') as f:
	markdown = f.read()


setup(
	name="pyeumonia",
	version="0.1.1-alpha",
	description="Covid-19 api wrote by python, you can get the covid-19 data from China and the world",
	author="Senge-Studio",
	author_email="a1356872768@gmail.com",
	long_description=markdown,
	long_description_content_type='text/markdown',
	install_requires=['requests', 'beautifulsoup4'],
	python_requires=">=3.7.0",
	packages=find_packages(),
	include_package_data=True,
	license="GPL v3",
)
rm_rf('pyeumonia.egg-info')
rm_rf('build')
