import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

description = (
    'A Python script that generates a new Django secret key and prints it to stdout.'
)

setuptools.setup(
    name='django-make-secret-key',
    version='1.0.0',
    author='Armandt van Zyl',
    author_email='armandtvz@gmail.com',
    description=description,
    license='GPL-3.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/armandtvz/django-make-secret-key',
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Django >=3.2',
    ],
)
