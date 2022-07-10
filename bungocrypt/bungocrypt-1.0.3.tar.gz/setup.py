from setuptools import setup

setup(
    name="bungocrypt",
    version="1.2",
    license="MIT",
    description="bungocrypt is an encryption library for python. It's secure and key based so it will keep your data safe!",
    author="NikkieDev Software",
    author_email="business@nikkiedev.com",
    packages=["bungocrypt"],
    package_dir={'': 'src'},
    url="https://github.com/NikkieDev/bungocrypt-python",
    download_url="https://github.com/NikkieDev/bungocrypt-python/archive/refs/tags/v1.2.tar.gz",
    keywords="Encryption, decryption, fernet, cryptography, crypto, security, data, safety"
)