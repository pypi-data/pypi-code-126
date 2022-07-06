# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eco2ai', 'eco2ai.tools']

package_data = \
{'': ['*'], 'eco2ai': ['data/*']}

install_requires = \
['APScheduler>=3.8.1,<4.0.0',
 'numpy>=1.22.1,<2.0.0',
 'pandas>=1.3.5,<2.0.0',
 'psutil>=5.9.0,<6.0.0',
 'py-cpuinfo>=8.0.0,<9.0.0',
 'pynvml>=11.4.1,<12.0.0',
 'requests>=2.27.1,<3.0.0',
 'tzlocal>=4.1,<5.0']

setup_kwargs = {
    'name': 'eco2ai',
    'version': '0.2.1',
    'description': 'emission tracking library',
    'long_description': '\n# Eco2AI\n\n+ [About Eco2AI ](#1)\n+ [Installation ](#2)\n+ [Use examples ](#3)\n+ [Important note ](#4)\n+ [Feedback ](#5)\n\n## About Eco2AI  <a name="1"></a> \nThe Eco2AI is a python library for CO<sub>2</sub> emission tracking. It monitors energy consumption of CPU & GPU devices and estimates equivalent carbon emissions taking into account the regional emission coefficient. \nThe Eco2AI is applicable to all python scripts and all you need is to add the couple of strings to your code. All emissions data and information about your devices are recorded in a local file. \n\nEvery single run of Tracker() accompanies by a session description added to the log file, including the following elements:\n                              \n\n+ project_name\n+ experiment_description\n+ start_time\n+ duration(s)\n+ power_consumption(kWTh)\n+ CO<sub>2</sub>_emissions(kg)\n+ CPU_name\n+ GPU_name\n+ OS\n+ country\n\n##  Installation <a name="2"></a> \nTo install the eco2ai library, run the following command:\n\n```\npip install eco2ai\n```\n\n## Use examples <a name="3"></a> \n\nThe eco2ai interface is quite simple. Here is the simplest usage example:\n\n```python\n\nimport eco2ai\n\ntracker = eco2ai.Tracker(project_name="YourProjectName", experiment_description="training the <your model> model")\n\ntracker.start()\n\n<your gpu &(or) cpu calculations>\n\ntracker.stop()\n```\n\nThe eco2ai also supports decorators. As soon as the decorated function is executed, the information about the emissions will be written to the emission.csv file:\n\n```python\nfrom eco2ai import track\n\n@track\ndef train_func(model, dataset, optimizer, epochs):\n    ...\n\ntrain_func(your_model, your_dataset, your_optimizer, your_epochs)\n```\n\nFor your convenience, every time you instantiate the Tracker object with your custom parameters, these settings will be saved until the library is deleted. Eeach new tracker will be created with your custom settings (if you create a tracker with new parameters, they will be saved instead of the old ones). For example:\n\n```python\n\nimport eco2ai\n\ntracker = eco2ai.Tracker(\n    project_name="YourProjectName", \n    experiment_description="training <your model> model",\n    file_name="emission.csv"\n    )\n\ntracker.start()\n<your gpu &(or) cpu calculations>\ntracker.stop()\n\n...\n\n# now, we want to create a new tracker for new calculations\ntracker = eco2ai.Tracker()\n# now, it\'s equivalent to:\n# tracker = eco2ai.Tracker(\n#     project_name="YourProjectName", \n#     experiment_description="training the <your model> model",\n#     file_name="emission.csv"\n# )\ntracker.start()\n<your gpu &(or) cpu calculations>\ntracker.stop()\n\n```\n\nYou can also set parameters using the set_params() function, as in the example below:\n\n```python\nfrom eco2ai import set_params, Tracker\n\nset_params(\n    project_name="My_default_project_name",\n    experiment_description="We trained...",\n    file_name="my_emission_file.csv"\n)\n\ntracker = Tracker()\n# now, it\'s equivelent to:\n# tracker = Tracker(\n#     project_name="My_default_project_name",\n#     experiment_description="We trained...",\n#     file_name="my_emission_file.csv"\n# )\ntracker.start()\n<your code>\ntracker.stop()\n```\n\n\n\n<!-- There is [sber_emission_tracker_guide.ipynb](https://github.com/vladimir-laz/AIRIEmisisonTracker/blob/704ff88468f6ad403d69a63738888e1a3c41f59b/guide/sber_emission_tracker_guide.ipynb)  - useful jupyter notebook with more examples and notes. We highly recommend to check it out beforehand. -->\n## Important note <a name="4"></a> \n\nIf for some reasons it is not possible to define country, then emission coefficient is set to 436.529kg/MWh, which is global average.\n[Global Electricity Review](https://ember-climate.org/insights/research/global-electricity-review-2022/#supporting-material-downloads)\n\nFor proper calculation of gpu and cpu power consumption, you should create a "Tracker" before any gpu or CPU usage.\n\nCreate a new “Tracker” for every new calculation.\n\n\n# Feedback <a name="5"></a> \n\nIf you have any problems working with our tracker, please make comments on [document](https://docs.google.com/spreadsheets/d/1927TwoFaW7R_IFC6-4xKG_sjlPUaYCX9vLqzrOsASB4/edit#gid=0)\n\n# In collaboration with [AIRI](https://airi.net/)\n\n',
    'author': 'AI Lab, Sber',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sb-ai-lab/Eco2AI',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
