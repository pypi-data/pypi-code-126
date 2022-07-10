#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import print_function
import os
import errno


# equivalent of mkdir -p
def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python ≥ 2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        # possibly handle other errno cases here, otherwise finally:
        else:
            raise