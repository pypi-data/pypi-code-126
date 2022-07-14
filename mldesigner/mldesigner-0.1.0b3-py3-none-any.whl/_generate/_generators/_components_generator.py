# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Dict
from pathlib import Path

from azure.ai.ml.entities import Component

from mldesigner._generate._generators._base_generator import BaseGenerator
from mldesigner._generate._generators._base_component_generator import BaseComponentGenerator


class SingleComponentReferenceGenerator(BaseGenerator, BaseComponentGenerator):
    def __init__(self, component_entity: Component, working_dir: Path, unique_name: str = None):
        super(SingleComponentReferenceGenerator, self).__init__(
            component_entity=component_entity, unique_name=unique_name
        )
        self._working_dir = Path(working_dir).absolute()

    @property
    def tpl_file(self):
        return self.TEMPLATE_PATH / "single_component_reference.template"

    @property
    def ref_params(self):
        component = self._entity
        if component._source_path:
            source_file = Path(component._source_path).absolute().relative_to(Path(self._working_dir)).as_posix()
            return {"yaml_file": source_file}
        else:
            return {"name": component.name, "version": component.version}

    @property
    def entry_template_keys(self) -> list:
        return [
            "ref_params",
            "component_func_name",
            "component_cls_name",
            "description",
            "enums",
            "inputs",
            "outputs",
        ]


class ComponentReferenceGenerator(BaseGenerator):
    def __init__(self, name_to_components: Dict[str, Component], working_dir):
        self._component_entities = name_to_components.values()
        self._ref_generators = [
            SingleComponentReferenceGenerator(component_entity=val, working_dir=working_dir, unique_name=name)
            for name, val in name_to_components.items()
        ]
        entities = [f"{c.component_cls_name}Component" for c in self._ref_generators]
        enums = [e.enum_cls_name for c in self._ref_generators for e in c.enums]
        self._components_impl_imports = sorted(entities + enums)

    @property
    def tpl_file(self):
        return self.TEMPLATE_PATH / "_components.template"

    @property
    def builtin_imports(self):
        return []

    @property
    def third_party_imports(self):
        return [
            "from azure.ai.ml import Input",
            "from mldesigner import reference_component",
        ]

    @property
    def components_impl_imports(self):
        return self._components_impl_imports

    @property
    def component_funcs(self):
        return [g.generate() for g in self._ref_generators]

    @property
    def component_func_names(self):
        return [g.component_func_name for g in self._ref_generators]

    @property
    def entry_template_keys(self) -> list:
        return [
            "builtin_imports",
            "third_party_imports",
            "components_impl_imports",
            "component_funcs",
        ]
