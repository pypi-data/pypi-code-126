import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Harvard Lib",
    version="1.0.0",
    author="Ulif Systems",
    author_email="support@ulifsystems.tech",
    description="A Python library that contains multiple other libraries created by Ulif Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://54.234.189.76",
    project_urls={
        "DiscordRPC Website": "http://54.234.189.76/rpc",
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