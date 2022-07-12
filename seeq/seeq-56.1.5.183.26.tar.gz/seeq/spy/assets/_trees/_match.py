from __future__ import annotations

import dataclasses
import fnmatch
import functools
import re
from typing import Tuple, List, Union

import numpy as np
import pandas as pd

from seeq.spy import _common
from seeq.spy._errors import *
from seeq.spy.assets._trees import _path


@dataclasses.dataclass(frozen=True)
class TreeNode:
    """
    This is a helper class used to navigate the internal DataFrame of a spy.assets.Tree object in a more traditional
    object-oriented manner. Each object of this type corresponds to a row in said DataFrame.

    Currently this class is only used for resolving formula parameters referenced by path/name in the tree. In the
    future this class may be expanded upon and used for more direct persistence of Tree state.

    NOTE: equality and hashing is determined entirely by the `index` attribute. Do not compare TreeNodes that
    originate from different DataFrames
    """
    id: str = dataclasses.field(init=True, repr=False, compare=False)
    name: str = dataclasses.field(init=True, repr=True, compare=False)
    type: str = dataclasses.field(init=True, repr=False, compare=False)
    children: Tuple[TreeNode] = dataclasses.field(init=True, repr=False, compare=False)
    path: str = dataclasses.field(init=False, repr=True, compare=False)
    index: int = dataclasses.field(init=True, repr=False, compare=True)
    size: int = dataclasses.field(init=True, repr=False, compare=False)
    parent: TreeNode = dataclasses.field(init=False, repr=False, compare=False)
    root: TreeNode = dataclasses.field(init=False, repr=False, compare=False)

    @staticmethod
    def of(df: pd.DataFrame, set_as_root=True) -> TreeNode:
        root = df.iloc[0]
        root_depth = root.Depth
        size: int

        def children_generator():
            i = 1
            while i < len(df) and df.iloc[i].Depth > root_depth:
                child = TreeNode.of(df.iloc[i:], set_as_root=False)
                yield child
                i += child.size
            nonlocal size
            size = i

        children = tuple(children_generator())

        this = TreeNode(id=_common.get(root, 'ID'),
                        name=_common.get(root, 'Name'),
                        type=_common.get(root, 'Type'),
                        index=df.index[0],
                        size=size,
                        children=children)
        for child in children:
            object.__setattr__(child, 'parent', this)  # This bypasses immutability so we can late-initialize fields
        if set_as_root:
            object.__setattr__(this, 'parent', None)
            this._set_path_and_root_rec(path='', root=this)
        return this

    def _set_path_and_root_rec(self, path, root):
        object.__setattr__(self, 'path', path)
        object.__setattr__(self, 'root', root)
        for child in self.children:
            child._set_path_and_root_rec(self.full_path, root)

    @property
    def full_path(self) -> str:
        return f'{self.path} >> {self.name}' if self.path else self.name

    def __iter__(self):
        yield self
        for child in self.children:
            yield from child

    def is_match(self, source_df: pd.DataFrame, pattern) -> bool:
        return is_node_match(pattern, source_df.loc[self.index])

    def is_name_match(self, name: str) -> bool:
        return is_path_match_via_regex_tuple((exact_or_glob_or_regex(name),), (self.name,))

    def resolve_reference(self, reference: str) -> TreeNode:
        reference_name = f'{self.path} >> {reference}'

        def reference_at_node(node: TreeNode, relative_path: str, full_name: str, check_self=False) -> TreeNode:
            _result = None
            for i, match in enumerate(node._relative_matches(relative_path, check_self=check_self)):
                if i == 0:
                    if match.type == 'Asset':
                        raise SPyRuntimeError(f'Formula parameter "{full_name}" is an asset. Formula parameters '
                                              f'must be conditions, scalars, or signals.')
                    _result = match
                else:
                    raise SPyRuntimeError(f'Formula parameter "{full_name}" matches multiple items in tree.')
            return _result

        relative = reference_at_node(self.parent, reference, reference_name, check_self=False)
        if relative is None:
            if reference.startswith(self.root.name):  # Assume that no one will try to wildcard-match the root
                absolute = reference_at_node(self.root, reference, reference, check_self=True)
                if absolute is None:
                    raise SPyRuntimeError(
                        f'Formula parameter is invalid, missing, or has been removed from tree: "{reference}".')
                else:
                    return absolute
            else:
                raise SPyRuntimeError(
                    f'Formula parameter is invalid, missing, or has been removed from tree: "{reference_name}".')
        else:
            return relative

    def resolve_references(self, reference: str) -> List[TreeNode]:
        reference_name = f'{self.path} >> {reference}'

        def references_at_node(node: TreeNode, relative_path: str, full_name: str, check_self=False) -> TreeNode:
            for match in node._relative_matches(relative_path, check_self=check_self):
                if match.type == 'Asset':
                    raise SPyRuntimeError(f'Formula parameter "{full_name}" is an asset. Formula parameters '
                                          f'must be conditions, scalars, or signals.')
                yield match

        relative = list(references_at_node(self.parent, reference, reference_name, check_self=False))
        if len(relative) == 0 and reference.startswith(self.root.name):
            absolute = list(references_at_node(self.root, reference, reference, check_self=True))
            if len(absolute) != 0:
                return absolute
        return relative

    def _relative_matches(self, relative_path: Union[str, List[str]], check_self=False, offset=0):
        components = _common.path_string_to_list(relative_path) if isinstance(relative_path, str) else relative_path
        if offset < len(components):
            if components[offset] == '..':
                if not check_self and self.parent is not None:
                    yield from self.parent._relative_matches(components, check_self=False, offset=offset + 1)
            else:
                if check_self:
                    if self.is_name_match(components[offset]):
                        if offset == len(components) - 1:
                            yield self
                        elif components[offset + 1] == '..':
                            if self.parent is not None:
                                yield from self.parent._relative_matches(components, check_self=False,
                                                                         offset=offset + 2)
                        else:
                            for child in self.children:
                                yield from child._relative_matches(components, check_self=True, offset=offset + 1)
                else:
                    for child in self.children:
                        yield from child._relative_matches(components, check_self=True, offset=offset)


