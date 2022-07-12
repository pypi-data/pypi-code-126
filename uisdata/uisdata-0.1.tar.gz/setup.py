import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='uisdata',
    version='0.1',
    author='Maxime Murphy',
    author_email='maxime.murphy@gmail.com',
    description='Consumes the UIS Bulk Data Download System (BDDS): get, select, subset, merge metadata/labels, search, other utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Maxime-Murphy/uisdata',
    # see https://pypi.org/classifiers/
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    # Add minimal working version when known
    install_requires=[
        'pandas',
        'requests',
        'numpy'
    ]
)
