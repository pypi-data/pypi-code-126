import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name="SnowML",
    version="0.2.0",
    author="Shlomi Green",
    maintainer="Shlomi Green",
    author_email="Shlomi.G@openweb.com",
    long_description="A full utility package for ML engineers & Data Scientists",
    description="Openweb's ML utility package",
    long_description_content_type="text/markdown",
    url="https://github.com/SpotIM/openweb-ml-utils",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
    install_requires=[
        "pandas",
        "scikit-learn",
        "numpy",
        "slack-sdk",
        "mlflow",
        "scipy",
        "pyspark"
    ]
)