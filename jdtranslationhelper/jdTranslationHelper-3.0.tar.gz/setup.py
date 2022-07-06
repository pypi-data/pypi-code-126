#!/usr/bin/env python3
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(name='jdTranslationHelper',
    version='3.0',
    description='A simple API for translating your programs',
    long_description=description,
    long_description_content_type='text/markdown',
    author='JakobDev',
    author_email='jakobdev@gmx.de',
    url='https://gitlab.com/JakobDev/jdTranslationHelper',
     python_requires='>=3.7',
    include_package_data=True,
    packages=['jdTranslationHelper'],
    license='BSD',
    keywords=['JakobDev', 'translation', 'localization'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Other Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
 )
