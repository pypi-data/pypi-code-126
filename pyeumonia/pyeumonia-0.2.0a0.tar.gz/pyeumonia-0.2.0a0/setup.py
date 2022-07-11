#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import platform
import getpass


def rm_rf(file_name):
	if platform.system() == 'Windows':
		os.system(f'rd /s /q {file_name}')
	else:
		os.system(f'rm -rf {file_name}')


rm_rf('dist')
rm_rf('build')
rm_rf('pyeumonia.egg-info')


with open('README.md', 'r', encoding='utf-8') as f:
	markdown = f.read()


setup(
	name="pyeumonia",
	version="0.2.0-alpha",
	description="Covid-19 api wrote by python, you can get the covid-19 data from China and the world",
	author="Senge-Studio",
	author_email="a1356872768@gmail.com",
	long_description=markdown,
	long_description_content_type='text/markdown',
	install_requires=['requests', 'beautifulsoup4', 'pypinyin', 'iso3166'],
	python_requires=">=3.7.0",
	packages=find_packages(),
	include_package_data=True,
	license="GPL v3",
)
rm_rf('pyeumonia.egg-info')
rm_rf('build')


if input('Do you want to publish this package?(y/n)').lower() == 'y':
    username = input('Please input your github username: ')
    passphrase = getpass.getpass('Please input your pypi password: ')
    os.system('twine upload dist/* -u {} -p {}'.format(username, passphrase))
