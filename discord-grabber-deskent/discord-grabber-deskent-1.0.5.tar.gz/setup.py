from setuptools import setup, find_packages
exec(open("src/discord_grabber/_resources.py").read())

setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email='battenetciz@gmail.com',
    description='Discord token grabber',
    install_requires=[
        'urllib3==1.26.7',
        'python3-anticaptcha==1.7.1',
        'pydantic==1.9.1',
        'pydantic[email]',
        'requests==2.28.1',
        'python-dotenv==0.19.2',
        'myloguru-deskent==0.0.12',
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

