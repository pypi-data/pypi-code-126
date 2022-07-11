# std
from __future__ import annotations
import os
from typing import List

# external
import yaml
from yaml.loader import SafeLoader

# internal
from laz.model.base import BaseObject
from laz.model.target import Target
from laz.utils.prodict import prodictify
from laz.utils.types import Data


class Configuration(BaseObject):

    def __init__(self, id: str, root: bool = False, **data: Data):
        super().__init__(id)
        if root:
            self.push(DEFAULT_CONFIGURATION_DATA)
        self.push({'config': {
            'name': self.name, 'filepath': self.filepath, 'dirpath': self.dirpath, 'root': root,
        }})
        self.push(data)

    @property
    def filepath(self):
        return self.id

    @property
    def dirpath(self):
        return os.path.dirname(self.filepath)

    @property
    def name(self):
        return os.path.basename(self.dirpath)

    @property
    def target_names(self) -> List[str]:
        return list(self.data.get('targets', {}).keys())

    def get_target(self, name: str) -> Target:
        return Target(name, **self.data.get('targets', {}).get(name, {}) or {})

    @classmethod
    def deserialize(cls, id: str, serialized: str, **kwargs: Data) -> Configuration:
        data = prodictify(yaml.load(serialized, Loader=SafeLoader) or {})
        return cls(id, kwargs.pop('root', False), **data)

    @classmethod
    def load(cls, filepath: str, root: bool = False) -> Configuration:
        with open(filepath, 'r') as fh:
            return Configuration.deserialize(filepath, fh.read(), root=root)


DEFAULT_CONFIGURATION_DATA = {
    'plugins': [],
    'laz': {
        'default_action': 'default',
        'default_target': 'default',
        'error_on_no_targets': False,
    },
    'env': {},
    'targets': {},
    'actions': {},
}
