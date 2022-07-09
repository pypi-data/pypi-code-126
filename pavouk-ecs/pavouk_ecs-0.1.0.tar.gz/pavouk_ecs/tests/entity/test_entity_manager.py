import unittest

from pavouk_ecs.entity.manager import EntityManager


class TestEntityManager(unittest.TestCase):
    def setUp(self):
        self.manager = EntityManager()
        self.available_ids_size = len(self.manager.availables_ids)

    def test_entities_are_empty(self):
        self.assertEqual(self.manager.entities, [])

    def test_create_entity_decrease_available_ids(self):
        self.manager.create()
        self.assertEqual(
            len(self.manager.availables_ids), self.available_ids_size - 1)

    def test_create_all_available_entities(self):
        for i in range(self.available_ids_size):
            self.manager.create()
        self.assertEqual(len(self.manager.availables_ids), 0)

    def test_create_too_many_entities_fails(self):
        for i in range(self.available_ids_size):
            self.manager.create()
        self.assertIsNone(self.manager.create())

    def test_remove_entity_increase_available_ids(self):
        e = self.manager.create()
        self.manager.remove(e)
        self.assertEqual(
            len(self.manager.availables_ids), self.available_ids_size)

    def test_remove_all_entities(self):
        for i in range(self.available_ids_size):
            self.manager.create()
        self.manager.remove_all()
        self.assertEqual(
            len(self.manager.availables_ids), self.available_ids_size)

    def test_get_entities_with_mask(self):
        for i in range(self.available_ids_size):
            self.manager.create()
        self.assertEqual(len(self.manager.get_entities_with_mask(1)), 0)

    def test_add_mask_to_entities_assert_get_entities_with_mask(self):
        for i in range(self.available_ids_size):
            e = self.manager.create()
            e.add_mask(1)
        self.assertEqual(
            len(self.manager.get_entities_with_mask(1)),
            self.available_ids_size)
