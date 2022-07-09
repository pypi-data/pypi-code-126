from .dependency_registry import DependencyRegistry
from .registry import Registry

class ControllerRegistry(DependencyRegistry):
    _controllers: list = []

    def add(self, class_):

        key = self.get_key(class_.klass)

        list_dependencies = self.get_dependencies(class_.klass)
        self._controllers.append(Registry(key, list_dependencies, class_))

    def get_controllers(self) -> list:
        return self._controllers
