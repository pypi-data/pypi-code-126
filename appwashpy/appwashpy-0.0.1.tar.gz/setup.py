from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="appwashpy",
    version="0.0.1",
    description="Inofficial API Client for appWash by Miele.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="fapfaff",
    author_email="fabian-pfaff@outlook.de",
    url="https://github.com/fapfaff/appwashpy",
    package_dir={"": "appwashpy"},
    packages=["appwashpy"],
    license="GNU General Public License 3",
    python_requires=">=3.6.0",
    install_requires=[
        "requests"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-mock"
            "autopep8"
        ]
    }
)
