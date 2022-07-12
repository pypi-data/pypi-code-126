from setuptools import setup, find_packages


setup(
    name="python-technology-CZ10-loterie-a",
    version="1.0.0",
    author="Pavel Eis",
    author_email="aisik004@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    description="Knihovna pro ucely vyuky Pythonu skupiny SDA CZ10.",
    long_description="Tento balicek implementuje jednoduchou loterii pro ucely vyuky Pythonu skupiny SDA CZ10.",
    install_requires=["alive-progress"],
    python_requires=">=3.8"
)
