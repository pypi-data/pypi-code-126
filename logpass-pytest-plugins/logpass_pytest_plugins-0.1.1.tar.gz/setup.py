# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logpass_pytest_plugins', 'logpass_pytest_plugins.contrib']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=6.2.0']

extras_require = \
{'auto_pytest_factoryboy': ['pytest-factoryboy>=2.5.0,<3.0.0'],
 'channels': ['channels>=3.0.0',
              'pytest-asyncio>=0.17.2,<0.19.0',
              'pytest-django>=4.5.2,<5.0.0'],
 'flask': ['flask>=2.1.2,<3.0.0'],
 'rest_framework': ['djangorestframework>=3.13.1,<4.0.0']}

setup_kwargs = {
    'name': 'logpass-pytest-plugins',
    'version': '0.1.1',
    'description': "Pytest's plugins crafted by LogPass",
    'long_description': '# LogPass pytest plugins\n\nA few pytest plugins used by LogPass.\n\n## Installation\n\nTo use `logpass_pytest_plugins` install it with your package manager,\ne.g. via pip:\n\n```bash\npip install logpass_pytest_plugins\n```\n\nTo install plugin with all its dependencies use one of following extras:\n\n+ `auto_pytest_factoryboy`\n+ `channels`\n+ `rest_framework`\n\nFor instance, to install `channels` and `rest_framework` plugins with all\ndependencies:\n\n```bash\npip install logpass_pytest_plugins[channels,rest_framework]\n```\n\nAnd finally add plugin import path to [pytest_plugins][] in your root\n`conftest.py` file, e.g. to use `channels` and `rest_framework` plugins:\n\n```python\n# root `conftest.py`\npytest_plugins = (\n    \'logpass_pytest_plugins.contrib.channels\',\n    \'logpass_pytest_plugins.contrib.rest_framework\',\n)\n```\n\n## Available plugins\n\nNOTE: None plugin is **not** used by default - you need to enable them via\n[pytest_plugins]\n\n### `logpass_pytest_plugins.contrib.auto_pytest_factoryboy`\n\nPlugin that automatically registers `factory_boy` factories to\n`pytest-factoryboy`, so factories and models instances will be available\nas pytest fixtures.\n\n#### Configuration\n\nFollowing INI options can be used to configure `auto_pytest_factoryboy` plugin:\n\n+ `auto_pytest_factoryboy_root_dir` - directory where factories declarations\n  searching starts (defaults to `.` - pytest config path)\n+ `auto_pytest_factoryboy_globs` - list of `glob` patterns used to find files\n  with `factoryboy` factories declarations starting from the\n  `auto_pytest_factoryboy_root_dir` directory (defaults to `**/factories*.py`)\n\n### `logpass_pytest_plugins.contrib.channels`\n\nPlugin that simplifies `channels` consumers testing by providing following\nfixtures:\n\n+ `websocket_commmunicator_factory` - factory of `WebSocketCommunicator`\n  instances, that will automatically disconnect at the end of a test.\n  Using this fixture also automatically flush all used channel layers\n+ `http_commmunicator_factory` - factory of `HttpCommunicator`\n  instances. Using this fixture also automatically flush all used\n  channel layers\n\n### `logpass_pytest_plugins.contrib.flask`\n\nPlugin that simplifies `flask` views and other components testing\nby providing following fixtures:\n\n+ `flask_app` - `Flask` app instance\n+ `client` - `FlaskClient` instance to use in tests\n\nFollowing INI options can be used to configure `flask` plugin:\n\n+ `FLASK_SETTINGS_MODULE` - import path to settings module when using\n  flask\'s config from object. Overrides `FLASK_SETTINGS_MODULE` environment\n  variable.\n+ `FLASK_APP` - import path to flask app factory or flask app instance.\n  Overrides `FLASK_APP` environment variable.\n\nTo use `flask` plugin you need to do one of following:\n\n+ set `FLASK_APP` INI option\n+ set `FLASK_APP` environment variable\n+ define `flask_app` function-scoped fixture in root `conftest.py`\n\n### `logpass_pytest_plugins.contrib.rest_framework`\n\nPlugin that simplifies `rest_framework` views and other components testing\nby providing following fixtures:\n\n+ `api_rf` - `APIRequestFactory` instance\n+ `api_client` - `APIClient` instance\n\n[pytest_plugins]: https://docs.pytest.org/en/7.1.x/how-to/plugins.html#requiring-loading-plugins-in-a-test-module-or-conftest-file "`pytest_plugins`"\n',
    'author': 'Bartosz Barwikowski',
    'author_email': 'bartosz.barwikowski@logpass.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dev.logpass.me',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
