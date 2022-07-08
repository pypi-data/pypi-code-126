# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eventstoredb',
 'eventstoredb.client',
 'eventstoredb.generated',
 'eventstoredb.generated.event_store',
 'eventstoredb.generated.event_store.client',
 'eventstoredb.generated.event_store.client.gossip',
 'eventstoredb.generated.event_store.client.monitoring',
 'eventstoredb.generated.event_store.client.operations',
 'eventstoredb.generated.event_store.client.persistent_subscriptions',
 'eventstoredb.generated.event_store.client.projections',
 'eventstoredb.generated.event_store.client.server_features',
 'eventstoredb.generated.event_store.client.streams',
 'eventstoredb.generated.event_store.client.users',
 'eventstoredb.generated.event_store.cluster',
 'eventstoredb.generated.google',
 'eventstoredb.generated.google.rpc',
 'eventstoredb.persistent_subscriptions',
 'eventstoredb.persistent_subscriptions.common',
 'eventstoredb.persistent_subscriptions.create',
 'eventstoredb.persistent_subscriptions.delete',
 'eventstoredb.persistent_subscriptions.subscribe',
 'eventstoredb.persistent_subscriptions.update',
 'eventstoredb.streams',
 'eventstoredb.streams.append',
 'eventstoredb.streams.read',
 'eventstoredb.streams.subscribe']

package_data = \
{'': ['*']}

install_requires = \
['betterproto==2.0.0-beta4']

setup_kwargs = {
    'name': 'eventstoredb',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'betaboon',
    'author_email': 'betaboon@0x80.ninja',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
