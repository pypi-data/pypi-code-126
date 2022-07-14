from setuptools import setup

setup(
    # name of package
    name='data-inspect',

    version='0.0.1',
    description='tool to assess data',

    # which folders will be uploaded
    py_modules=["data-inspect"],

    # telling code is under source directory
    package_dir={'': 'src'},

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ],

    install_requires=[
        "pandas",
        "bokeh",
        "notebook",
        "scikit-learn"
    ],

    license='MIT',

    author='Rens Jochemsen',
    author_email='rensjochemsen@gmail.com'
)
