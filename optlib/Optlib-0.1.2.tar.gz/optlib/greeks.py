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
date     : May 11, 2022
email    : Nasy <nasyxx+python@gmail.com>
filename : greeks.py
project  : Optlib
license  : GPL-3.0+

Greeks
"""
import numpy as np
from .common import NPF64, Float, Int, d1, d2
from scipy.stats import norm


def delta(S0: Float, K: Float, r: Float, sigma: Float, T: Float, type: str) -> NPF64:
    """计算delta，股票价格变化对期权价格的影响."""
    if isinstance(type, int):
        type = type == 1 and "call" or "put"

    sym = {"call": 1, "put": -1}[type]

    return sym * norm.cdf(sym * d1(S0, K, r, sigma, T), 0, 1)


def gamma(S0: Float, K: Float, r: Float, sigma: Float, T: Float) -> NPF64:
    """计算gamma，股票价格变化对delta的影响."""
    return np.exp(-d1(S0, K, r, sigma, T) ** 2 / 2) / (
        S0 * np.sqrt(2 * np.pi * T * sigma**2)
    )


def vega(S0: Float, K: Float, r: Float, sigma: Float, T: Float) -> NPF64:
    """计算vega，波动率变化对期权价格的影响."""
    return S0 * np.sqrt(T) * norm.pdf(d1(S0, K, r, sigma, T), 0, 1) / 100


def rho(S0: Float, K: Float, r: Float, sigma: Float, T: Float, type: str) -> NPF64:
    """计算rho，股票价格变化对期权价格的影响."""
    if isinstance(type, int):
        type = type == 1 and "call" or "put"

    sym = {"call": 1, "put": -1}[type]

    d2_v = d2(d1(S0, K, r, sigma, T), sigma, T)
    return (
        sym * K
        * T * np.exp(-r * T)
        * norm.cdf( sym * d2_v, 0, 1
        ) / 100
    )


def theta(S0: Float, K: Float, r: Float, sigma: Float, T: Float, type: str) -> NPF64:
    """计算theta，波动率变化对期权价格的影响."""
    if isinstance(type, int):
        type = type == 1 and "call" or "put"

    d1_v = d1(S0, K, r, sigma, T)
    sym = {"call": 1, "put": -1}[type]

    return -(S0 * norm.pdf(sym * d1_v, 0, 1) * sigma) / (
        2 * np.sqrt(T)
    ) + (- sym) * r * K * np.exp(-r * T) * norm.cdf( sym * d2(d1_v, sigma, T), 0, 1)
