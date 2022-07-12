from setuptools import setup


with open('readme.md') as f:
    long_description = f.read()


setup(
    name='magicli',
    version='0.1.1',
    description='Automatically call args parsed by `docopt` as functions.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': 'src'},
    py_modules=[
        'magicli',
        'example'
    ],
    install_requires=[
        'docopt'
    ],
    extras_require={
        'tests':[
            'pytest',
        ]
    },
    entry_points={
        'console_scripts':[
            'magicli_example=example:cli'
            ]
        },
    keywords=[
        'python',
        'docopt',
        'cli'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: OS Independent"
    ]
)
