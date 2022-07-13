from importlib.resources import path
import setuptools
from pathlib import Path

setuptools.setup(
    name="Redurpdf",
    version=1.0,
    long_description="path().read_text()",
    packages=setuptools.find_packages(exclude=["data", "tests"])


)
