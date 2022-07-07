# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['orats', 'orats.api', 'orats.model']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'pydantic>=1.9.1,<1.10.0']

setup_kwargs = {
    'name': 'orats',
    'version': '0.1.1a0',
    'description': 'Client SDK for the ORATS API.',
    'long_description': '# ORATS Python SDK\n\n> **BEWARE** This project is **unstable** and in early stages of development!\n\nThis project is a wrapper around [ORATS](https://orats.com/) APIs.\n\n![Docs](../../actions/workflows/build-docs.yml/badge.svg)\n![Tests](../../actions/workflows/run-tests.yml/badge.svg)\n\n> **NOTE**: ORATS offers numerous subscription services.\nDepending on your personal subscriptions, you will be issued an API key with\nappropriate permissions. Some functionality in this SDK may not be accessible\nif you are not subscribed to the necessary services.\n\n## Project Structure\n\n### Development Tooling\n\n- Source Control Management: [Git](https://git-scm.com/) + [GitHub](https://github.com/)\n- Documentation: [Sphinx](https://www.sphinx-doc.org/) + [GitHub Pages](https://pages.github.com/)\n- CI/CD: [GitHub Actions](https://github.com/features/actions)\n- Code Style: [Black](https://pypi.org/project/black/)\n- Type Checker: [mypy](http://mypy-lang.org/)\n- Test Runner: [tox](https://tox.wiki/) + [pytest](https://docs.pytest.org/)\n',
    'author': 'Lucas Lofaro',
    'author_email': 'lucasmlofaro@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lucasmlofaro/orats-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
