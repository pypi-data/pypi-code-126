# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
from abc import abstractmethod

import attrs

from ..base import Base


class ComponentBase(Base):
    """A base class for all components.

    This class is used to ensure that all derived classes have a sync method as well as shared methods.
    """

    def _set_unneeded_keys_to_empty_dict(self, component, keys=["createdByUser", "modifiedByUser", "permissions"]):
        """A component object to remove defined keys from.

        Args:
            component (dict or attrs): A Swimlane component object to clean.
            keys (list): A list of keys to set as empty dictionaries.

        Returns:
            dict or attrs: Returns an updated component with the values set as empty dictionaries.
        """
        for key in self.UNNEEDED_KEYS:
            if isinstance(component, dict):
                if component.get(key):
                    component[key] = {}
            elif isinstance(component, attrs):
                if hasattr(component, key):
                    setattr(component, key, {})
        return component

    @abstractmethod
    def sync(self):
        """Every component must have a defined sync method.

        Raises:
            NotImplementedError: Raises when a component does not have a sync method defined.
        """
        raise NotImplementedError("The class does not have a sync method.")
