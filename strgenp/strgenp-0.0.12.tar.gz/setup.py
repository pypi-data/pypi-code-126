from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.12'
DESCRIPTION = 'generate Random string'


# Setting up
setup(
    name="strgenp",
    version=VERSION,
    author="mahinbinhasan (Mahin Bin Hasan)",
    author_email="<allmahin149@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'password generator'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)