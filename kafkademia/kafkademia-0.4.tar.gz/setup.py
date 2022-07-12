import re
import setuptools

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('kafkademia/kafkademia.py').read(),
    re.M
).group(1)

setuptools.setup(
    name="kafkademia",
    version=version,
    packages=["kafkademia"],
    entry_points = {
        "console_scripts": ['kafkademia = kafkademia.kafkademia:main']
        },
    author_email="ulises.ramirez@datalytics.com",
    package_dir={"kafkademia": "kafkademia"},
    license="MIT",
    install_requires=[
        'kafka-python',
    ]
)
