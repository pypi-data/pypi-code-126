from setuptools import setup, find_packages

with open("README.rst", "r") as f:
    long_description=f.read()

setup(
    name="langtranslator",
    version="1.0.2",
    license="MIT",
    author="Patrik Ackermann",
    author_email="patrik_ackermann@outlook.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    keywords="translate program translation localize localization language languages",
    description="Translate your program to different languages.",
    long_description=long_description,
    long_description_content_type='text/markdown'
)