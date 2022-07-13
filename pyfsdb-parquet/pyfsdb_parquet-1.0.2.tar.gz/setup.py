import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfsdb_parquet",
    version="1.0.2",
    author="Wes Hardaker",
    author_email="opensource@hardakers.net",
    description="Python tools to convert to and from FSDB and parquet files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gawseed/pyfsdb_parquet",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pdb2parquet = pyfsdb_parquet.tools.fsdb2parquet:main",
            "parquet2pdb = pyfsdb_parquet.tools.parquet2fsdb:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyfsdb>=2.0.3',
        'cramjam', # fails to auto install?
        'pandas',
        'fastparquet',
        'pyarrow'
    ],
    python_requires=">=3.6",
    test_suite="nose.collector",
    tests_require=["nose"],
)
