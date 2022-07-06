from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Khodnevis Normalizer'
LONG_DESCRIPTION = 'A Python library for Persian text preprocessing.'

# Setting up
setup(
    name="khodnevis",
    version=VERSION,
    author="khodnevisAI",
    author_email="<khodnevis.group@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['hazm', 'parsivar'],
    keywords=['python', 'persian', 'normalizer', 'text'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
