from setuptools import setup, find_packages
import codecs
import os
from setuptools.command.install import install
from distutils.command.build_py import build_py as _build_py
from setuptools.command.develop import develop
from subprocess import check_call

VERSION = '0.2.1'
DESCRIPTION = 'SDK sanic application'

class CustomInstall(install):
    def run(self):
        print('overriden install command')
        install.run(self)

class PostDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        check_call("apt-get install this-package".split())
        develop.run(self)

packages = ["keyo"]

# Setting up
setup(
    name="keyo_coral",
    version=VERSION,
    author="swalih",
    author_email="<swalihchungath@gmail.com>",
    cmdclass={'install': CustomInstall, 'develop': PostDevelopCommand,},
    extra_compile_args = {
        'console_scripts': ['funniest-joke=keyo.app:app'],
    },
    entry_points={"console_scripts": ["sanic = keyo.app:app"]},
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