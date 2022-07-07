import setuptools

with open("README.md") as f:
    long_description = f.read()

with open("./yeongnok/__init__.py") as f:
    for line in f.readlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            break
    else:
        print("Can't find version!")
        exit(1)

setuptools.setup(
    name="yeongnok",
    version=version,
    author="Anji Wong",
    author_email="anzhi0708@gmail.com",
    description="Korean National Assembly VOD (영상회의록) Crawler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "korean",
        "congress",
        "politics",
        "video",
        "assembly",
        "VOD",
        "korea",
        "crawler",
        "record"
    ],
    install_requires=["requests", "objprint", "faker"],
    url="https://github.com/anzhi0708/yeongnok",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'': ['*.csv']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Sociology :: History",
        "Topic :: Sociology :: Genealogy",
        "Topic :: Education :: Testing",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
