import typing as t


def flatten_list(
    mylist: t.List[t.Any],
    levels: t.Optional[int] = None,
) -> t.List[t.Any]:
    """
    Flatten a list. Parameter ``levels`` limits how deep flattening will go.

    >>> flatten_list([1, [2, [3]]])
    [1, 2, 3]
    >>> flatten_list([1, [2, [3]]], levels=1)
    [1, 2, [3]]
    """
    ret: t.List[t.Any] = []
    for item in mylist:
        if isinstance(item, list):
            if levels is None:
                ret.extend(flatten_list(item))
            elif levels > 0:
                ret.extend(flatten_list(item, levels=levels - 1))
            else:
                ret.append(item)
        else:
            ret.append(item)
    return ret


def deduplicate_list(mylist: t.List[t.Any]) -> t.List[t.Any]:
    """
    Deduplicate a list while preserving the order of the items. The first
    occurence of the item is preserved and subsequent duplicates are removed.
    """
    ret: t.List[t.Any] = []
    for item in mylist:
        if item not in ret:
            ret.append(item)
    return ret
