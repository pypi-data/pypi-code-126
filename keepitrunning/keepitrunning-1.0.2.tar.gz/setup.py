import os
import setuptools

with open("/home/runner/termux-1/keepitrunning/README.md", "r") as fh:
    long_description = fh.read()

with open('/home/runner/termux-1/keepitrunning/requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="keepitrunning",
    version="1.0.2",
    author="jiroawesome",
    description="A simple python library that makes your python website 24/7.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiroawesome/keepitrunning",
    project_urls={
        "Bug Tracker": "https://github.com/jiroawesome/keepitrunning/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    package_data={'': ['**/*']},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=required
)