from setuptools import setup, find_packages
import codecs
import os
from setuptools.command.install import install
from distutils.command.build_py import build_py as _build_py

VERSION = '0.0.6'
DESCRIPTION = 'SDK sanic application'

class CustomInstall(install):
    def run(self):
        install.run(self)
        print('overriden install command')

packages = ["keyo"]

# Setting up
setup(
    name="keyo_coral",
    version=VERSION,
    author="swalih",
    author_email="<swalihchungath@gmail.com>",
    cmdclass={'install': CustomInstall},
    description=DESCRIPTION,
    packages=packages,
    install_requires=['sanic'],
    keywords=['sanic','palm'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)