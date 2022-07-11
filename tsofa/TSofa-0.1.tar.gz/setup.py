# Standard library imports.
import os

# Setuptools package imports.
from setuptools import setup

# Read the README.rst file for the 'long_description' argument given
# to the setup function.
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path.
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name = 'TSofa',
    version = '0.1',
    packages = [
        'tsofa',
        'tsofa.views',
        'tsofa.views.sdocs',
        'tsofa.views.sdocs.cmds',
        'tsofa.views.snums',
        'tsofa.views.snums.cmds',
        'tsofa.views.sobjs',
        'tsofa.views.sobjs.cmds',
        'tsofa.views.svals',
        'tsofa.views.svals.cmds'],
    entry_points = {'console_scripts': [
        'tsofa-sdocs-dy = tsofa.views.sdocs.cmds.dy:main',
        'tsofa-sdocs-hr = tsofa.views.sdocs.cmds.hr:main',
        'tsofa-sdocs-mn = tsofa.views.sdocs.cmds.mn:main',
        'tsofa-sdocs-sc = tsofa.views.sdocs.cmds.sc:main',
        'tsofa-snums-dy = tsofa.views.snums.cmds.dy:main',
        'tsofa-snums-hr = tsofa.views.snums.cmds.hr:main',
        'tsofa-snums-mn = tsofa.views.snums.cmds.mn:main',
        'tsofa-snums-sc = tsofa.views.snums.cmds.sc:main',
        'tsofa-sobjs-dy = tsofa.views.sobjs.cmds.dy:main',
        'tsofa-sobjs-hr = tsofa.views.sobjs.cmds.hr:main',
        'tsofa-sobjs-mn = tsofa.views.sobjs.cmds.mn:main',
        'tsofa-sobjs-sc = tsofa.views.sobjs.cmds.sc:main',
        'tsofa-svals-dy = tsofa.views.svals.cmds.dy:main',
        'tsofa-svals-hr = tsofa.views.svals.cmds.hr:main',
        'tsofa-svals-mn = tsofa.views.svals.cmds.mn:main',
        'tsofa-svals-sc = tsofa.views.svals.cmds.sc:main']},
    install_requires = ['pytz >= 2020.4', 'qrazyv >= 1a2'],
    license = 'BSD License',
    description = 'This package contains the reference CouchDB views for '\
        + 'well formatted timeseries data, the Python functionality to '\
        + 'retrieve data from those views, and functionality to process '\
        + 'the output.',
    long_description = README,
    url = 'https://bitbucket.org/notequal/tsofa/',
    author = 'Stanley Engle',
    author_email = 'stan.engle@gmail.com',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'],)
