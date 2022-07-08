import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="braveox",
    version="1.2.5",
    author="Inn Ritsukenn",
    author_email="ylx2005114514@163.com",
    description="You can turn your number into a new type.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://space.bilibili.com/426222659",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
