import os

from setuptools import setup, Extension

NAME = 'pyoslog'

about = {}
working_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), NAME)
with open(os.path.join(working_directory, '__version__.py')) as version_file:
    exec(version_file.read(), about)

with open('README.md') as readme_file:
    readme = readme_file.read()

# TODO: see https://pypi.org/project/ctwin32/ for a Windows example of configuring wheel tags
# see compatibility.py - allow installation on older versions (or other OSs) but provide is_supported() at runtime
compatibility_module_name = 'compatibility'
compatibility_module_path = os.path.join(working_directory, '%s.py' % compatibility_module_name)
try:
    # noinspection PyUnresolvedReferences
    import importlib.util

    spec = importlib.util.spec_from_file_location(compatibility_module_name, compatibility_module_path)
    compatibility = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(compatibility)
except ImportError:
    import imp

    compatibility = imp.load_source(compatibility_module_name, compatibility_module_path)

ext_modules = []
if compatibility.is_supported():
    ext_modules.append(Extension('_' + NAME, ['%s/_%s.c' % (NAME, NAME)]))

# TODO: is could this all be done using ctypes? (or cffi?)
#  https://solarianprogrammer.com/2019/07/18/python-using-c-cpp-libraries-ctypes/
#  https://stackoverflow.com/a/14123158/
# https://setuptools.pypa.io/en/latest/references/keywords.html
setup(
    name=NAME,
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],

    platforms=['darwin'],
    packages=[NAME],
    ext_modules=ext_modules,

    package_data={'': ['LICENSE']},
    include_package_data=True,

    license=about['__license__'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python'
    ]
)
