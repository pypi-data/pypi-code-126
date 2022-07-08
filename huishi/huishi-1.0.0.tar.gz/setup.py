import setuptools

with open("README.md", "r",encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="huishi",
    version="1.0.0",
    author="ZenMeHuiShiNe",
    author_email="2020302111360@whu.edu.cn",
    description="A package that can let you create a poem by AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/wangshixincheng/keywords_to_poem",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)