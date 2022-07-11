# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioelpris', 'aioelpris.core']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'aioelpris',
    'version': '0.2.0',
    'description': 'An aio library to retrieve some Nordic countries current electricity price.',
    'long_description': '# aioelpris\n\nAn aio library to retrieve current electricity price in (some parts) of the Nordics. Current supported regions are:\n\n- `DK1`: Denmark/west of the Great Belt\n- `DK2`: Denmark/east of the Great Belt\n- `NO2`: Norway/Kristiansand\n- `SE3`: Sweden/Stockholm\n- `SE4`: Sweden/Malmö\n\nPrices are returned in DKK and EUR currencies.\n\n## Basic example\n\n```python\n\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom aioelpris import ElPris\nfrom aioelpris.core.models import Price\n\n\nasync def example() -> Price:\n    async with ClientSession() as session:\n        pris = ElPris(session=session, price_area="SE3")\n        price: Price = await pris.get_current_price()\n        print(price.SpotPriceDKK)\n        return price\n\n\nasyncio.run(example())\n\n\n\n```\n\n## Data sources\n\n[Energi Data Service](https://www.energidataservice.dk/tso-electricity/Elspotprices).\n',
    'author': 'Alejandro González Pérez',
    'author_email': '8874974+dansmachina@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dansmachina/aioelpris',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
