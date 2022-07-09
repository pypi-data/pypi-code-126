from setuptools import setup, find_packages

VERSION = "0.0.3"
DESCRIPTION = "polyexpose"
LONG_DESCRIPTION = "polyexpose package"

# Setting up
setup(
    name="polyexpose",
    version=VERSION,
    author="Luis Velasco",
    author_email="<luis.velasco@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=["polyexpose"],
    package_dir={"polyexposepkg": "polyexpose"},
    include_package_data=True,
    data_files=[("polyexpose", ["polyexpose/data/userdata.parquet"])],
    install_requires=[
        "google-cloud-dataproc",
        "google-cloud-storage",
        "pyspark~=3.3.0",
        "pyyaml",
        "google-cloud-pubsublite==1.4.2",
        "protobuf",
        "requests",
    ],
    keywords=["python", "polyexpose"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
