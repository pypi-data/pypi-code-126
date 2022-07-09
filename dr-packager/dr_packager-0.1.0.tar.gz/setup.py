# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dr_packager']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['dr_package = dr_packager:main']}

setup_kwargs = {
    'name': 'dr-packager',
    'version': '0.1.0',
    'description': 'Automate react shipping with Django with a simple command',
    'long_description': "# Django-React Packager\nReact-Django packager helps you ship a react front end with django as backend.\nThis package automatically builds your react project and places the static and index file in their appropriate place in your django project.\n\n## Installation\nInstall the package using pip:\n```bash\npip install dr_packager\n```\nand thats it!\n## Motivation\nReact is one of the most popular front-end frameworks, and with django being one of the most popular backend choices, there are a lot of websites built with this stack.\nYou can serve django on a different server than the react project and communicate between them using an API, but for smaller projects (or even bigger ones), Having 2 separate server is not justified. Copying react build files to your server is not fun either (which can be simplified with a CI\\CD).\n\nThis project helps you serve react project with django (that can be deployed on a single server). This package was made out of frustration of building react project and manually copying everything to django project.\n## Usage\nTo use the packager, you should have both the react folder & django folder in the same parent folder as follows (Absolute path is still not supported in this version):\n```bash\n├───root_folder\n│   ├───django_project\n│   ├───react_project\n```\nYour django project should contain:\n- An app that serves the `index.html`\n- A static folder (set by STATIC_ROOT variable in your settings)\n> IMPORTANT: Your django project root folder and base app should have the same name\n> for example, settings.py should be located at `example.example.settings.py`\n\nOpen terminal in `root_folder`, and run the following command:\n```bash\ndr_package <react_path> <django_path> <django_front_app_name>\n```\nFollowing the above folder example, consider that we have an app named `front` in our django project:\n```bash\ndr_package react_project django_project front\n```\n> IMPORTANT: Your django settings files should contain STATIC_ROOT variable\n\n### Commands\n```bash\nusage: dr_package [-h] [-S] [--npm] [--yarn] [-D] [-I] [--folders-old [FOLDERS_OLD ...]]\n                  react_path django_path app_name\n\nBuild React Project and Deploy with Django!\n\npositional arguments:\n  react_path            React folder name (RELATIVE PATH)\n  django_path           Django folder name (RELATIVE PATH)\n  app_name              Name of the app that holds index.html\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -S, --skip-build      Skip react build (Use what is alredy in \\build\\)\n  --npm                 use npm as the package manager of the react project\n  --yarn                use yarn as the package manager of the react project\n  -D, --delete-old      Delete old static files\n  -I, --install         Run install command before building (use if you haven't installed the required packages)\n  --folders-old [FOLDERS_OLD ...]\n                        Name of the folders to delete (Doesn't work if --delelete-old is not provided), separated by\n                        space\n````\n\n## Roadmap\n- Support for absolute path\n- Default setting file\n- More customization\n- Creating a separate django package (to run as management commands) to use with git hooks\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n",
    'author': 'moporem',
    'author_email': 'pooriavrj@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
