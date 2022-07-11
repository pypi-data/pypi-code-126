import setuptools

setuptools.setup(
    name="facebook-events-scraper",
    version="0.0.1",
    author="ZhouZ-1",
    description="A simple tool to scrape Facebook events using Selenium",
    packages=["facebook_events"],
    install_requires=[
        "webdriver-manager==3.5.4",
        "pybrowsers",
        "selenium==3.141.0",
        "python-dateutil",
    ],
    license='MIT',
)
