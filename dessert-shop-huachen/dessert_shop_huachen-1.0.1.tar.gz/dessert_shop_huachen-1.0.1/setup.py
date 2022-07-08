import setuptools

with open("README.md","r") as f:
    long_description = f.read()

setuptools.setup(
    name="dessert_shop_huachen",
    version="1.0.1",
    author="JOJO_li",
    author_email="1010153649@qq.com",
    description="infra监控",
    url="https://github.com/lihuachenw/li.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
