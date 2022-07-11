from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'tradingview alert in python '
LONG_DESCRIPTION = "get tradingview alert using session id"

# Setting up
setup(
    name="tradingview_alert",
    version=VERSION,
    author="Gourav",
    author_email="kgourav@combiz.org",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['tradingview alert', 'tradingview'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)