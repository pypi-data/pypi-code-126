from setuptools import setup

name = "types-jmespath"
description = "Typing stubs for jmespath"
long_description = '''
## Typing stubs for jmespath

This is a PEP 561 type stub package for the `jmespath` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `jmespath`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/jmespath. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `abea36c06960a515609f0b889ae5c630a39fd961`.
'''.lstrip()

setup(name=name,
      version="1.0.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/jmespath.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['jmespath-stubs'],
      package_data={'jmespath-stubs': ['__init__.pyi', 'ast.pyi', 'exceptions.pyi', 'functions.pyi', 'lexer.pyi', 'parser.pyi', 'visitor.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
