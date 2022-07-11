from setuptools import setup
from pywaveapps import __version__
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="PyWaveApps",
    version=__version__,
    description="API Connection to the WaveApps (https://www.waveapps.com/) API.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/The-Nicholas-R-Barrow-Company-LLC/PyWaveApps",
    author="The Nicholas R. Barrow Company, LLC",
    author_email="me@nicholasrbarrow.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    packages=["pywaveapps"],
    install_requires=["gql[all]"],
    project_urls={
        'Source': 'https://github.com/The-Nicholas-R-Barrow-Company-LLC/PyWaveApps',
        'Tracker': 'https://github.com/The-Nicholas-R-Barrow-Company-LLC/PyWaveApps/issues',
    }
)
