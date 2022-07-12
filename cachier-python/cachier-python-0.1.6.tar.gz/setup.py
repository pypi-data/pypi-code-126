import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='cachier-python',
    version='0.1.6',
    author='apinanyogaratnam',
    author_email='apinanapinan@icloud.com',
    description='A python wrapper package for connecting to a self-hosted cachier service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/apinanyogaratnam/cachier-python',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10.4',
    install_requires=[
        'requests',
    ],
)
