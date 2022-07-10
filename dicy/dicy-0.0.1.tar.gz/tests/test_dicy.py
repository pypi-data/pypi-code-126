#!/usr/bin/env python

"""Tests for `dicy` package."""

import pytest

from dicy import dicy as d


class TestDicyObject(object):

    @pytest.fixture
    def dice_object(self, tmpdir):
        x = d.Dicy()
        yield x

    """Good group"""

    def test_init_dice_object_will_init_a_list_of_six_objects(self, dice_object):
        assert len(dice_object) == 6

    def test_can_iterate_on_the_dice_faces(self, dice_object):
        x = 1
        for d in dice_object:
            assert (d.face == x)
            x += 1
