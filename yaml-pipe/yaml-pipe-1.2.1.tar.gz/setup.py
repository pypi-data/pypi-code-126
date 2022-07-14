# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['yaml_pipe']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'omegaconf>=2.2.2,<3.0.0']

entry_points = \
{'console_scripts': ['yaml-pipe = yaml_pipe.cli:main']}

setup_kwargs = {
    'name': 'yaml-pipe',
    'version': '1.2.1',
    'description': 'Parse yaml',
    'long_description': '# yaml-pipe\n\n<p align="center">\n  <a href="https://pypi.org/project/yaml-pipe/">\n    <img\n      alt="PyPI Python Versions"\n      src="https://img.shields.io/pypi/pyversions/yaml-pipe"\n    />\n  </a>\n  <a href="https://pypi.org/project/yaml-pipe/">\n    <img\n      alt="PyPI"\n      src="https://img.shields.io/pypi/v/yaml-pipe"\n    />\n  </a>\n  <a href="https://pepy.tech/project/yaml-pipe">\n    <img\n      alt="Download"\n      src="https://static.pepy.tech/personalized-badge/yaml-pipe?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads"\n    />\n  </a>\n  <a href="https://github.com/psf/black">\n    <img\n      alt="Issues"\n      src="https://img.shields.io/badge/code%20style-black-000000.svg"\n    />\n  </a>\n  <a href="https://github.com/pollenjp/yaml-pipe/actions/workflows/release.yml">\n    <img\n      alt="Release Drafter"\n      src="https://github.com/pollenjp/yaml-pipe/actions/workflows/release.yml/badge.svg"\n    />\n  </a>\n</p>\n\n## Install\n\n```sh\npip install yaml-pipe\n```\n\n## How to use\n\n- `--dotindex`: extract only now.\n- `--dotlist`: edit only now.\n\n### Extract Example 1\n\n```yaml\n---\naaa:\n  bbb: bbb\n```\n\n```sh\ncat sample.yml | yaml-pipe --dotindex "aaa.bbb"\n```\n\noutput\n\n```log\nbbb\n```\n\n### Extract Example 2\n\n```yaml\n---\naaa:\n  bbb: bbb\n---\nxxx:\n  yyy: yyy\n```\n\n```sh\ncat sample.yml | yaml-pipe --block_id 1 --dotindex "xxx.yyy"\n```\n\noutput\n\n```log\nyyy\n```\n\n### Extract Example 3\n\n```yaml\n---\nxxx:\n  yyy:\n    zzz: zzz\n```\n\n```sh\ncat sample.yml | yaml-pipe --block_id 1 --dotindex "xxx"\n```\n\noutput\n\n```yaml\nyyy:\n  zzz: zzz\n\n```\n\n### Edit Example 1\n\n`sample.yml`\n\n```yml\n---\nfoo:\n  bar: BAR\n```\n\n```sh\ncat sample.yml | yaml-pipe --dotlist foo.bar="bar"\n```\n\noutput\n\n```yaml\n---\nfoo:\n  bar: bar\n```\n\n### Edit Example 2\n\n`sample.yml`\n\n```yaml\n---\nfoo:\n  bar: BAR\n---\nfizz:\n  buzz: BUZZ\n```\n\n```sh\ncat sample.yml | yaml-pipe --block_id 1 --dotlist fizz.buzz="buzz"\n```\n\noutput\n\n```yaml\n---\nfoo:\n  bar: BAR\n---\nfizz:\n  buzz: buzz\n```\n\n### example3\n\n`sample.yml`\n\n```yaml\n---\nfoo:\n  bar: BAR\n---\nfizz:\n  buzz: BUZZ\n````\n\n`update.yml`\n\n```yml\nfizz:\n  buzz: buzz\n```\n\n```sh\ncat sample.yml | yaml-pipe --block_id 1 --dotlist update.yml\n```\n\noutput\n\n```yaml\n---\nfoo:\n  bar: BAR\n---\nfizz:\n  buzz: buzz\n```\n\n## Developers\n\n### Linting and test\n\n```sh\npyenv local 3.10.4 3.9.13 3.8.13\n```\n\n```sh\npoetry install\npoetry run nox\n./test_cli.sh\n```\n\n### Upload to PyPI\n\nDefault target is testpypi.\n\n```sh\nmake pypi-upload\n```\n\nIf you upload to pypi, set empty to `TEST_PYPI`.\n\n```sh\nmake pypi-upload TEST_PYPI=\n```\n',
    'author': 'pollenjp',
    'author_email': 'polleninjp@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pollenjp/yaml-pipe',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
