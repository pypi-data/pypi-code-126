import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

pkg_location = 'src'
pkg_name = 'schwicv'

# This call to setup() does all the work
setup(
    name="schwicv",
    version="0.0.7",
    description="Schwi's Utilities",
    long_description=README,
    long_description_content_type="text/markdown",
    py_modules=[pkg_name],
    url="https://github.com/Schwi88/SchwiCV",
    author="Thomas Schwingenschlögl",
    author_email="office@schwi.at",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(where=pkg_location, exclude=['tests']),
    package_dir={'': pkg_location},
    install_requires=[],
    entry_points={
        "console_scripts": []
    },
)
