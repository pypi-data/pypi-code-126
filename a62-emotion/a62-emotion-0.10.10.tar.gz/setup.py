# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emotion',
 'emotion.cli',
 'emotion.data',
 'emotion.data.audio',
 'emotion.features',
 'emotion.features.audio',
 'emotion.models',
 'emotion.train',
 'emotion.train.audio',
 'emotion.visualization']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.1.2,<3.0.0',
 'dvc[gdrive]<2.11',
 'gunicorn>=20.1.0,<21.0.0',
 'keras>=2.8.0,<3.0.0',
 'librosa>=0.9.1,<0.10.0',
 'numpy==1.20.3',
 'pandas==1.2.4',
 'scikit-learn==0.24.2']

entry_points = \
{'console_scripts': ['emotion = emotion.cli:cli']}

setup_kwargs = {
    'name': 'a62-emotion',
    'version': '0.10.10',
    'description': 'A model for emotion classification based on text and audio.',
    'long_description': '# Emotion\n\nA model for emotion classification based on text and audio.\n\n[![emotion - merge](https://github.com/philipGaudreau/emotion/actions/workflows/merge.yml/badge.svg)](https://github.com/philipGaudreau/emotion/actions/workflows/merge.yml)\n[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)\n\n## Acknowledgements\n\n - Hafed Benteftifa\n - Soumaya Chaffar\n\n## Features\n\nGive audio and text as input and get back the dominant emotion.\n\n## Usage/Examples\n\nBe sure to add double quotes to lines containing one or more commas for `.csv` files.\n\nFor graphical interface, use https://a62-emotion.herokuapp.com/index and upload `.wav` and `.csv` files.\n\n```python\nIn [1]: import requests\n\nIn [2]: with open("./data/raw_sample/audio/UlTJmndbGHM.wav", "rb") as fd:\n   ...:     response = requests.post("https://a62-emotion.herokuapp.com/predict", files={\'files[]\': fd})\n   ...:\n\nIn [3]: response.json()\nOut[3]: {\'predictions_audio\': {\'UlTJmndbGHM.wav\': \'positive\'}, \'predictions_texte\': {}}\n```\n\n```bash\ncurl -F \'files[]=@/home/user/emotion/data/raw_sample/audio/DatH-ra0VKY.wav\' -F \'files[]=@/home/user/file.csv\' https://a62-emotion.herokuapp.com/predict\n{"predictions_audio":{"DatH-ra0VKY.wav":"positive"},"predictions_texte":{"file.csv":{"DAMON WILLIAMS: I am the Senior Vice President and Chief Education and Youth Development Officer for the Boys and Girls Clubs of America.":"neutral","In that role, I help to shape the education policy and youth development direction for more than 4,000 clubs that are part of our federated network, having an impact on more than 4 million young people across this nation.":"positive"}}}\n```\n\n## API Reference\n\n#### Get a prediction for file(s)\n\n```http\n  POST /predict\n```\n\n| Parameter | Type     | Description                      |\n| :-------- | :------- | :------------------------------- |\n| `files[]` | `File`   | **Required**. File(s) to process |\n\n## Installation\n\nInstall emotion with pip\n\n```bash\n  pip install a62-emotion\n```\n\n## Environment Variables\n\nTo run this project, you will need to add the following environment variables to your .env file\n\n`GDRIVE_CREDENTIALS_DATA`\n\n`FLASK_SECRET_KEY`\n\n## System Dependencies\n\nFor audio, you will need to install `libsndfile1` (and `libsndfile1-dev` on some systems) \n```bash\nsudo apt-get install libsndfile1\n```\n## Run Locally\n\nBe sure to have python 3.8.13 as the python executable\n```bash\npython3 --version\n```\n\nTo install Poetry, run:\n\n```bash\ncurl -sSL https://install.python-poetry.org | POETRY_VERSION=1.1.14 python3 - --yes\n```\n\n(Optional) To install the Heroku CLI, follow these steps\n\nhttps://devcenter.heroku.com/articles/heroku-cli#standalone-installation-with-a-tarball\n\nClone the project\n\n```bash\ngit clone https://github.com/philipgaudreau/emotion\n```\n\nGo to the project directory\n\n```bash\ncd emotion\n```\n\nInstall dependencies (add flag `--without-dev` if you do not want development dependencies)\n\n```bash\npoetry install\n```\n\nActivate the virtual environment\n\n```bash\npoetry shell\n```\n\nPull cloud data if needed (You will need to export `GDRIVE_CREDENTIALS_DATA`)\n\n```bash\ndvc pull [<.dvc file>]\n```\n\nStart using the command line interface (Not implemented yet)\n\n```bash\nemotion --help\n```\n\n## Running Tests\n\nTo run tests, run the following command (development dependencies must be installed)\n\n```bash\npytest tests\n```\n\n## Deployment\n\nThis project is automatically deployed on Heroku when a PR is merged. To test locally, run (You will need to export `FLASK_SECRET_KEY`)\n\n```bash\nheroku local\n```\n\n## Tech Stack\n\n**CI:** GitHub Actions, DVC\n\n**CD:** GitHub Actions, Heroku\n\n**Frameworks:** Scikit-learn, Tensorflow, Flask\n\n**Versionning:** Poetry, SemVer\n\n**Cloud:** G-Drive, GitHub, Heroku\n\n## Feedback\n\nIf you have any feedback, please reach out to one of us.\n\n\n## Authors\n\n- [@philipgaudreau](https://github.com/philipgaudreau)\n- [@guraymo](https://github.com/guraymo)\n- [@gtrottier](https://github.com/gtrottier)\n\n\n## 🚀 About Us\nWe are on our way to finish a degree in Machine Learning.\n\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n\n',
    'author': 'Philip Gaudreau',
    'author_email': 'this@philipgaudreau.email',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/philipgaudreau/emotion',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '==3.8.13',
}


setup(**setup_kwargs)
