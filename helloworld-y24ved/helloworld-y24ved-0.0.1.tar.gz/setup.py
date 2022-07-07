from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='helloworld-y24ved',
    version='0.0.1',
    description='Say hello',
    py_modules=["helloworld"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires= [
        "click~=8.0.4",
    ],
    extras_require = {
        "dev": [
            "pytest>=7.0.1",
        ],
    },
    url="https://github.com/y24ved/helloworld",
    author="y24 ved",
    author_email="y24.ved@gmail.com",
)
