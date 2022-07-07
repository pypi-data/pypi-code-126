from setuptools import setup, find_packages

setup(
    name="calendariUS",
    version="0.2.0",
    author="so07",
    author_email="s.orlandini@cineca.it",
    description="Generate calendar for Help Desk shifts",
    long_description="""Generate calendar for Help Desk shifts""",
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["python-dateutil", "ics"],
    entry_points={
        "console_scripts": ["calendarius=calendarius.calendarius:main"],
    },
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
)
