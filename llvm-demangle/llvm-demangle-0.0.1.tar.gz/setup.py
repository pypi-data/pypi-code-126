from setuptools import setup, find_packages, Extension
from subprocess import run
import os
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def do_run(cmd):
    res = run(cmd.split(" "), capture_output=True)
    if res.returncode != 0:
        print(f"Command '{cmd}' failed. Aborting setup.")
        sys.exit(1)
    return res.stdout.decode("ascii")

# Get LLVM CXX flags, LD flags, and demangle library
cxx_flags = do_run("llvm-config --cxxflags")
ld_flags = " ".join([do_run("llvm-config --ldflags"), do_run("llvm-config --libs demangle")])

# Set CXXFLAGS, LDFLAGS, and compiler
os.environ["CC"] = "g++"
os.environ["LDSHARED"] = "g++ -shared"
os.environ["CXXFLAGS"] = cxx_flags
os.environ["LDFLAGS"] = ld_flags

# Cython extension
extensions = [
    Extension(
        "llvmdemangle.demangle",
        ["src/llvmdemangle/demangle.pyx"],
        language="c++",
    ),
]

setup(
    name="llvm-demangle",
    version="0.0.1",
    description="Python wrapper arround llvm::demangle.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="0BSD",
    author="MNayer",
    author_email="marie.nayer@web.de",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/MNayer/llvmdemangle",
    keywords="demangling c++ cxx cpp",
    install_requires=[
        "setuptools>=18.0",
        "Cython",
        "click",
    ],
    ext_modules=extensions,
    entry_points={
        "console_scripts": [
            "demangle = llvmdemangle.tools:demangle",
        ],
    },
)

