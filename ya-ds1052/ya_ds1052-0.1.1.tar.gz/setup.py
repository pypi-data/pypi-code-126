#!/usr/bin/env python

from pathlib import Path
from setuptools import find_packages, setup

here = Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ya_ds1052',
    description='Remote control of Rigol DS1000E/D oscilloscopes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.1.1',
    url='https://gitlab.com/adeuring/ya_ds1052',
    author='Abel Deuring',
    author_email='adeuring@gmx.net',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later '
            '(GPLv3+)',
        'Topic :: System :: Hardware :: Hardware Drivers',
        ],
    packages = find_packages(),
    test_suite='ds1052.tests',
    install_requires=[
        'aenum',
        'numpy',
    ],
    license_files=['LICENSE.txt'],
    )
