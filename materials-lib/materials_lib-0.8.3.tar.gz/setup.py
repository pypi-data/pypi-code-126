from setuptools import setup, find_packages

VERSION = '0.8.3'
DESCRIPTION = 'Open and configurable materials library for Python.'

# Read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Add resource links
project_urls = {
    'Repository': 'https://gitlab.com/johnhal/materials-python'
}

# Setting up
setup(
    name="materials_lib",
    version=VERSION,
    author="John Halazonetis",
    author_email="<john.halazonetis@icloud.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=open("requirements.txt", "r").read().split("\n"),
    keywords=['python', 'materials'],
    project_urls=project_urls,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
