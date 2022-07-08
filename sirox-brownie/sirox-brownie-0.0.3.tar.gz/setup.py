from setuptools import setup, find_namespace_packages

setup(
    name="sirox-brownie",
    version="0.0.3",
    description="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["eth-brownie"],
    packages=find_namespace_packages(include=["sirox.*"]),
)
