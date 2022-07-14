"""A setuptools based setup module.
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. 
    name="streamn",
    version="1.0.1",
    description="a python library to use Streamn API's ",
    long_description=long_description,  # Optional
    
    long_description_content_type="text/markdown",  # Optional (see note above)
    #url="https://github.com/saireddy12/streamn_sdk",  # Optional
    url="",
    # This should be your name or the name of the organization which owns the
    # project.
    author="B. sai reddy Developer",  # Optional
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email="sai@streamn.com",  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    keywords="streamn , ASR , ASR API, Speech Recognition API , Audio Labs ",  # Optional
    package_dir={"": "src"},  # Optional
    
    #   py_modules=["my_module"],
    
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7",
    # Any package you put here will be installed by pip when your project is installed, so they must be valid existing projects.
    install_requires=["requests>=2.28.1"],  # Optional
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    # extras_require={  # Optional
    #     "dev": ["check-manifest"],
    #     "test": ["coverage"],
    # },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={  # Optional
        "sample": ["package_data.dat"],
    },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[("my_data", ["data/data_file"])],  # Optional
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     "console_scripts": [
    #         "sample=sample:main",
    #     ],
    # },
    # List additional URLs that are relevant to your project as a dict.
    # This field corresponds to the "Project-URL" metadata fields:
    project_urls={  # Optional
        "Bug Reports": "https://github.com/saireddy12/streamn_sdk/issues",
        "Source": "https://github.com/saireddy12/streamn_sdk",
        #"Contact": "contact@streamn.ai"
    },
)