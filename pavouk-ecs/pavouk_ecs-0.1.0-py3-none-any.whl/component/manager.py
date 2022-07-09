from pavouk_ecs.component import Components
from pavouk_ecs.id_generator import IDGenerator


def sanitize_list(unsanitize_list):
    if unsanitize_list is None or len(unsanitize_list) == 0:
        return []
    unsanitize_list = [i for i in unsanitize_list if i is not None]
    return unsanitize_list


class ComponentManager:
    def __init__(self):
        self.component_type_to_components = {}

    def assign(self, Type, e):
        if Type is None or e is None:
            return
        if Type not in self.component_type_to_components:
            self.component_type_to_components[Type] = Components(Type)
        components = self.component_type_to_components.get(Type)
        return components.assign(e)

    def remove(self, Type, e):
        if Type is None or e is None:
            return
        self.component_type_to_components[Type].remove(e)

    def get(self, Type, e):
        if Type in self.component_type_to_components:
            return self.component_type_to_components[Type].get(e)

    def get_mask(self, Types):
        Types = sanitize_list(Types)
        mask = 0

        for t in Types:
            mask = mask | IDGenerator.getID(t)

        return mask

    def clear(self):
        self.component_type_to_components = {}

    def __repr__(self):
        return str(self.component_type_to_components)
