# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resin_release_tool']

package_data = \
{'': ['*']}

install_requires = \
['balena-sdk>=11.2.0,<12.0.0', 'click>=8.0.0,<9.0.0']

entry_points = \
{'console_scripts': ['resin-release-tool = resin_release_tool.cli:cli']}

setup_kwargs = {
    'name': 'resin-release-tool',
    'version': '0.3.0',
    'description': 'Release tool to have canary in resin.io',
    'long_description': '# resin-release-tool\nThis tool is to set releases to release groups and canaries in balenaCloud\n\n## Installation\n```\npip install resin-release-tool\n```\n\n## Build / Run locally\nYou need poetry to build the project https://python-poetry.org/\n```\npoetry install\npoetry build\npoetry run resin-release-tool\netc..\n```\n\n## Example usage\n\n### One canary group\n\nMark relevant devices with device tags with name "release_group" and value "canary" on balenaCloud.\n\n**To deploy a canary commit to them, run:**\n\n```bash\nresin-release-tool --app $APP_ID release -c $CANARY_COMMIT -g canary\n```\n\n**To deploy said commit to rest of devices, run:**\n\n```bash\nresin-release-tool --app $APP_ID release -c $NEW_RELEASE_COMMIT -a\nresin-release-tool --app $APP_ID unpin canary\n```\n\n(Note: Running the unpin command is not necessary if canary is already on `NEW_RELEASE_COMMIT`, however, without it, it won\'t track the latest app-wide release.)\n\n### Staggered release with multiple groups\n\nMark relevant devices with device tags with name "release_group" and value "release_group_1/2/3" on balenaCloud.\n\n**To deploy a commit to all devices in a staggered way:**\n\n(Add appropriate wait or checks between commands as appropriate for your usecase.)\n\n```bash\nresin-release-tool --app $APP_ID release -c $NEW_RELEASE_COMMIT -g release_group_1\nresin-release-tool --app $APP_ID release -c $NEW_RELEASE_COMMIT -g release_group_2\nresin-release-tool --app $APP_ID release -c $NEW_RELEASE_COMMIT -g release_group_3\n\nresin-release-tool --app $APP_ID release -c $NEW_RELEASE_COMMIT -a\nresin-release-tool --app $APP_ID unpin release_group_1 release_group_2 release_group_3\n```\n\n## Usage\n```\nUsage: resin-release-tool [OPTIONS] COMMAND [ARGS]...\n\n  You can set app and token as environment variables, using RESIN_APP and\n  RESIN_TOKEN\n\nOptions:\n  --token TOKEN  balenaCloud auth token  [required]\n  --app APP_ID   balenaCloud app ID  [required]\n  --help         Show this message and exit.\n\nCommands:\n  disable_rolling      Disables rolling releases in the application\n  enable_rolling       Enables rolling releases in the application\n  info                 Information of the application\n  release              Sets release commits for a given release or app\n  releases             Show successful releases of the application\n  show_devices_status  Show the status of the devices in the app\n  show_group_versions  Show the release versions of the devices in release groups\n  unpin                Unpins the version of one or more releases\n```\n\n# Development\n\n* The config file used by the balena_sdk is located at `$HOME/.balena/balena.cfg` \n\nTo format the code run:  \n\n    black <path to files >\n\n\nTests can be run with \n\n    poetry run pytests\n\n\nTo debug/run commands in pycharm configure `resin_release_tool/cli.py` as the script path and the command you want to  run as parameter (credentials can be added as envs)\n\n## Publishing a new version\n### Pre-release steps\n\n* upddate the changelog and run\n    ```bash\n    make release <version>  # e.g. v0.3.1\n    ```\n    to update the version in `pyproject.toml`\n\n### Release step\n* After merging these changes, tag the commit on master using `git tag <version>`. This must match the new version in the `pyprojct.toml`\n* push the new tag to Github `git push origin <version>` this should trigger the `publish-to-pypi` workflow\n\nNew versions are uploaded to https://pypi.org/project/resin-release-tool/',
    'author': 'roger',
    'author_email': 'roger.duran@mobilityhouse.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mobilityhouse/resin-release-tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
