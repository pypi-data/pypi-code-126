import unittest

from pavouk_ecs.entity import Entity


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.e = Entity(1)

    def test_created_entity_is_alive(self):
        self.assertFalse(self.e.is_dead())

    def test_created_entity_has_no_mask(self):
        self.assertEqual(self.e.mask, 0)

    def test_assert_mask_was_added(self):
        self.e.add_mask(1)
        self.assertEqual(self.e.mask, 1)

    def test_assert_mask_was_removed(self):
        self.e.add_mask(1)
        self.e.remove_mask(1)
        self.assertEqual(self.e.mask, 0)

    def test_add_mask_assert_has_mask(self):
        self.e.add_mask(1)
        self.assertTrue(self.e.has_mask(1))

    def test_assert_has_invalid_mask(self):
        self.assertFalse(self.e.has_mask(1))

    def test_assert_add_many_masks_assert_has_all(self):
        self.e.add_mask(1)
        self.e.add_mask(2)
        self.e.add_mask(4)
        self.assertTrue(self.e.has_mask(1))
        self.assertTrue(self.e.has_mask(2))
        self.assertTrue(self.e.has_mask(4))
