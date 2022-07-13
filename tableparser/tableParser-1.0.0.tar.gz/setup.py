import pathlib
from setuptools import setup

# try: # for pip >= 10
#     from pip._internal.req import parse_requirements
# except ImportError: # for pip <= 9.0.3
#     from pip.req import parse_requirements

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]



install_reqs = parse_requirements('requirements.txt')
reqs = install_reqs


# This call to setup() does all the work
setup(
    name="tableParser",
    version="1.0.0",
    description="It extract the table data from the pdf",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abhishekthegodfather/tableDataParser.git",
    author="Abhishek Biswas",
    author_email="abhishekbiswas772@gmail.com",
    # license="MIT",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    packages=["tableParser"],
    include_package_data=True,
    install_requires= reqs,
    entry_points={
        "console_scripts": [
            "tableParser=tableParser.__main__:main",
        ]
    },
)