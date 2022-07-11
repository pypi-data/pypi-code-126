# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['volume_segmantics',
 'volume_segmantics.data',
 'volume_segmantics.model',
 'volume_segmantics.model.operations',
 'volume_segmantics.scripts',
 'volume_segmantics.utilities']

package_data = \
{'': ['*']}

install_requires = \
['albumentations<=1.1.0',
 'h5py>=3.0.0,<4.0.0',
 'matplotlib>=3.3.0,<4.0.0',
 'numpy>=1.18.0,<2.0.0',
 'segmentation-models-pytorch>=0.2.1,<0.3.0',
 'termplotlib>=0.3.6,<0.4.0',
 'torch>=1.7.1']

entry_points = \
{'console_scripts': ['model-predict-2d = '
                     'volume_segmantics.scripts.predict_2d_model:main',
                     'model-train-2d = '
                     'volume_segmantics.scripts.train_2d_model:main']}

setup_kwargs = {
    'name': 'volume-segmantics',
    'version': '0.2.1',
    'description': 'A toolkit for semantic segmentation of volumetric data using pyTorch deep learning models',
    'long_description': '# Volume Segmantics\n\nA toolkit for semantic segmentation of volumetric data using PyTorch deep learning models.\n\nGiven a 3d image volume and corresponding dense labels (the segmentation), a 2d model is trained on image slices taken along the x, y, and z axes. The method is optimised for small training datasets, e.g a single $384^3$ pixel dataset. To achieve this, all models use pretrained encoders and image augmentations are used to expand the size of the training dataset.\n\nThis work utilises the abilities afforded by the excellent [segmentation-models-pytorch](https://github.com/qubvel/segmentation_models.pytorch) library. Also the metrics and loss functions used make use of the hard work done by Adrian Wolny in his [pytorch-3dunet](https://github.com/wolny/pytorch-3dunet) repository. \n\n## Installation\n\nAt present, the easiest way to install is to create a new conda enviroment or virtualenv with python (ideally >= version 3.8) and pip, activate the envionment and `pip install volume-segmantics`.\n\n## Configuration and command line use\n\nAfter installation, two new commands will be available from your terminal whilst your environment is activated, `model-train-2d` and `model-predict-2d`.\n\nThese commands require access to some settings stored in YAML files. These need to be located in a directory named `volseg-settings` within the directory where you are running the commands. The settings files can be copied from [here](https://github.com/DiamondLightSource/volume-segmantics/tree/main/settings). \n\nThe file `2d_model_train_settings.yaml` can be edited in order to change training parameters such as number of epochs, loss functions, evaluation metrics and also model and encoder architectures. The file `2d_model_predict_settings.yaml` can be edited to change parameters such as the prediction "quality" e.g "low" quality refers to prediction of the volume segmentation by taking images along a single axis (images in the (x,y) plane). For "medium" and "high" quality, predictions are done along 3 axes and in 12 directions (3 axes, 4 rotations) respectively, before being combined by maximum probability. \n\n### For training a 2d model on a 3d image volume and corresponding labels\nRun the following command. Input files can be in HDF5 or multipage TIFF format.\n\n```shell\nmodel-train-2d --data path/to/image/data.h5 --labels path/to/corresponding/segmentation/labels.h5\n```\n\nPaths to multiple data and label volumes can be added after the `--data` and `--labels` flags respectively. A model will be trained according to the settings defined in `/volseg-settings/2d_model_train_settings.yaml` and saved to your working directory. In addition, a figure showing "ground truth" segmentation vs model segmentation for some images in the validation set will be saved. \n\n##### For 3d volume segmentation prediction using a 2d model\nRun the following command. Input image files can be in HDF5 or multipage TIFF format.\n\n```shell\nmodel-predict-2d path/to/model_file.pytorch path/to/data_for_prediction.h5\n```\n\nThe input data will be segmented using the input model following the settings specified in `volseg-settings/2d_model_predict_settings.yaml`. An HDF5 file containing the segmented volume will be saved to your working directory.\n',
    'author': 'Oliver King',
    'author_email': 'olly.king@diamond.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DiamondLightSource/volume-segmantics',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
