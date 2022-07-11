import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="steel_seal",
    version="0.0.5",
    author="afeyer",
    author_email="afeyer@h5base.cn",
    description="简单、易用且支持防重放的签名工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    python_requires='>=3.0',  # 对python的最低版本要求
)