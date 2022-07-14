# The MIT License.
# Copyright (C) 2022 evildevill , Waseem Akram.
#
# @filename    : setup.py
# @description : The traditional setup.py script for
#                Installation from pip or easy_install

from codecs import open
from os.path import abspath, dirname, join , expanduser

from setuptools import Command, find_packages, setup

from InstahackWasii import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'instahack',
    version = __version__,
    description = 'Slick Instagram brute force command line tool writen in python.',
    long_description = long_description,
    url = 'https://github.com/evildevill/instahack',
    download_url = 'https://github.com/evildevill/instahack/archive/v'+str(__version__)+'.tar.gz',
    author = 'Waseem Akram',
    author_email = 'hackerwasi1@gmail.com',
    license = 'MIT',
    classifiers = [
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6'
    ],
    keywords = ['cli' , 'hack' , 'instagram' , 'with' , 'out' , 'password' , 'limit' , 'brute' ,
                'force' , 'attack' , 'instagram' , 'instahack' , 'evildevill' , 'hackerwasii'],
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['requests' , 'requests[socks]' , 'stem'],
    entry_points = {
        'console_scripts': [
            'instahack=InstahackWasii:ExecuteInstahackWasii',
        ],
    },

)
