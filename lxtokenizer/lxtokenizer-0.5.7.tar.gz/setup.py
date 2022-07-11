from setuptools import setup

setup(
    name="lxtokenizer",
    url="https://gitlab.nlx.di.fc.ul.pt/lx/lxtokenizer",
    author="Luís Gomes (the Python stuff); António Branco and João Silva",
    author_email="luis.gomes@di.fc.ul.pt",
    version="0.5.7",
    description="LX-Tokenizer segments text into lexically relevant tokens.",
    package_dir={"": "src"},
    install_requires=["docopt", "lxcommon", "openfile", "toolwrapper"],
    include_package_data=True,
    packages=["lxtokenizer"],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["lx-tokenizer=lxtokenizer.__main__:main"]},
)
