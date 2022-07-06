from setuptools import find_packages, setup

setup (
    name="creativiousUtilities",
    packages=find_packages(include=["creativiousUtilities"]),
    version='1.1.0',
    description="General purpose prebuilt functions for any project that I work on",
    author="Creativious",
    author_email="timothy@creativious.net",
    license="MIT",
    install_requires=["colorlog"]
)

