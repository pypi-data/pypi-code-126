import unittest
from dataclasses import dataclass


from pavouk_ecs.component.manager import ComponentManager
from pavouk_ecs.entity import Entity


@dataclass
class CustomComponent:
    var: int = 0


class TestComponentManager(unittest.TestCase):
    def setUp(self):
        self.manager = ComponentManager()
        self.e = Entity(1)

    def test_assing_none_type_return_none(self):
        self.assertIsNone(self.manager.assign(None, self.e))

    def test_assing_none_entity_return_none(self):
        self.assertIsNone(self.manager.assign(CustomComponent, None))

    def test_get_none_type_with_empty_manager(self):
        self.assertIsNone(self.manager.get(None, self.e))

    def test_get_none_entity_with_empty_manager(self):
        self.assertIsNone(self.manager.get(CustomComponent, None))

    def test_get_not_assigned(self):
        self.assertIsNone(self.manager.get(CustomComponent, self.e))

    def test_remove_none_type_with_empty_manager(self):
        self.manager.remove(None, self.e)

    def test_remove_none_entity_with_empty_manager(self):
        self.manager.remove(CustomComponent, None)

    def test_get_mask_none_types_with_empty_manager(self):
        self.assertFalse(self.manager.get_mask(None))

    def test_get_mask_empty_types_with_empty_manager(self):
        self.assertFalse(self.manager.get_mask([]))

    def test_get_mask_none_list_types_with_empty_manager(self):
        self.assertFalse(self.manager.get_mask([None]))

    def test_assign(self):
        components = self.manager.assign(CustomComponent, self.e)
        self.assertEqual(type(components), CustomComponent)

    def test_remove(self):
        self.manager.assign(CustomComponent, self.e)
        self.manager.remove(CustomComponent, self.e)
        self.assertIsNone(self.manager.get(CustomComponent, self.e))

    def test_get_assigned(self):
        self.manager.assign(CustomComponent, self.e)
        components = self.manager.get(CustomComponent, self.e)
        self.assertEqual(type(components), CustomComponent)

    def test_clear_with_assigned(self):
        self.manager.assign(CustomComponent, self.e)
        self.manager.clear()
        self.assertIsNone(self.manager.get(CustomComponent, self.e))
