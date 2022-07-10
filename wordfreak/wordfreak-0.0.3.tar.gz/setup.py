import setuptools

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="wordfreak",
    version="0.0.3",
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="",
    long_description=readme,
    license=license,
    packages=setuptools.find_packages(exclude=("test", "docs"))
)
