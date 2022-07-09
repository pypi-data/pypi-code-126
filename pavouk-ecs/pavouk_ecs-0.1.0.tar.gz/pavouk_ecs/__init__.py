from pavouk_ecs.component.manager import ComponentManager
from pavouk_ecs.entity.manager import EntityManager


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Manager(metaclass=SingletonMeta):
    def __init__(self):
        self.entity_manager = EntityManager()
        self.component_manager = ComponentManager()
        self.systems = []

    def create_entity(self):
        return self.entity_manager.create()

    def remove_entity(self, e):
        self.entity_manager.remove(e)

    def query(self, Types):
        mask = self.component_manager.get_mask(Types)
        return self.entity_manager.get_entities_with_mask(mask)

    def assign(self, Type, e):
        return self.component_manager.assign(Type, e)

    def remove_assignment(self, Type, e):
        self.component_manager.remove(Type, e)

    def get(self, Type, e):
        return self.component_manager.get(Type, e)

    def add_system(self, System):
        self.systems.append(System(self))

    def update_systems(self, surface, deltatime):
        for system in self.systems:
            system.on_update(surface, deltatime)

    def clear(self):
        self.component_manager.clear()
        self.entity_manager.clear()
        self.systems = []

    def __repr__(self):
        return "{}\n{}".format(self.entity_manager, self.component_manager)
