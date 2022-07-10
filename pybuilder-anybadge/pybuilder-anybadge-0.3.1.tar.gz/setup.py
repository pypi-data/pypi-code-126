#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'pybuilder-anybadge',
        version = '0.3.1',
        description = 'A pybuilder plugin that generates badges for your project',
        long_description = "# pybuilder-anybadge\n[![GitHub Workflow Status](https://github.com/soda480/pybuilder-anybadge/workflows/build/badge.svg)](https://github.com/soda480/pybuilder-anybadge/actions)\n[![Code Coverage](https://codecov.io/gh/soda480/pybuilder-anybadge/branch/main/graph/badge.svg)](https://codecov.io/gh/soda480/pybuilder-anybadge)\n[![Code Grade](https://api.codiga.io/project/20103/status/svg)](https://app.codiga.io/public/project/20103/pybuilder-anybadge/dashboard)\n[![PyPI version](https://badge.fury.io/py/pybuilder-anybadge.svg)](https://badge.fury.io/py/pybuilder-anybadge)\n[![python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-teal)](https://www.python.org/downloads/)\n\nA pybuilder plugin that generates badges for your project. The plugin will generate badges using [shields.io](https://shields.io/). However it can also create badges using [anybadge](https://pypi.org/project/anybadge/) if configured to do so.\n\nTo add this plugin into your pybuilder project, add the following line near the top of your build.py:\n```python\nuse_plugin('pypi:pybuilder_anybadge')\n```\n\n**NOTE** if you are using Pybuilder version `v0.11.x`, then specify the following version of the plugin:\n```python\nuse_plugin('pypi:pybuilder_anybadge', '~=0.1.6')\n```\n\n### Pybuilder anybadge properties\n\nThe pybuilder task `pyb anybadge` will use anybadge to generate badges for your project by processing reports produced from various plugins; the badges that are currently supported are:\n- **complexity** - requires the [pybuilder_radon](https://pypi.org/project/pybuilder-radon/) plugin. Generate badge using cyclomatic complexity score of your most complicated function.\n- **vulnerabilities** - requires the [pybuilder_bandit](https://pypi.org/project/pybuilder-bandit/) plugin. Generate badge using number of security vulnerabilities discovered by vulnerabilities.\n- **coverage** - requires the `coverage` plugin. Generate badge for overall unit test coverage.\n- **python** - Generate badge for version of Python being used\n\nThe plugin will write the respective badges to the `docs/images` folder. The following plugin properties are available to further configure badge generation.\n\nName | Type | Default Value | Description\n-- | -- | -- | --\nanybadge_exclude | str | '' | Comma delimited string of badges to exclude from processing, valid values are 'complexity', 'vulnerabilities', 'coverage' and 'python'\nanybadge_complexity_use_average | bool | False | Use overall average complexity as score when generating complexity badge\nanybadge_use_shields | bool | True | Will use `img.shields.io` to create the badges, if False will use `anybadge`\n\n**Note** the plugin will add the badge references but you must commit/push the changes (including svg files in the docs/images folder)\n\nThe plugin properties are set using `project.set_property`, the following is an example of how to set the properties:\n\n```Python\nproject.set_property('anybadge_exclude', 'vulnerabilities,coverage')\nproject.set_property('anybadge_complexity_use_average', True)\nproject.set_property('anybadge_use_shields', True)\n```\n\nBy default the plugin will use `shields.io` to create the badges:\n\n[![coverage](https://img.shields.io/badge/coverage-100.0%25-brightgreen)](https://pybuilder.io/)\n[![complexity](https://img.shields.io/badge/complexity-Stable:%209-olive)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![python](https://img.shields.io/badge/python-3.6-teal)](https://www.python.org/downloads/)\n\nHowever, setting `anybadge_use_shields` to `False` will render the badges using `anybadge` and save them as svg files in the `docs\\images` folder:\n\n![coverage](https://raw.githubusercontent.com/soda480/pybuilder-anybadge/main/docs/images/coverage.svg)\n![complexity](https://raw.githubusercontent.com/soda480/pybuilder-anybadge/main/docs/images/complexity.svg)\n![vulnerabilities](https://raw.githubusercontent.com/soda480/pybuilder-anybadge/main/docs/images/vulnerabilities.svg)\n![python](https://raw.githubusercontent.com/soda480/pybuilder-anybadge/main/docs/images/python.svg)\n\n\n### Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t \\\npybanybadge:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\npybanybadge:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```",
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Other Environment',
            'Environment :: Plugins',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Software Development :: Build Tools'
        ],
        keywords = '',

        author = 'Emilio Reyes',
        author_email = 'soda480@gmail.com',
        maintainer = '',
        maintainer_email = '',

        license = 'Apache License, Version 2.0',

        url = 'https://github.com/soda480/pybuilder-anybadge',
        project_urls = {},

        scripts = [],
        packages = ['pybuilder_anybadge'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = ['anybadge'],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
