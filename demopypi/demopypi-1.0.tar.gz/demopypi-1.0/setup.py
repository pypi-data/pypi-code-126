import setuptools
from pathlib import Path

setuptools.setup(
    name="demopypi",
    version=1.0,
    long_description=Path("README.txt").read_text(),
    packages=setuptools.find_packages(exclude=["Tests", "Data"])
)