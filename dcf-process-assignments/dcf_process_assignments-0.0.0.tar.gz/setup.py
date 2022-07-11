# DCF process_assignments package
# setup.py: to build the package
# Author: Mubarak Idoko (midoko.dev@gmail.com)
# Date: 06/19/2022

# UPDATE LOG: 
# Format: (Name of author) Date: Note
# (Mubarak Idoko) 06/19/2022: Implemented the setup.py file

# KNOWN ISSUES:
# Format: (Name of author) Date [Critical Score (0-5)]: Notes [Ideas for fix] {Updates (if any)}

from importlib.metadata import entry_points
from setuptools import setup, find_packages

VERSION = '0.0.0'
PACKAGE_NAME = 'dcf_process_assignments'
AUTHOR = 'Mubarak Idoko'
AUTHOR_EMAIL = 'midoko.dev@gmail.com'
URL = 'https://github.com/mubbie/dcf-thankview/tree/main/dev/dcf_process_assignments'
LICENSE = 'MIT'
DESCRIPTION = 'Package to automate processing DCF ThankView Assignments'
LONG_DESCRIPTION = open("./README.md", 'r', encoding='utf-8').read()
LONG_DESC_TYPE = 'text/markdown'
REQUIREMENTS = [x.rstrip("\n") for x in open("./requirements.txt", 'r', encoding='utf-8')]

setup(
    name=PACKAGE_NAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    keywords=['DCF', 'ThankView Assignments Processing', 'Automation'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': [
            'process_assignments = dcf_process_assignments.process_assignments:main',
        ]
    }
)
