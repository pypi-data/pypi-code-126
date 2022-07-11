# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sweep_design',
 'sweep_design.config',
 'sweep_design.dataio',
 'sweep_design.dataio.read',
 'sweep_design.dataio.write',
 'sweep_design.math_signals',
 'sweep_design.math_signals.defaults',
 'sweep_design.math_signals.prepared_sweeps',
 'sweep_design.math_signals.test',
 'sweep_design.math_signals.utility_functions',
 'sweep_design.named_signals',
 'sweep_design.named_signals.defaults',
 'sweep_design.named_signals.header_signals',
 'sweep_design.named_signals.header_signals.defaults',
 'sweep_design.named_signals.header_signals.test',
 'sweep_design.view',
 'sweep_design.view.base_view',
 'sweep_design.view.base_view.abc_common_framer_grapher',
 'sweep_design.view.framemakers',
 'sweep_design.view.framemakers.ipywidgetframer',
 'sweep_design.view.framemakers.ipywidgetframer.defaults',
 'sweep_design.view.framemakers.ipywidgetframer.figwidget',
 'sweep_design.view.view_general',
 'sweep_design.view.view_pilot_rm_bp',
 'sweep_design.view.view_source',
 'sweep_design.view.view_sweep']

package_data = \
{'': ['*']}

install_requires = \
['EMD-signal>=1.2.2,<2.0.0',
 'bokeh>=2.4.2,<3.0.0',
 'ipywidgets>=7.6.5,<8.0.0',
 'jupyter-bokeh>=3.0.4,<4.0.0',
 'jupyterlab>=3.2.9,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.1,<4.0.0',
 'notebook>=6.4.8,<7.0.0',
 'numpy>=1.22.3,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'screeninfo>=0.8,<0.9']

setup_kwargs = {
    'name': 'sweep-design',
    'version': '0.1.0',
    'description': 'The project is designed to create simple and complex sweep signals.',
    'long_description': None,
    'author': 'Vladislav',
    'author_email': 'serebraykov.vs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
