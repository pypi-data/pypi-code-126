from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='akxurl',
    version='1.0.1',
    description='Py Url Shortener ',
    author= 'AKXVAU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['weather','weather info'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    py_modules=['Py_Weather'],
    package_dir={'akxurl':'src'},
    install_requires = [
        'lolcat',
        'requests',
    ]
)
