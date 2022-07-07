from setuptools import setup, find_packages
import os

LONG_DESCRIPTION = "Simple!"
DESCRIPTION = "Simple!"

setup(
    name="toptenticle",
    version="0.0.1",
    author="Tk",
    author_email="<tylerfromgw@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pibrella'],
    keywords=["top ten maker", "csvtools"],
    classifiers=[
        "Development Status :: 1 - Dev",
        "Intended Audience :: Hobbyists",
        "Programming Language :: Python :: 3"
    ]
)