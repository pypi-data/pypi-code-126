from setuptools import setup, find_packages
import os

LONG_DESCRIPTION = """

# hello!
thanks xd

"""
DESCRIPTION = "Simple!"

setup(
    name="toptengen",
    version="1.0.0",
    author="GoodWorks Soft Co.",
    author_email="<tylerfromgw@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pibrella'],
    keywords=["top ten maker", "csvtools"],
    
)