def is_column_value_query(s):
    if not isinstance(s, str):
        return False
    if re.search(r'{{.*}.*}', s):
        return True
    return False


def fill_column_values(row, query: str = None, query_column=None):
    """
    Fills a column values query with actual column values from a row in a dataframe. Returns the output string
    """
    if pd.isnull(query):
        if query_column not in row:
            return np.nan
        query = row[query_column]
        if pd.isnull(query):
            return np.nan

    def _fill_column_value(col_val_query_match: re.Match):
        col_val_query = col_val_query_match[1]
        col, extract_pattern = re.fullmatch(r'{(.*?)}(.*)', col_val_query).groups(default='')
        if not _common.present(row, col):
            raise SPyValueError('Not a match')
        value = str(row[col])
        if extract_pattern == '':
            return value

        # Match against a glob pattern first, then try regex
        for pattern in (glob_with_capture_groups_to_regex(extract_pattern), extract_pattern):
            try:
                extraction = re.fullmatch(pattern, value)
                if extraction:
                    if len(extraction.groups()) != 0:
                        return extraction[1]
                    else:
                        return extraction[0]
            except re.error:
                # There may be a compilation error if the input wasn't intended to be interpreted as regex
                continue
        raise SPyValueError('Not a match')

    try:
        return re.sub(r'{({.*?}.*?)}', _fill_column_value, query)
    except SPyValueError:
        return np.nan


def glob_with_capture_groups_to_regex(glob):
    """
    Converts a glob to a regex, but does not escape parentheses, so that the glob can be written with capture groups
    """
    return re.sub(r'\\([()])', r'\1', fnmatch.translate(glob))


