from distutils.core import setup

setup(
    name = "pycalcium",
    packages = ['pycalcium'],
    version = "1.0",
    license = "GPL",
    description = "A Mathematical Equation Parser and Solver",
    author = "EliaZ",
    url = "https://github.com/eliazdev/Calcium",
    download_url = "https://github.com/eliazdev/Calcium/archive/refs/tags/v1.0.0.tar.gz",
    keywords = ['calcium', 'solver'],
    install_requires=[
        'ply'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
)