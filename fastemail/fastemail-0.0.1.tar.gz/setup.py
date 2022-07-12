import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastemail",
    version="0.0.1",
    author="laishuhan",
    author_email="3027826050@qq.com",
    description="send email by python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laishuhan/fastemail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)