import sys
import json


def plug(fn):
    [_, *argv] = sys.argv
    args = [json.loads(arg) for arg in argv]

    res = fn(*args)

    return print(json.dumps(res))
