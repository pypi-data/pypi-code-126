import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="facebook-events-scraper",
    version="0.0.2",
    author="ZhouZ-1",
    description="A simple tool to scrape Facebook events using Selenium",
    packages=["facebook_events"],
    install_requires=[
        "webdriver-manager==3.5.4",
        "pybrowsers",
        "selenium==3.141.0",
        "python-dateutil",
    ],
    license="MIT",
    author_email="me@zzhou.dev",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
