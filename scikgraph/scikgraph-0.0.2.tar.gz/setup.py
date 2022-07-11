from setuptools import find_packages, setup

setup(
    name='scikgraph',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'nltk',
        'matplotlib',
        'networkx==2.3',
        'flask_bootstrap',
        'py2cytoscape',
    ],
)
