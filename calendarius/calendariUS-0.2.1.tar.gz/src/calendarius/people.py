import copy
import random

from .calendarius_utils import logger


class People:
    def __init__(self, people):
        self.num_mondays = 0
        self.people = copy.deepcopy(people)
        # check on number of people
        if len(self.people) < 4:
            raise ValueError("ERROR list of people must contain at least 4 persons")

    def get_monday(self):
        """Returns 2 persons for Mondays"""

        # select 2 persons for monday
        self.p1 = self.people[self.num_mondays % len(self.people)]
        self.p2 = self.people[(self.num_mondays + 1) % len(self.people)]

        logger.debug(f"monday selection: {', '.join((self.p1, self.p2))}")

        # copy list of people
        self._work = copy.deepcopy(self.people)

        # remove 2 persons from complete list
        self._work.remove(self.p1)
        self._work.remove(self.p2)

        self.num_mondays += 2

        return self.p1, self.p2

    def get(self):
        """Returns 2 persons from the list excluding people assigned to Monday"""

        p1 = self._select()

        self._remove(p1)

        logger.debug(f"select: {p1}")

        p2 = self._select()

        while p2 == p1:
            p2 = self._select()

        self._remove(p2)

        logger.debug(f"select: {p2}")

        return p1, p2

    def _select(self):
        return random.choice(self._work)

    def _remove(self, p):
        self._work.remove(p)
        # reset list if empty
        if len(self._work) == 0:
            self._reset()

    def _reset(self):
        self._work = copy.deepcopy(self.people)
        self._work.remove(self.p1)
        self._work.remove(self.p2)
