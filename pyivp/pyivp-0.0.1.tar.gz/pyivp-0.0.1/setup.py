import os
from setuptools import setup
from setuptools.extension import Extension

this_dir = os.path.dirname(os.path.abspath(__file__))

pyivp = Extension(
    name='pyivp',
    include_dirs=[
        os.path.join(this_dir, 'src/lib_geometry'),
        os.path.join(this_dir, 'src/lib_mbutil')
    ],
    sources=[
        os.path.join(this_dir, 'src/pybind11', 'XYPoint.cpp'),
        os.path.join(this_dir, 'src/pybind11', 'XYSegList.cpp')
    ]
)

setup(
    name='pyivp',
    version='0.0.1',
    author='ARG',
    description='pyivp module',
    long_description='using pybind11 to bind moosivp into python library',
    url='https://github.com/ARG-NCTU/pyivp.git',
    classifiers=[
        # The list of PyPI classifiers
    ],
    ext_modules=[pyivp],
    zip_safe=False,
    include_package_data=True,
)
