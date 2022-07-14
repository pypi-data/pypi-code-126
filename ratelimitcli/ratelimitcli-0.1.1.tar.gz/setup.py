# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ratelimitcli',
 'ratelimitcli.billing',
 'ratelimitcli.client',
 'ratelimitcli.conf',
 'ratelimitcli.config',
 'ratelimitcli.limits']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'python-jose>=3.3.0,<4.0.0',
 'pytomlpp>=1.0.11,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'thriftpy2>=0.4.14,<0.5.0',
 'typer[all]>=0.5.0,<0.6.0']

entry_points = \
{'console_scripts': ['ratelimitcli = ratelimitcli.main:app']}

setup_kwargs = {
    'name': 'ratelimitcli',
    'version': '0.1.1',
    'description': 'A CLI to manage rate limits.',
    'long_description': '# Adding rate limits to your API\n\nFor more detailed documentation check out [https://docs.ratelimit.xyz](https://docs.ratelimit.xyz).\n\n## Quickstart\n\n1. Install the RateLimit CLI.\n\n```bash\npip install ratelimitcli\n```\n\n2. Configure the RateLimit CLI and follow the interactive prompts. You won\'t have an API key yet so you can just press `[ENTER]` when asked for a value.\n\n```bash\nratelimitcli configure\n```\n\n3. Request an API key. You\'ll be asked to enter credit card information.\n\n```bash\nratelimitcli billing configure\n```\n\n4. Check to see that the config file has been written to `$HOME/.ratelimit/config`\n\n```bash\ncat ~/.ratelimit/config\n```\n\n5. Create your first rate limit.\n\n```bash\nratelimitcli limits upsert --throttling-burst-limit 2 --throttling-rate-limit 0\n```\n\nReturns\n\n```\nOk: API response ({"limit_id": "a9f9f31b-2c0b-321b-b398-f9d36kd30820"}).\n```\n\n6. Test your first rate limit.\n\n```bash\nratelimitcli limits record a9f9f31b-2c0b-321b-b398-f9d36kd30820  # ok\nratelimitcli limits record a9f9f31b-2c0b-321b-b398-f9d36kd30820  # ok\nratelimitcli limits record a9f9f31b-2c0b-321b-b398-f9d36kd30820  # error\n```\n\n7. Test rate limits in an interpreter shell.\n\n```python\n>>> from ratelimitcli.client.client import RatelimitClient\n>>> client = RatelimitClient(client_id="<email>", api_key="<api_key>")\n>>> client.sync_record_request("a9f9f31b-2c0b-321b-b398-f9d36kd30820")\n```\n\n8. Use your rate limit in your code.\n\n```python\nfrom fastapi import FastAPI\nfrom ratelimitcli.client.client import APIRateLimitException, RatelimitClient as ratelimitclient\n\napp = FastAPI()\n\ndef on_error_callback(_: APIRateLimitException):\n    return "Goodbye, World!"\n\n\n@app.get("/")\n@ratelimitclient(\n    id="a9f9f31b-2c0b-321b-b398-f9d36kd30820",\n    callback=on_error_callback,\n)\nasync def hello():\n    return "Hello, World!"\n```\n',
    'author': 'Anwar',
    'author_email': 'anwar@anwarthink.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://docs.ratelimit.xyz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
