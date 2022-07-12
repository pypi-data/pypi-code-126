from setuptools import setup, find_packages

setup(
    name="deepsmirud",
    version="0.1.1",
    keywords=("pip", "deepsmirud"),
    description="deepsmirud",
    long_description="deep learning SM-miR relation",
    license="MIT",

    url="https://github.com/2003100127/deepsmirud",
    author="Jianfeng Sun",
    author_email="jianfeng.sunmt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>3.6',
    install_requires=[
        'pandas',
        'numpy',
        'biopython',
        'pyfiglet',
        'click',
        'tensorflow',
        'rdkit-pypi',
    ],
    entry_points={
        'console_scripts': [
            'deepsmirud=deepsmirud.Main:main',
            'deepsmirud_download=deepsmirud.Main:download',
        ],
    }
)
