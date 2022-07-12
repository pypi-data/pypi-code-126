from setuptools import setup, find_packages


setup(
    name="lxsentencesplitter",
    url="https://gitlab.nlx.di.fc.ul.pt/lx/lxsentencesplitter",
    author="Luís Gomes (the Python stuff); António Branco and João Silva",
    author_email="luis.gomes@di.fc.ul.pt",
    version="1.0.13",
    description="LX-SentenceSplitter identifies sentence and paragraph boundaries.",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    install_requires=["docopt", "openfile", "lxcommon>=2.6.0"],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["lx-sentencesplitter=lxsentencesplitter.__main__:main"],
    },
)
