from setuptools import setup, find_packages


setup(
    name='hex_color_output',
    version='1.1.2',
    license='MIT',
    author="Cownex",
    description="Color the output with Hex Color Codes.",
    author_email='contact@cownex.de',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    url='https://github.com/Cownex/HexOutput',
    keywords='python hex color terminal output color-output',
)