import unittest
from dataclasses import dataclass


from pavouk_ecs.component import Components
from pavouk_ecs.entity import Entity
from pavouk_ecs.setup import MAX_ENTITIES


@dataclass
class CustomComponent:
    var: int = 0


class TestComponents(unittest.TestCase):
    def setUp(self):
        self.components = Components(CustomComponent)
        self.e = Entity(1)

    def test_created_components_is_empty(self):
        self.assertEqual(self.components.get_size(), 0)

    def test_get_component_from_not_assigned_entity(self):
        self.assertIsNone(self.components.get(self.e))

    def test_assign_entity_increases_size(self):
        self.components.assign(self.e)
        self.assertEqual(self.components.get_size(), 1)

    def test_assign_none(self):
        self.assertIsNone(self.components.assign(None))

    def test_remove_none_with_empty_components(self):
        self.components.remove(None)
        self.assertEqual(self.components.get_size(), 0)

    def test_remove_none(self):
        self.components.assign(self.e)
        self.components.remove(None)
        self.assertEqual(self.components.get_size(), 1)

    def test_get_unassigned_entity(self):
        self.assertIsNone(self.components.get(self.e))

    def test_get_assigned_entity(self):
        self.components.assign(self.e)
        self.assertIsNotNone(self.components.get(self.e))

    def test_get_none(self):
        self.assertIsNone(self.components.get(None))

    def test_get_assigned_entity_returns_component(self):
        self.components.assign(self.e)
        self.assertEqual(type(self.components.get(self.e)), CustomComponent)

    def test_remove_entity_decreases_size(self):
        self.components.assign(self.e)
        self.components.remove(self.e)
        self.assertEqual(self.components.get_size(), 0)

    def test_changed_component_remains_changed(self):
        new_value = 1
        self.components.assign(self.e)
        self.components.get(self.e).var = new_value
        self.assertEqual(self.components.get(self.e).var, new_value)

    def test_comp_is_new_when_comp_is_changed_then_removed_and_readded(self):
        self.components.assign(self.e)
        self.components.get(self.e).var = 1
        self.components.remove(self.e)
        self.components.assign(self.e)
        self.assertEqual(self.components.get(self.e).var, 0)

    def test_can_create_until_max_limit(self):
        for i in range(MAX_ENTITIES):
            self.components.assign(Entity(i))
        self.assertEqual(self.components.get_size(), MAX_ENTITIES)

    def test_cant_assign_more_than_max_limit(self):
        for i in range(MAX_ENTITIES + 1):
            self.components.assign(Entity(i))
        self.assertEqual(self.components.get_size(), MAX_ENTITIES)

    def test_cant_create_more_than_max_limit(self):
        for i in range(MAX_ENTITIES):
            self.components.assign(Entity(i))
        self.assertIsNone(self.components.assign(Entity(i)))

    def test_assign_entity_after_reach_max_limit_and_remove_one(self):
        for i in range(MAX_ENTITIES):
            e = Entity(i)
            self.components.assign(e)
        self.components.remove(e)
        e = Entity(i)
        self.assertIsNotNone(self.components.assign(e))
