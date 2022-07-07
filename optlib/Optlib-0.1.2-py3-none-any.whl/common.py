#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
Python ♡ Nasy.

    |             *         *
    |                  .                .
    |           .                              登
    |     *                      ,
    |                   .                      至
    |
    |                               *          恖
    |          |\___/|
    |          )    -(             .           聖 ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : May  2, 2022
email    : Nasy <nasyxx+python@gmail.com>
filename : common.py
project  : Optlib
license  : GPL-3.0+

Commons
"""

# Math
import numpy as np
import numpy.typing as npt

# Types
from typing import Union

NPF64 = npt.NDArray[np.float64]
NPI = npt.NDArray[np.int64]

Float = Union[NPF64, float]
Int = Union[NPI, int]

def d1(S0: Float, K: Float, r: Float, sigma: Float, T: Float) -> NPF64:
    """计算 d1."""
    return (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))


def d2(d1: Float, sigma: Float, T: Float) -> NPF64:
    return d1 - sigma * np.sqrt(T)
