from setuptools import setup, find_packages
#import codecs
#import os

VERSION = '0.0.1'
DESCRIPTION = 'plz work'


setup(
    name="resnetcarvana",
    version=VERSION,
    author="Sha",
    author_email="sliu23009@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['opencv-python'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)