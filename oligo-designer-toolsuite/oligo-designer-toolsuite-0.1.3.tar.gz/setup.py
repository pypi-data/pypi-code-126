from distutils.core import setup

setup(
    name='oligo-designer-toolsuite',
    version='0.1.3',
    summary='Oligo designer toolsuite',
    description='Oligo designer toolsuite',
    packages=['oligo_designer_toolsuite', 'oligo_designer_toolsuite.pipelines'],
    install_requires=['datetime', 'argparse', 'pandas', 'iteration_utilities', 
                      'Bio', 'gtfparse', 'pyfaidx', 'pyyaml', 'pybedtools', 'networkx'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lisa Barros de Andrade e Sousa',
    entry_points={
        'console_scripts': [
            'padlock_probe_designer = oligo_designer_toolsuite.pipelines.padlock_probe_designer:main'
        ]
    },
)
