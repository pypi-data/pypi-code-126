import setuptools

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="wordfreak",
    version="0.0.8",
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="Word Freak is a Python library that extracts word frequencies from files.",
    license=license,
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=["PyPDF2",
                      "docx2txt",
                      "setuptools"]
)
