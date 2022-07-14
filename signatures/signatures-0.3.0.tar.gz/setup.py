# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['signatures']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'signatures',
    'version': '0.3.0',
    'description': 'Utilities for inspecting and comparing Python function signatures.',
    'long_description': '<!--\n Copyright (c) 2022 Joseph Hale\n \n This Source Code Form is subject to the terms of the Mozilla Public\n License, v. 2.0. If a copy of the MPL was not distributed with this\n file, You can obtain one at http://mozilla.org/MPL/2.0/.\n-->\n\n# Signatures\n\nUtitilties for assessing Python function signature equality and compatibility,\nwith the latter accounting for subtypes (including Generics!)\n\n## Examples\nSee the [test suite](/tests/test_signatures.py) for a full set of examples.\n\n### Equality\n```python\n# Identical function signatures are equal.\nimport signatures\n\ndef foo(thing: Any) -> None:\n    pass\n\ndef bar(thing: Any) -> None:\n    pass\n\nassert signatures.equal(foo, bar)\n```\n```python\n# Different function signatures are not equal.\nimport signatures\n\ndef foo(eggs: Any) -> None:\n    pass\n\ndef bar(cheese: Any) -> None:\n    pass\n\nassert not signatures.equal(foo, bar)\n```\n\n### Compatibility\n```python\n# A function signature is compatible with a more\n# generic function signature.\nfrom typing import TypeVar\n\nimport signatures\n\nT = TypeVar("T", bound=int)\n\ndef foo(thing: bool) -> None:\n    pass\n\ndef bar(thing: T) -> None:\n    pass\n\nassert signatures.compatible(foo, bar)\n```\n```python\n# Compatibility checks support nested Generic types.\nimport signatures\n\ndef foo(thing: List[Tuple[bool, str]]) -> None:\n    pass\n\ndef bar(thing: List[Tuple[int, str]]) -> None:\n    pass\n\nassert signatures.compatible(foo, bar)\n```\n```python\n# A function signature is not compatible when\n# Generic types are not compatible.\nimport signatures\n\ndef foo(thing: List[int]) -> None:\n    pass\n\ndef bar(thing: List[Tuple[int, str]]) -> None:\n    pass\n\nassert not signatures.compatible(foo, bar)\n```\n\n## [License](/LICENSE)\nMozilla Public License v2.0',
    'author': 'Joseph Hale',
    'author_email': 'me@jhale.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thehale/signatures',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
