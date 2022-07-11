import setuptools

setuptools.setup(
    name="orpl",
    version="100.0.2.1",
    author="OpenRE",
    description="The fork of simpledemotivators",
    url="https://github.com/Daemon-RE/openre-pylib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
)
