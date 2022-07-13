try:
    from setuptools import setup
except:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = "ecmind_protlib_transition",
    version = "1.5.0",
    py_modules = ["protlib"],
    cmdclass = {'build_py': build_py},
    
    author = "Eli Courtwright",
    author_email = "eli@courtwright.org",
    description = "library for implementing binary network protocols",
    license = "BSD",
    url = "https://github.com/rolandkoller/protlib",
    # use_2to3=True,
    test_suite="unit_tests",
    long_description = """
Fork with removed 2to3 setup flag.

protlib makes it easy to implement binary network protocols. It uses
the struct and SocketServer modules from the standard library. It
provides support for default and constant struct fields, nested structs, 
arrays of structs, better handling for strings and arrays, struct 
inheritance, and convenient syntax for instantiating and using your 
custom structs.

protlib requires Python 3.
""",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking"
    ]
)
