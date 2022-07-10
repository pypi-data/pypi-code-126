import setuptools

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="wordfreak",
    version="0.0.6",
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="",
    long_description=readme,
    license=license,
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=["PyPDF2",
                      "docx2txt",
                      "setuptools"]
)
