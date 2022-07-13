from setuptools import setup, find_packages


def readme():
    with open('./README.md', 'r') as readme:
        return readme.read()


VERSION = '1.0.2'
DESCRIPTION = 'Simply pre-written small packages that implement in code'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="vunv79_utilities",
    version=VERSION,
    author="Vu Nguyen",
    author_email="vuviet.nguyen.it@gmail.com",
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "confluent-kafka==1.9.0",
        "requests~=2.28.1",
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
