"""
MAVTel package setup
    Keywords: https://setuptools.pypa.io/en/latest/references/keywords.html
    A good example of setup.py can be found here: https://github.com/pypa/sampleproject/blob/main/setup.py
    Packaging HOWTO: https://packaging.python.org/en/latest/tutorials/packaging-projects/
"""
import os
import subprocess

from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

try:
    with open(os.path.join(ROOT_DIR, '.VERSION')) as f:
        version = f.readlines()[0]
except FileNotFoundError:
    version = subprocess.check_output('git describe --tags --abbrev=0', cwd=ROOT_DIR, shell=True)

with open(os.path.join(ROOT_DIR, 'mavtel_client', 'README.md'), encoding='utf-8') as fs:
    long_description = fs.read()

test_dependencies = [
    'aiounittest>=1.4.2',
    'coverage>=6.4',
    'pytest>=7.1',
]

extras = {
    'test': test_dependencies,
}

setup(
    name='mavtel-client',
    version=version,
    description='Client for MAVTel',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    author='Mykhailo Ziatin',
    author_email='mikhail.zyatin@gmail.com',
    packages=find_packages(
        where='.',
        include=['mavtel_models**', 'mavtel_client**'],
    ),
    package_dir={'': '.'},
    python_requires='>=3.7, <4',
    install_requires=[
        'httpx>=0.23.0',
        'inflection>=0.5.1',
        'orjson>=3.7.7',
        'pydantic>=1.9.1',
        'websockets>=10.3',
    ],
    setup_requires=[],
    license_files=('LICENSE',),
    tests_require=test_dependencies,
    extras_require=extras,
    data_files=[('version', ['.VERSION', '.BUILD']), ('docs', ['mavtel_client/README.md'])],
    url='https://gitlab.com/Zyatin/mavtel/mavtel_client',
    project_urls={
        'Bug Reports': 'https://gitlab.com/Zyatin/mavtel/-/issues',
        'Source': 'https://gitlab.com/Zyatin/mavtel',
        'Homepage': 'https://gitlab.com/Zyatin/mavtel/mavtel_client',
    },
)
