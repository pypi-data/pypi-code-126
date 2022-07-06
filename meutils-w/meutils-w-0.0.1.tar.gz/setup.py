from time import time
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
setuptools.setup(
     name="meutils-w",
     version="0.0.1",
     author="wangdexiang",
     author_email="k7856499@163.com",
     description="A test package",
     long_description=long_description,
long_description_content_type="text/markdown",
     url="https://github.com/pypa/sampleproject",
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
