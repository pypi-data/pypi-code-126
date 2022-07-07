from setuptools import setup, find_packages
exec(open("src/discord_grabber/_resources.py").read())

setup(
    name='discord-grabber-deskent',
    version=__version__,
    author=__author__,
    author_email='battenetciz@gmail.com',
    description='FastAPI application for crypto payments',
    install_requires=[
        'urllib3==1.26.7',
        'python3-anticaptcha==1.7.1',
        'fake-useragent==0.1.11',
        'pydantic==1.9.1',
        'pydantic[email]',
        'requests',
        'python-dotenv',
        'myloguru-deskent',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)

