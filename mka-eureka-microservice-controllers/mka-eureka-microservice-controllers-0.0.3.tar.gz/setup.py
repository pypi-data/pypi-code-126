import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mka-eureka-microservice-controllers",
    version="0.0.3",
    author="Adnan Aji",
    author_email="",
    description="A package contains scripts to easily connection between connected django microservice with eureka",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={'':"src"},
    packages=find_packages("src"),
    python_requires=">=3.6",
    entry_points={
                        'console_scripts': [
                                'hwpypcmd=hwpyp.mypy:sayHello',
                        ]
                }
)