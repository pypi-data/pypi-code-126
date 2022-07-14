from setuptools import find_packages, setup

VERSION = "0.0.0"
setup(
    name="jamesukae",
    version=VERSION,
    packages=find_packages(),
    python_requires=">=3.8.0",
    install_requires=[
        "requests>=2.27",
        "cryptography>=37.0",
        "betterproto>=1.2",
        "paho-mqtt>=1.6",
        "ntplib>=0.4",
    ],
)
