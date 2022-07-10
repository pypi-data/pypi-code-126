# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libemtk',
 'libemtk.clusters',
 'libemtk.controller',
 'libemtk.lists',
 'libemtk.lists.traits',
 'libemtk.lists.traits.clusters',
 'libemtk.parser',
 'libemtk.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'libemtk',
    'version': '0.1.2',
    'description': 'Extended Modifiers Tool Kit (library)',
    'long_description': "[![Python package](https://github.com/0djentd/libemtk/actions/workflows/python-package.yml/badge.svg)](https://github.com/0djentd/libemtk/actions/workflows/python-package.yml)\n\nlibEMTK, Extended Modifiers Tool Kit (library).\n=======================================\n\nThis thing provides new level of abstraction for _Blender_ modifiers stack.\n\nLibrary name is not final and probably will be changed on release.\n\n_libemtk_ is designed to be used with [_EMTK_](https://github.com/0djentd/emtk).\n\nMost classes and methods have docstrings.\n\nThere are some simple unittests for basic operations.\n\n# Installation\nLinux:\nSymlink `~/.config/blender/3.1/scripts/modules/libemtk` to `libemtk`\n\nWindows:\nidk\n\nMac:\nidk\n\n# Main concepts\n_Actual_ _modifier_ is an actual Blender modifier.\n\n_Modifier_ is a cluster or actual Blender modifier.\n\n_Cluster_ is an object that consists of any number\nof modifiers or clusters.\nAny subclass of _ClusterTrait_ is a _Cluster_. \n\n_ModifiersCluster_ is a cluster that only has\nactual Blender modifiers in it.\n\n_ClustersLayer_ is a cluster that only has\nother clusters in it. This doesnt mean\nthat it cant contain ModifiersClusters\nwith actual modifiers.\n\n_ExtendedModifiersList_ is an object representing\nclusters stack. It is similar to ClustersLayer,\nbut doesnt have ClusterTrait attributes.\nIt require all modifiers in it to be on the same Blender object.\n\n_SortingRule_ is an object that represents set of\nrules that can be used to sort clusters in ExtendedModifiersList.\n\n_ModifiersOperator_ is a mix-in class for Operator class.\nIt has methods for manipulating multiple\nExtendedModifiersList instances.\n\n_ClustersCommand_ is implementation of command pattern for\nsome of frequently used operations.\n\nIt consists of _ClustersAction_, basic elements that have minimal information\nabout side effects of command.\nExamble:\nClustersAction('MOVE', 'Bevel.123', {'direction': 'UP'})\nThis action does not included information about position of 'Bevel.123' and\nother detail required to interpret action as a part of command.\n\nClusterCommands use _ClustersCommandsSolver_ to ask clusters for additional commands.\nExample:\n(using previous example)\nClustersLayer will add ClustersAction('MOVE', 'Bevel.321', {'direction': 'DOWN'}),\nif 'Bevel.321' will change its index after moving 'Bevel.123'.\nThen ClustersCommandsSolver will ask 'Bevel.321' if it should do something else\nafter moving it.\n\n# Currently supported features # \nAll basic editing, like moving, applying, removing,\nduplication and switching visibility of clusters.\n\nSerialization and deserialization of clusters state.\nFull or partial resoring of clusters state.\n\nSerialization and deserialization of clusters types definitions.\n\nClusters Commands and Actions.\n\n# TODO # \nBuffering for ExtendedModifiersList controller.\n\nPanel type subclass for panels that use\nExtendedModifiersList.\n\nOperators for ExtendedModifiersList controller.\n\nMore clusters operation types.\n",
    'author': '0djentd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/0djentd/libemtk',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
