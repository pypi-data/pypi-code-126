from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="leetcodetest",
    version="0.0.1",
    description="A simple leetcode testing utility.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asmeili/LeetcodeTest",
    author="Asmeili",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="leetcode",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=[],
    project_urls={
        "Bug Reports": "https://github.com/Asmeili/LeetcodeTest/issues",
        "Source": "https://github.com/Asmeili/LeetcodeTest",
    },
)