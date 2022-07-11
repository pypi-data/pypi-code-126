# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_requesting_os_analyzer', 'django_requesting_os_analyzer.migrations']

package_data = \
{'': ['*'],
 'django_requesting_os_analyzer': ['templates/*',
                                   'templates/admin/*',
                                   'templates/admin/django_requesting_os_analyzer/*',
                                   'templates/admin/django_requesting_os_analyzer/stat/*']}

install_requires = \
['Django>3.2']

setup_kwargs = {
    'name': 'django-requesting-os-analyzer',
    'version': '0.1.3',
    'description': 'Counts the number of the requests coming from various os.',
    'long_description': "to install run the command\n```\n    pip install django_requesting_os_analyzer\n```\nadd to your installed apps\n```\n    INSTALLED_APPS = [\n        ...,\n        django_requesting_os_analyzer.apps.DjangoRequestingOsAnalyzerConfig,\n    ]\n```\nadd middleware\n```\n    MIDDLEWARE = [\n        ...,\n        django_requesting_os_analyzer.middleware.CounterMiddleware,\n    ]\n```\nand then to allow the graph to show up you have to tweak your templates settings,\nmake sure 'APP_DIRS' is set to True.\n```\nTEMPLATES = [\n    {\n        ...,\n        'DIRS': ['templates'],\n        'APP_DIRS': True,\n    },\n]\n```\nyou can also change the color of the graph's bar and their border by defing following\n```\nREQUEST_ANALYZER_BG_COLOR = (255,255,255,0.2)\nREQUEST_ANALYZER_CHART_COLOR = (255,0,0,0.2)\n```",
    'author': 'hassan-shahzad',
    'author_email': 'hassanshahzadthegeek@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
