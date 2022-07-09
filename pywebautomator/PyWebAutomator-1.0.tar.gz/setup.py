from setuptools import setup

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Microsoft :: Windows"
]

setup(
    name="PyWebAutomator",
    version="1.0",
    license="MIT",
    author="Sanjay Kumar Y R",
    author_email="seenusanjay20102002@gmail.com",
    packages= ["PyWebAutomator"],
    install_requires = ["selenium"],
    keywords="Web Automation",
    url="https://github.com/yrzgithub/PyWebAutomator",
    description="A Python Package developed using selenium for web automation",
    long_description = open("README.txt").read(),
    classifiers=classifiers,
)
