from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pycircpl',
    version='1.0',
    description='Python logic circuit programming language',
    keywords='logic circuit programming language',
    author='Samy Zafrany',
    url='https://www.samyzaf.com/pycircpl/pycircpl.html',
    author_email='sz@samyzaf.com',
    license='MIT',
    packages=['pycircpl'],
    zip_safe=False,
)

