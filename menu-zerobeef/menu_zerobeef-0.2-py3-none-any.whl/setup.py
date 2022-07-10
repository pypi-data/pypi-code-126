from setuptools import find_packages, setup

setup(
    name="menu",
    version="0.2",
    author="Erik",
    author_email="zerobeef@icloud.com",
    description="A simple menu program for command line enthusiasts made possible using curses",
    url="https://github.com/erikkamph/project_menu",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
