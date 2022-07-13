import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="astocktrade",
    version="0.0.3",
    author="laishuhan",
    author_email="3027826050@qq.com",
    description="some tools for astocktrade",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laishuhan/astocktrade",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)