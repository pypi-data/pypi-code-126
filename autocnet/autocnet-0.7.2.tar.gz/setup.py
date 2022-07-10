import os
from setuptools import setup, find_packages

__version__ = '0.7.2'

def setup_package():
    setup(
        name = "autocnet",
        version = __version__,
        author = "Jay Laura",
        author_email = "jlaura@usgs.gov",
        description = "Automated control network generation.",
        long_description = "Automated sparse control network generation to support photogrammetric control of planetary image data.",
        license = "Public Domain",
        keywords = "Multi-image correspondence detection",
        url = "http://packages.python.org/autocnet",
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
          "csmapi",
          "cython",
          "cyvlfeat",
          "matplotlib",
          "dill",
          "gdal",
          "geoalchemy2",
          "geopandas",
          "gdal",
          "hoggorm",
          "imageio",
          "kalasiris",
          "knoten ==0.2.0",
          "ncurses",
          "networkx ==2",
          "numpy",
          "opencv <=3.5",
          "plio >=1.3",
          "pandas",
          "pyyaml",
          "plurmy",
          "psycopg2",
          "pvl ==1.0",
          "pyproj",
          "richdem",
          "scikit-image ==0.17",
          "scikit-learn",
          "scipy ==1.2.1",
          "shapely",
          "sqlalchemy ==1.4",
          "sqlalchemy-utils ==0.37.0",
          "redis-py",
          "usgscsm",
          "vlfeat",
          "pip",
          "protobuf",
        ],
        tests_requires=[
            "coveralls",
            "fakeredis",
            "pytest",
            "pytest-cov",
            "pytest-mock"
        ],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: Public Domain",
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        entry_points={"console_scripts": [
        "acn_submit = autocnet.graph.cluster_submit:main",
        "acn_submit_single = autocnet.graph.cluster_submit_single:main"], 
        }
    )

if __name__ == '__main__':
    setup_package()
