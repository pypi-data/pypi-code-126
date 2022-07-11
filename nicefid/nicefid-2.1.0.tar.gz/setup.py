# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nicefid']

package_data = \
{'': ['*']}

install_requires = \
['resize-right>=0.0.2,<0.0.3']

setup_kwargs = {
    'name': 'nicefid',
    'version': '2.1.0',
    'description': 'Minimalistic FID and KID implementation. Reference checked against cleanfid',
    'long_description': "# nicefid\n\nMinimalistic FID and KID implementation. Reference checked against [cleanfid](https://github.com/GaParmar/clean-fid).\nCode is a mix between [crowsonkb's implementation](https://github.com/crowsonkb/k-diffusion/blob/master/k_diffusion/evaluation.py)\nand [cleanfid](https://github.com/GaParmar/clean-fid).\n\n> [On Aliased Resizing and Surprising Subtleties in GAN Evaluation](https://arxiv.org/abs/2104.11222)\n\n## Install\n\n```bash\npoetry add nicefid\n```\n\nOr, for the old timers:\n\n```bash\npip install nicefid\n```\n\n## API\n\n```python\nnicefid.Features.from_directory(path: Union[str, Path])\nnicefid.Features.from_iterator(iterator: Iterator[torch.Tensor])  # NCHW\nnicefid.Features.from_path(path: Union[str, Path])\nfeatures.save(path: Union[str, Path])\n\nnicefid.compute_fid(features_a, features_b)\nnicefid.compute_kid(features_a, features_b)\n```\n\n## Usage\n\nComparing directory with generated images.\n\n```python\nimport nicefid\n\nfeatures_generated = nicefid.Features.from_iterator(...)\nfeatures_real = nicefid.Features.from_directory(...)\n\nfid = nicefid.compute_fid(features_generated, features_real)\nkid = nicefid.compute_kid(features_generated, features_real)\n```\n",
    'author': 'Richard Löwenström',
    'author_email': 'samedii@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/samedii/nicefid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
