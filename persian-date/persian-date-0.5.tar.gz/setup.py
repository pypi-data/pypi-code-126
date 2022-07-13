from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
def readme():
    with open('README.md') as f:
        return f.read()
setup(
    name='persian-date',
    packages=['persian-date'],
    version='0.5',
    license='MIT',
    description='A library that gives user date in persian calender',
    long_description=readme(),
    author='Bardia Nikbakhsh',
    author_email='BardiaNikbakhsh@gmail.com',
    url='https://github.com/bardianz/PersianDate-python-package',
    download_url='https://github.com/bardianz/PersianDate-python-package/archive/refs/tags/v_0.2.tar.gz',
    keywords=['Persian Date', 'PersianCalender', 'SolarCalender'],
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
