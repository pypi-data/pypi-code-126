import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tkar",
    version="1.0.3",
    description="android reversing automation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abeljm/Tool-Kit-Android-Reverser-V2.0",
    author="Avelino Navarro",
    author_email="abeljm2017@gmail.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    entry_points={
        "console_scripts": [
            "tkar=tkar.tkar:main",
        ]
    }
)
