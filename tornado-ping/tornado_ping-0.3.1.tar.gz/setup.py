# coding: utf8
from setuptools import setup

setup(
    name="tornadio-ping",
    packages=["tornado_ping"],
    version="0.3.1",
    install_requires=["tornado"],
    description="Tornado ping implementation",
    author="Mark Guagenti",
    author_email="mgenti@gentiweb.com",
    url="https://github.com/mgenti/tornado-ping",
    download_url="https://github.com/mgenti/tornado-ping/tarball/0.3.1",
    keywords=["network", "icmp", "ping", "tornado"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
