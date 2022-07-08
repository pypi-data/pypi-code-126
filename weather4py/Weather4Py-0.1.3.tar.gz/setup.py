# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['weather4py']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'weather4py',
    'version': '0.1.3',
    'description': 'a library for your weathery needs.',
    'long_description': '# Weather4Py\na weather library for python to get the weather of a location or set of coordinates, with the ability to save to a json.\n\n[Github repository for Weather4Py](https://github.com/MintTeaNeko/Weather4Py)\n\n# Here\'s some examples to how to use the library.\n```py\nfrom WeatherPy import WeatherMan\n\n# to get the region of a location\nprint(WeatherMan("38.8,37.7").region)\n\n# to get the weather of a location\nprint(WeatherMan("israel").weather)\n\n# to get the temperature of a location\nprint(WeatherMan("texas").temperature)\n\n# to get the humidity of a location\nprint(WeatherMan("newyork").humidity)\n\n# to reobtain infromation about a location.\nWeatherMan("owo").obtain_information()\n\n# to save the results to a folder in json format\nWeatherMan("38.8,37.7").save_to_file("output.json")\n```\n',
    'author': 'MintTeaNeko',
    'author_email': 'neonwinternight1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
