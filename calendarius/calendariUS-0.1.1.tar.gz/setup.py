from setuptools import setup, find_packages

setup(
    name="calendariUS",
    version="0.1.1",
    author="so07",
    author_email="s.orlandini@cineca.it",
    description="Generate calendar for Help Desk shifts",
    long_description="""Generate calendar for Help Desk shifts""",
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["python-dateutil"],
    entry_points={
        "console_scripts": ["calendarius=calendarius.calendarius:main"],
    },
)
