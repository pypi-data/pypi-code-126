import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="happycode",
  version="0.0.1",
  author="HappyCode Shabi",
  author_email="happycode@shabi.com",
  description="HappyCode is Shabi!!!",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://www.luogu.com.cn/user/546369",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)