from setuptools import setup

setup(
    name='BRLibraryDocumentor',
    version='1.0.0',
    packages=['brLibrarydocumentor'],
    url='https://github.com/brcclark/mkdocs-md-fb-faceplate-converter',
    license='GPL-3',
    author='Connor Trostel',
    include_package_data=True,
    author_email='connor.trostel@br-automation.com',
    description='B&R Function Block Markdown Face Plate Converter is a tool to translate a special code block in markdown to a B&R documentation faceplate design.',
    install_requires=['mkdocs'],

    entry_points={
        'mkdocs.plugins': [
            'br-as-library-documenter = brLibrarydocumentor:BRLibraryDocumentor',
        ]
    },
)
