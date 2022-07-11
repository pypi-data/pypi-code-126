# jsontree.py
import json
from .themes import default
from asciitree import LeftAligned
from asciitree.drawing import BoxStyle, BOX_LIGHT
from colr import color
from collections import OrderedDict as OD


class JSONTree(object):
    def __init__(self):
        self.ascii_tree = LeftAligned(draw=BoxStyle(gfx=BOX_LIGHT, horiz_len=2))
        self.root_node_key = '●'
        self.theme = default

    @classmethod
    def _transform(cls, d):
        r = {}
        for k, v in d:
            if type(v) in [dict, list]:
                r.update({k: OD(v)})
        return r

    @classmethod
    def _object_node_signature(cls, node):
        return ''.join(k for k in node.keys())

    def _list_node_signatures(self, _list):
        signatures = []
        for j in _list:
            if type(j) == dict:
                signature = self._object_node_signature(j)
                if signature not in signatures:
                    signatures.append(signature)
        return signatures

    def _colourise(self, s, t):
        return color(s, fore=self.theme[t], style='bright')

    def _elaborate_distinct(self, _list):
        elaborated_schema = {}
        signatures = []
        i = 0
        for j in _list:
            if type(j) == dict:
                signature = self._object_node_signature(j)
                if signature not in signatures:
                    signatures.append(signature)
                    elaborated_schema.update({'◎-schema-{}'.format(i): j})
                    i += 1
        return elaborated_schema

    @classmethod
    def _elaborate_union(cls, _list):
        elaborated_schema = {}
        for d in _list:
            if type(d) == dict:
                for k in d.keys():
                    if k not in elaborated_schema.keys():
                        elaborated_schema.update({k: d[k]})
        return elaborated_schema

    def _format_tree(self, d, mode=None):
        r = {}
        if type(d) == dict:
            for k in d.keys():
                t = type(d[k])
                if d[k] is None:
                    r.update({self._colourise(k, None): {}})
                elif t == str:
                    r.update({'"{}"'.format(self._colourise(k, t)): {}})
                elif t in [bool, float, str, int]:
                    r.update({self._colourise(k, t): {}})
                elif t == dict:
                    r.update({'{{{}}}'.format(self._colourise(k, t)): self._format_tree(d[k], mode=mode)})
                elif t == list:
                    if len(d[k]):
                        signatures = self._list_node_signatures(d[k])
                        if mode == 'first' or len(signatures) == 1:
                            r.update({'[{}]'.format(self._colourise(k, t)): self._format_tree(d[k][0], mode=mode)})
                        elif mode == 'distinct':
                            elaborated_schema = self._elaborate_distinct(d[k])
                            r.update({'[{}]'.format(self._colourise(k, t)): self._format_tree(elaborated_schema, mode=mode)})
                        elif mode == 'union':
                            elaborated_schema = self._elaborate_union(d[k])
                            r.update({'[{}]'.format(self._colourise(k, t)): self._format_tree(elaborated_schema, mode=mode)})
                    else:
                        r.update({'[{}]'.format(self._colourise(k, t)): self._format_tree({}, mode=mode)})
        return r

    def _wrap_root_node_key(self, root_node_type):
        if root_node_type == dict:
            return '{{{}}}'.format(self._colourise(self.root_node_key, root_node_type))
        elif root_node_type == list:
            return '[{}]'.format(self._colourise(self.root_node_key, root_node_type))

    def tree(self, root_node, mode=None):
        root_node_type = type(root_node)
        if root_node_type == list:
            signatures = self._list_node_signatures(root_node)
            if mode == 'first' or len(signatures) == 1:
                elaborated_root_node = root_node[0]
            elif mode == 'distinct':
                elaborated_root_node = self._elaborate_distinct(root_node)
            elif mode == 'union':
                elaborated_root_node = self._elaborate_union(root_node)
        else:
            elaborated_root_node = root_node

        dt = {self._wrap_root_node_key(type(root_node)): json.loads(json.dumps(self._format_tree(elaborated_root_node, mode=mode)), object_pairs_hook=self._transform)}
        return '\n' + self.ascii_tree(OD(dt)) + '\n'
