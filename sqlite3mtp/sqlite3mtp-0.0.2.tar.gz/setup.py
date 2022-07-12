import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlite3mtp",
    version="0.0.2",
    author="laishuhan",
    author_email="3027826050@qq.com",
    description="to manipulate a sqlite3 database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laishuhan/sqlite3mtp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)