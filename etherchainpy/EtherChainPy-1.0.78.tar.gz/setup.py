import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EtherChainPy",
    version="1.0.78",
    author="Emmanuel Adigun",
    author_email="emmanuel@zignal.net",
    description="A python interface to the ethereum blockchain explorer at https://www.etherscan.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZignalNET/EtherChainPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
