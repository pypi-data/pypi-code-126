import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pip-test-pkg",
    version="1.0.0",
    author="anubhavs",
    author_email="",
    description="A small demo package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anubhavs9/pip-test-pkg",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
