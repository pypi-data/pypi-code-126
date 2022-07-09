# sourcery skip: path-read
from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A library for data structures.'


with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="profq_data",
    version=VERSION,
    author="ProfessorQu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python', 'data structures', 'algorithms'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)