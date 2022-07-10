from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='laapyCore',
    version='0.0.2',
    description='core utils',
    py_modules=["working_tools, mathCore"],
    package_dir={'': 'src'},
    install_requires=[
        "numpy ~= 1.23.0",
        "matplotlib ~= 3.5",
        "pandas~=1.4",
        "scipy~=1.8",
        "sympy~=1.1",

    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Leik Andre Asbjørnsen Butenschøn',
    author_email='nordavindltd@gmail.com',
    url='https://github.com/Leikaab/laapyCore',

    extras_require={
        'dev': [
            'pytest>=7.1.2',
            'check-manifest>=0.48',
            'twine==4.0.1',
            'tox==3.25.1'

        ],
    },
)
