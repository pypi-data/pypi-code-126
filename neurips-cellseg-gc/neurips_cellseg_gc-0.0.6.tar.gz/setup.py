# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neurips_cellseg_gc', 'neurips_cellseg_gc.data', 'neurips_cellseg_gc.work_dir']

package_data = \
{'': ['*'],
 'neurips_cellseg_gc.data': ['Train_Labeled/images/*',
                             'Train_Labeled/labels/*',
                             'Train_Pre_3class/images/*',
                             'Train_Pre_3class/labels/*'],
 'neurips_cellseg_gc.work_dir': ['swinunetr_3class/*']}

install_requires = \
['einops==0.3.2',
 'gdown==4.2.0',
 'monai==0.9',
 'nibabel==3.2.1',
 'numpy==1.21.2',
 'pandas==1.4.1',
 'pillow==9.0.1',
 'psutil==5.8.0',
 'scikit-image==0.19.2',
 'tensorboard==2.8.0',
 'torchvision==0.11.2',
 'tqdm==4.63.0']

entry_points = \
{'console_scripts': ['model_training_3class = '
                     'neurips_cellseg_gc.model_training_3class:main',
                     'pre_process_3class = '
                     'neurips_cellseg_gc.data.pre_process_3class:main',
                     'predict = neurips_cellseg_gc.predict:main']}

setup_kwargs = {
    'name': 'neurips-cellseg-gc',
    'version': '0.0.6',
    'description': '',
    'long_description': None,
    'author': 'Cheng Ge',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
}


setup(**setup_kwargs)
