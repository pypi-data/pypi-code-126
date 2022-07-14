import numpy


def unscramble_roi_collection(data, keys):
    """Sort the dictinary of numpy arrays on the keys"""
    if not keys:
        return data
    lst = [data[key] for key in keys]
    idx = list(range(len(lst[0])))
    *_, idx = zip(*sorted(zip(*lst, idx)))
    idx = list(idx)
    return {k: numpy.asarray(v)[idx] for k, v in data.items()}
