from setuptools import setup, find_packages

setup(
    name="regex_hir",
    version="0.1.0",
    license="MIT",
    author="Dexter Hill",
    packages=find_packages("regex_hir"),
    package_dir={"": "regex_hir"},
    url="https://github.com/DexterHill0/regex_hir",
    keywords="regex python syntax ast",
    install_requires=[
        "unicategories==0.1.1",
    ],
)
