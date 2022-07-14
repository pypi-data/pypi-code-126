from setuptools import setup, find_packages

setup(
    name="langtranslator",
    version="1.0",
    license="MIT",
    author="Patrik Ackermann",
    author_email="patrik_ackermann@outlook.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    keywords="translate program translation localize localization language languages",
    install_requires=[
        "json"
    ]
)