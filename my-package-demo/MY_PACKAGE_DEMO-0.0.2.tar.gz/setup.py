import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="MY_PACKAGE_DEMO",
    version="0.0.2",
    author="jquan",
    author_email="jinquan6369@163.com",
    description="A chinese package_demo tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    # packages=setuptools.find_packages(),
    packages=['package_demo'],
    package_dir={'package_demo': 'package_demo'},
    package_data={'package_demo': ['*.*', 'conf/*', 'data/*', 'infer_model/*']},
    # install_requires=['paddlepaddle>=1.5.0', ],
    platforms="any",
    license="MIT Licence",

    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
