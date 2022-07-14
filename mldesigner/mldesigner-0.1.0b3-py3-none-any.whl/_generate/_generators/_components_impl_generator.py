# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Dict

from azure.ai.ml.entities import Component

from mldesigner._generate._generators._base_generator import BaseGenerator
from mldesigner._generate._generators._base_component_generator import BaseComponentGenerator


class SingleComponentEntityGenerator(BaseGenerator, BaseComponentGenerator):
    def __init__(self, component_entity, unique_name: str = None):
        super(SingleComponentEntityGenerator, self).__init__(component_entity=component_entity, unique_name=unique_name)

    @property
    def tpl_file(self):
        return self.TEMPLATE_PATH / "single_component_entity.template"

    @property
    def entry_template_keys(self) -> list:
        return ["component_cls_name", "component_type_cls", "inputs", "outputs", "enums"]


class ComponentImplGenerator(BaseGenerator):
    def __init__(self, name_to_components: Dict[str, Component]):
        self._component_entities = name_to_components.values()
        self._component_ids = [f"{c.name}:{c.version}" for c in self._component_entities]
        self._component_entity_generators = [
            SingleComponentEntityGenerator(component_entity=val, unique_name=key)
            for key, val in name_to_components.items()
        ]

    @property
    def tpl_file(self):
        return self.TEMPLATE_PATH / "_components_impl.template"

    @property
    def builtin_imports(self):
        return ["from enum import Enum"]

    @property
    def third_party_imports(self):
        return ["from azure.ai.ml import Input, Output", "from azure.ai.ml.entities._builders import Command, Parallel"]

    @property
    def component_ids(self):
        return self._component_ids

    @property
    def component_defs(self):
        return [g.generate() for g in self._component_entity_generators]

    @property
    def entry_template_keys(self) -> list:
        return [
            "builtin_imports",
            "third_party_imports",
            "component_ids",
            "component_defs",
        ]
