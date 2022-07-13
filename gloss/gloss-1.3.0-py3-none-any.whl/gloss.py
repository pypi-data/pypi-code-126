from itertools import chain
from typing import Dict, Hashable, ItemsView, KeysView, ValuesView


class Gloss(Dict):
    """Gloss[ary] is a symetric 1-1 mapping of terms (keys)

    As such both terms (the key and the value) must be hashable, all
    terms are indexable, and an update any one will affect its mapped
    term as an index.
    Although terms are hashable, they are not necessarily unique
    (although no more than two copies can be present).
    Insertion order is not guaranteed to be preserved in any python version.
    """

    class NoValue:
        pass

    def __init__(self, *args, **kwargs):
        self.data = {}
        self.atad = {}
        for term, pair in dict(*args, **kwargs).items():
            self[term] = pair

    def __setitem__(self, term, pair):
        if not isinstance(pair, Hashable):
            raise TypeError('unhashable type: {}'.format(type(pair)))
        if term in self.atad:
            del self.data[self.atad[term]]
            del self.atad[term]
        if pair in self.data:
            del self.atad[self.data[pair]]
            del self.data[pair]
        if term in self.data:
            del self.atad[self.data[term]]
        if pair in self.atad:
            del self.data[self.atad[pair]]
        self.data[term] = pair
        self.atad[pair] = term

    def __getitem__(self, term):
        if term in self.data:
            return self.data[term]
        return self.atad[term]

    def __delitem__(self, term):
        if term in self.data:
            del self.atad[self.data[term]]
            del self.data[term]
        else:
            del self.data[self.atad[term]]
            del self.atad[term]

    def __contains__(self, term):
        return term in self.data or term in self.atad

    def __iter__(self):
        for term in chain(self.data, self.atad):
            yield term

    def __len__(self):
        return 2 * len(self.data)

    def __or__(self, other):
        if not isinstance(other, dict):
            return NotImplemented
        new = Gloss(self)
        new.update(other)
        return new

    def __ror__(self, other):
        if not isinstance(other, dict):
            return NotImplemented
        new = Gloss(other)
        new.update(self)
        return new

    def __ior__(self, other):
        if not isinstance(other, dict):
            return NotImplemented
        self.update(other)
        return self

    def __repr__(self):
        return 'Gloss({})'.format(repr(self.data))

    def clear(self):
        self.data.clear()
        self.atad.clear()

    def copy(self):
        return Gloss(self)

    def get(self, term, default=None):
        if term in self.data:
            return self.data[term]
        elif term in self.atad:
            return self.atad[term]
        return default

    def items(self):
        return ItemsView(self)

    def keys(self):
        return KeysView(self)

    terms = keys

    def pop(self, term, default=NoValue):
        if term in self.data:
            pair = self.data.pop(term)
            del self.atad[pair]
            return pair
        if default is self.NoValue:
            pair = self.atad.pop(term)
        else:
            pair = self.atad.pop(term, default)
        if pair in self.data:
            del self.data[pair]
        return pair

    def popitem(self):
        term, pair = self.data.popitem()
        del self.atad[pair]
        return term, pair

    def setdefault(self, term, default=None):
        if term in self.data:
            return self.data[term]
        elif term in self.atad:
            return self.atad[term]
        self.__setitem__(term, default)
        return self.data[term]

    def update(self, *args, **kwargs):
        for term, pair in dict(*args, **kwargs).items():
            self[term] = pair

    def values(self):
        return ValuesView(self)
