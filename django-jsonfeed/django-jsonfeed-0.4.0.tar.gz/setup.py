# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsonfeed']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-jsonfeed',
    'version': '0.4.0',
    'description': 'JSONFeed syndication in Django.',
    'long_description': "===============\nDjango-JSONFeed\n===============\n\nThis library intends to support `JSON Feed`_ in Django_ and feedgenerator_.\n\n.. image:: design/repository-open-graph-template.png\n    :target: https://django-jsonfeed.mylesbraithwaite.org/\n    :alt: Django JSONFeed\n\nUsage\n-----\n\nIf you are using Django:\n\n.. code-block:: python\n\n    from django.contrib.syndication.views import Feed\n    from jsonfeed import JSONFeed\n\n    class ExampleFeed(Feed):\n        type = JSONFeed\n\nIf you are using this library without Django, you will first need to install the feedgenerator_ Python package:\n\n.. code-block:: python\n\n    from jsonfeed import JSONFeed\n\n    feed = JSONFeed(\n        title='Hello, World!',\n        link='https://example.com/',\n        language='en'\n    )\n\n    feed.add_item(\n        title='One',\n        link='https://example.com/1/',\n        pubdate=datetime(2018, 2, 28, 15, 16)\n    )\n\n    return feed.writeString()\n\nInstallation\n------------\n\n::\n\n    $ pip install django-jsonfeed\n\n.. _JSON Feed: https://jsonfeed.org/\n.. _feedgenerator: https://pypi.python.org/pypi/feedgenerator\n.. _Django: https://djangoproject.com/\n",
    'author': 'Myles Braithwaite',
    'author_email': 'me@mylesbraithwaite.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/myles/django-jsonfeed',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
