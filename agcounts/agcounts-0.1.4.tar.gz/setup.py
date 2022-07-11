# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['agcounts']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.5,<2.0.0', 'pandas>=1.0.5,<2.0.0', 'scipy>=1.7.0,<2.0.0']

setup_kwargs = {
    'name': 'agcounts',
    'version': '0.1.4',
    'description': 'This project contains code to generate activity counts from accelerometer data.',
    'long_description': '# agcounts\n![Tests](https://github.com/actigraph/agcounts/actions/workflows/tests.yml/badge.svg)\n\nA python package for extracting actigraphy counts from accelerometer data. \n\n## Install\n```bash\npip install agcounts\n```\n## Test\nDownload test data:\n```bash\ncurl -L https://github.com/actigraph/agcounts/files/8247896/GT3XPLUS-AccelerationCalibrated-1x8x0.NEO1G75911139.2000-01-06-13-00-00-000-P0000.sensor.csv.gz --output data.csv.gz\n```\n\nRun a simple test\n\n```python\nimport pandas as pd\nimport numpy as np\nfrom agcounts.extract import get_counts\n\ndef get_counts_csv(file, freq: int, epoch: int, fast: bool = True, verbose: bool = False, time_column: str = None):\n  if verbose:\n    print("Reading in CSV", flush = True)\n  raw = pd.read_csv(file, skiprows=0)\n  if time_column is not None:\n    ts = raw[time_column]\n    ts = pd.to_datetime(ts)\n    time_freq = str(epoch) + "S"\n    ts = ts.dt.round(time_freq)\n    ts = ts.unique()\n    ts = pd.DataFrame(ts, columns=[time_column])\n  raw = raw[["X", "Y", "Z"]]\n  if verbose:\n    print("Converting to array", flush = True)  \n  raw = np.array(raw)\n  if verbose:\n    print("Getting Counts", flush = True)    \n  counts = get_counts(raw, freq = freq, epoch = epoch, fast = fast, verbose = verbose)\n  del raw\n  counts = pd.DataFrame(counts, columns = ["Axis1","Axis2","Axis3"])\n  counts["AC"] = (counts["Axis1"]^2 + counts["Axis2"]^2 + counts["Axis3"]^2) ** 0.5\n  ts = ts[0:counts.shape[0]]\n  if time_column is not None:\n    counts = pd.concat([ts, counts], axis=1)\n  return counts\n\ndef convert_counts_csv(file, outfile, freq: int, epoch: int, fast: bool = True, verbose: bool = False, time_column: str = None):\n  counts = get_counts_csv(file, freq = 80, epoch = 60, verbose = True, time_column = time_column)\n  counts.to_csv(outfile,index=False)\n  return counts\n\ncounts = get_counts_csv("data.csv.gz", freq = 80, epoch = 60)\ncounts = convert_counts_csv("data.csv.gz", outfile="counts.csv.gz", \nfreq=80, epoch = 60, verbose = True, time_column = "HEADER_TIMESTAMP")\n```\n',
    'author': 'Actigraph LLC',
    'author_email': 'data.science@theactigraph.com',
    'maintainer': 'Ali Neishabouri',
    'maintainer_email': 'ali.neishabouri@theactigraph.com',
    'url': 'https://github.com/actigraph/agcounts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
