"""
Python Utilities for Microsoft Azure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyazureutils is a collection of utilities for interacting with Microsoft Azure.

pyazureutils can be used as a library by instantiating any of the contained classes.

Overview
~~~~~~~~

pyazureutils is available:
    * install using pip from pypi: https://pypi.org/project/pyazureutils
    * browse source code on github: https://github.com/microchip-pic-avr-tools/pyazureutils
    * read API documentation on github: https://microchip-pic-avr-tools.github.io/pyazureutils
    * read the changelog on github: https://github.com/microchip-pic-avr-tools/pyazureutils/blob/main/CHANGELOG.md

Dependencies
~~~~~~~~~~~~
This package uses pyedbglib through other libraries for USB communications.
For more information see: https://pypi.org/project/pyedbglib/

Logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This package uses the Python logging module for publishing log messages to library users.
A basic configuration can be used (see example), but for best results a more thorough configuration is
recommended in order to control the verbosity of output from dependencies in the stack which also use logging.
"""
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
