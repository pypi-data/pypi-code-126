# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_panel', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['panel>=0.12', 'plum-dispatch', 'pydantic']

setup_kwargs = {
    'name': 'pydantic-panel',
    'version': '0.1.1',
    'description': 'Top-level package for pydantic-panel.',
    'long_description': "==============\npydantic-panel\n==============\n\n\n.. image:: https://img.shields.io/pypi/v/pydantic_panel.svg\n        :target: https://pypi.python.org/pypi/pydantic_panel\n\n.. image:: https://img.shields.io/travis/jmosbacher/pydantic_panel.svg\n        :target: https://travis-ci.com/jmosbacher/pydantic_panel\n\n.. image:: https://readthedocs.org/projects/pydantic-panel/badge/?version=latest\n        :target: https://pydantic-panel.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\nEdit pydantic models with panel.\n\nThis is just a small little porject i made for my own use, its limited in scope and probably filled with bugs, USE AT YOUR OWN RISK.\nI will continue to add support for more types as I need them but feel free to open issues with requests or better yet PRs with implementations.\n\n\n* Free software: MIT\n* Documentation: https://pydantic-panel.readthedocs.io.\n\n\nBasic Usage\n-----------\n\nIf you import `pydantic_panel`, it will register the widget automatically using the `panel.BasePane.applies` interface.\nAfter importing, calling `panel.panel(model)` will return a `panel.CompositeWidget` whos value is the model.\nWhen you change one of the sub-widget values, the new value is validated/coerced using the corresponding pydantic\nfield and if it passes validation/coercion the new value is set on the model itself.\nBy default this is a one-way sync, if the model field values are changed via code, it does not sync the widgets.\nIf you want biderectional sync, you can pass `bidirectional = True` to the widget constructor, this will patch the model to sync changes to the widgets\nbut this may break without warning if pydantic change the internals of the `__setattr__`\nNested models and `List[BaseModel]` are supported, `Dict[str,BaseModel]` is trivial to also implement so will probably get around to that soon.\n\n\n.. code-block:: python\n\n    import panel as pn\n    import pydantic_panel\n\n    class SomeModel(pydantic.BaseModel):\n        name: str\n        value: float\n\n    # when passing a model class, \n    # all widget values will be None including the composite widget value\n    w = pn.panel(SomeModel)\n    \n    # if you pass a model instance \n    # widget values will be the same as the model instance\n    inst = SomeModel(name='meaning', value=42)\n    w = pn.panel(inst)\n\n    # This will display widgets to e.g. edit the model in a notebook\n    w\n\n    # This will return True\n    inst is w.value\n\n    # This will be None if the widgets have not yet been set to values\n    # if all the required fields have been set, this will be an instance of SomeModel\n    # with the validated attribute values from the widgets\n    w.value\n\n\nThe `pn.panel` method will return a widget which can be used as part of a larger application or as just \na user friendly way to edit your model data in the notebook.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `briggySmalls/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage\n",
    'author': 'Yossi Mosbacher',
    'author_email': 'joe.mosbacher@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jmosbacher/pydantic_panel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
