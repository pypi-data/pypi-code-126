# setup.py
from setuptools import setup

requirements = [
    'click',
    'PyYAML>5.1',
    'colr',
    'asciitree'
]

setup(
    name = 'jtv',
    version = '1.74.0',
    long_description = 'A command line utility which allows you to visualise the nodes in a JSON file (or GET request) as an ASCII tree.',
    platforms = 'Linux',
    license = 'MIT',
    url = 'https://github.com/astrocyte-medical/jtv',
    author = 'Astrocyte Medical LTD',
    author_email = 'horia.muntean@astrocyte-medical.com',
    package_dir = {"":"src"},
    packages = ['jtv'],
    install_requires = requirements,
    setup_requires = ['setuptools'],
    tests_require = ['pytest', 'tox', 'flake8'],
    zip_safe = True,
    entry_points = {
        'console_scripts': [
            'jtv = jtv:main',
        ]
    }
)
