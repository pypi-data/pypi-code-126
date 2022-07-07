from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="sv_ttk",
    version=1.0,
    author="rdbende",
    author_email="rdbende@gmail.com",
    url="https://github.com/rdbende/Sun-Valley-ttk-theme",
    license="MIT license",
    description="Use the Sun Valley ttk theme with a Python module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "tkinter",
        "ttk",
        "theme",
        "tcl",
        "tk",
        "tcl/tk",
        "tile",
        "theme",
        "sun-valley",
        "winui",
        "windows-11",
        "dark-theme",
    ],
    python_requires=">=3.4",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Tcl",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["sv_ttk"],
    package_data={
        "sv_ttk": ["sun-valley.tcl", "theme/*", "theme/dark/*", "theme/light/*"]
    },
)
