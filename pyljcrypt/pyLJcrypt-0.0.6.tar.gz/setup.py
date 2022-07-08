from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.6'
DESCRIPTION = 'Making Encrypting and Decrypting easy.'

# Setting up
setup(
    name="pyLJcrypt",
    version=VERSION,
    author="Louiejay S. Boglosa",
    author_email="boglosalouiejay@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['cryptography'],
    keywords=['python', 'cryptography', 'encrypting', 'decrypting'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)