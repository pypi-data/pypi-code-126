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
date     : May 17, 2022
email    : Nasy <nasyxx+python@gmail.com>
filename : option.py
project  : Optlib
license  : GPL-3.0+

Option
"""
# Standard Library
from dataclasses import dataclass

# Types
from typing import Annotated

# Local
from .common import NPF64, NPI


@dataclass
class Option:
    """An option."""

    S0: Annotated[float, "股票的期初价格"]
    K: Annotated[float, "期权的执行价格"]
    r: Annotated[float, "无风险利率"]
    T: Annotated[float, "有效期"]
    u: Annotated[float, "股价每次上涨幅度"]
    N: Annotated[int, "判断点个数"]
