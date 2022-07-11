from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'alice blue '
LONG_DESCRIPTION = "use alice blue without api"

# Setting up
setup(
    name="alicelue_brocker_wihtoutapi",
    version=VERSION,
    author="Gourav",
    author_email="kgourav@combiz.org",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['alice blue', 'alice blue no api use'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)