def is_node_match(pattern, node: pd.Series) -> bool:
    """
    General pattern matcher for tree methods that match on tree items. Input options for pattern:

    None
        Matches the root

    np.nan
        Matches nothing. This is used when the user inserts via a 'Parent' column in the children
        dataframe that is only specified for some children.

    int
        Matches all items of the specified depth.

    GUID
        Matches items that have ID or Referenced ID equal to pattern

    Path/Name match
        If just a name is given, matching will be attempted when interpreting the string as
        1) a case-insensitive exact query
        2) a globbing pattern
        3) a regex pattern
        If path markers '>>' are included, the pieces of the path will be split and matched like above
        to find items whose paths end with the path query given.

    list
        Iterates over all elements and calls this same function. If any match is found, return True

    pd.Series
        Checks if this is a DataFrame row containing 'ID' or 'Name' in its index. If so, tries to match
        on ID and then Path/Name. If not, then treated like an iterable in the same way as a list

    pd.DataFrame
        Checks if any of the rows are a match
    """
    if pattern is None:
        return node['Depth'] == 1
    if pd.api.types.is_scalar(pattern) and pd.isnull(pattern):
        # This case handles when the user only gives the 'Parent' column for some children, or gives a parent
        #  string that uses column values that aren't valid for some rows.
        return False
    if isinstance(pattern, pd.DataFrame):
        return pattern.apply(is_node_match, axis=1, node=node).any()
    if isinstance(pattern, list):
        if len(pattern) == 0:
            return False
        else:
            # Pass on to next isinstance() check
            pattern = pd.Series(pattern)
    if isinstance(pattern, pd.Series):
        # First interpret the Series as a dataframe row being matched up against the tree dataframe row
        if _common.present(pattern, 'ID'):
            return pattern['ID'] == _common.get(node, 'ID') or pattern['ID'] == _common.get(node, 'Referenced ID')
        if _common.present(pattern, 'Name'):
            if _common.present(pattern, 'Path') and _path.determine_path(pattern).casefold() != node['Path'].casefold():
                return False
            return pattern['Name'].casefold() == node['Name'].casefold()
        if len(pattern.index.intersection(node.index)) != 0:
            return False

        # Now interpret the Series as a collection of patterns to check against
        return pattern.apply(is_node_match, node=node).any()
    if isinstance(pattern, str):
        if _common.is_guid(pattern):
            if isinstance(node['ID'], str) and pattern.upper() == node['ID'].upper():
                return True
            if isinstance(node['Referenced ID'], str) and pattern.upper() == node['Referenced ID'].upper():
                return True
        else:
            regex_tuple = node_match_string_to_regex_tuple(pattern)
            return is_node_match_via_regex_tuple(regex_tuple, node)
    if isinstance(pattern, int):
        return node['Depth'] == pattern
    return False


def node_match_string_to_regex_tuple(pattern: str) -> Tuple[re.Pattern]:
    """
    :param pattern: String name match (case-insensitive equality, globbing, regex, column values)
                    or string path match (full or partial; case-insensitive equality, globbing, or regex)
    :return: A list of regular expressions that match the last n names in the full path of a node.
    """
    patterns = _common.path_string_to_list(pattern)
    return tuple(exact_or_glob_or_regex(p) for p in patterns)


@functools.lru_cache(maxsize=2048)
def exact_or_glob_or_regex(pat: str) -> re.Pattern:
    try:
        return re.compile('(?i)' + '(' + ')|('.join([re.escape(pat), fnmatch.translate(pat), pat]) + ')')
    except re.error:
        return re.compile('(?i)' + '(' + ')|('.join([re.escape(pat), fnmatch.translate(pat)]) + ')')


def is_node_match_via_regex_tuple(pattern_tuple: Tuple[re.Pattern], node: pd.Series) -> bool:
    path_tuple = tuple(_common.path_string_to_list(_path.get_full_path(node)))
    return is_path_match_via_regex_tuple(pattern_tuple, path_tuple)


@functools.lru_cache(maxsize=2048)
def is_path_match_via_regex_tuple(pattern_tuple: Tuple[re.Pattern], path_tuple: Tuple[str]) -> bool:
    offset = len(path_tuple) - len(pattern_tuple)
    if offset < 0:
        return False
    for i in reversed(range(len(pattern_tuple))):
        if not pattern_tuple[i].fullmatch(path_tuple[offset + i]):
            return False
    return True
