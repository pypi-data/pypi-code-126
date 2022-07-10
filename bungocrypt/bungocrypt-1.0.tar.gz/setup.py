from setuptools import setup, find_packages

setup(
    name="bungocrypt",
    version="1.0",
    license="MIT",
    author="NikkieDev Software",
    author_email="business@nikkiedev.com",
    packages=find_packages('bungocrypt'),
    package_dir={'': 'bungocrypt'},
    url="https://github.com/NikkieDev/bungocrypt-python",
    keywords="Encryption, decryption, fernet, cryptography, crypto, security, data, safety"
)