# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['piwik_pro_log_analytics']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['piwik_pro_log_analytics = '
                     'piwik_pro_log_analytics.import_logs:main']}

setup_kwargs = {
    'name': 'piwik-pro-log-analytics',
    'version': '5.0.5',
    'description': "Allows importing common web server log formats (nginx, apache, iss and more) directly to Piwik PRO. It's Free Software available under GPLv3 license, available on GitHub",
    'long_description': '# Piwik PRO Server Log Analytics\n\nImport your web server logs to Piwik PRO.\n\n## Requirements\n\n* Python 3.6+.\n* Piwik PRO >= 16+, all the versions, including Cloud, Core and On-Premises are supported\n\n\n## Getting started\n\n1. Download this git repository `git clone git@github.com:PiwikPRO/log-analytics.git`. The script uses only python standard library, so no external packages are required. Alternatively you can download our PyPi package - `pip install piwik-pro-log-analytics`.\n2. Generate Client ID and Client Secret for communication with Piwik PRO API - docs on how to do this can be found on [developers.piwik.pro](https://developers.piwik.pro/en/latest/data_collection/other_integrations/web_log_analytics.html)\n3. You are now ready to import your web server\'s access logs into Piwik PRO:\n  * `piwik_pro_log_analytics/import_logs.py --client-id <client-id> --client-secret <client-secret> --url=<my-organization>.piwik.pro /path/to/access.log`\n  * If you installed log analytics via `pip`, instead of `piwik_pro_log_analytics/import_logs.py` use `piwik_pro_log_analytics`\n  * If the code fails, saying, that your log format doesn\'t contain hostname - you must decide what App you\'d like to track to. You can find App ID in Piwik PRO UI> Administration> Sites & apps>. After that, use `--idsite <app-id>` flag to tell the importer which App you\'d like to track to.\n![How to find App ID](docs/app-id.png "How to find App ID")\n\n\n## More usage instructions\nMore usage instructions can be found on [developers.piwik.pro](https://developers.piwik.pro/en/latest/data_collection/other_integrations/web_log_analytics.html)\n\n\n## License\n\nLog-analytics is released under the GPLv3 or later.  Please refer to  [LEGALNOTICE](LEGALNOTICE) for copyright and trademark statements and [LICENSE.txt](LICENSE.txt) for the full text of the GPLv3.\n\n',
    'author': 'Piwik PRO',
    'author_email': 'kosto@piwik.pro',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
