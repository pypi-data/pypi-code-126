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
date     : Apr 28, 2022
email    : Nasy <nasyxx+python@gmail.com>
filename : prices.py
project  : Optlib
license  : MIT

Prices
"""
# Standard Library
from operator import sub

# Math
import numpy as np

# Types
from typing import Union

# Local
from .common import NPF64, Float, d1, d2
from scipy.stats import norm


def price_risk_neutral(
    S0: Float,
    K: Float,
    r: Float,
    T: Float,
    u: Float,
    N: int,
    AoE: Union[str, int],
    type: Union[str, int],
) -> tuple[NPF64, NPF64]:
    """Price an option via Cox-Ross-Rubenstein tree.

    Args:
        S0: initial stock price
        K: strike price
        r: interest rate
        T: time to maturity (in years)
        u: up-movement (a constent number of the increasing stock per t)
        N: number of time steps
        AoE: type of the option (european(1) / american(0))
        type: call(1) or put(0)

    Returns:
        price of the stock and option
    """
    d = 1 / u
    dt = T / N
    a = np.exp(r * dt)

    if isinstance(AoE, int):
        AoE = AoE == 1 and "european" or "american"
    if isinstance(type, int):
        type = type == 1 and "call" or "put"

    # 风险中性概率
    # S显示每期的各节点股票价格
    # P显示每期各节点的期权价格
    p = (a - d) / (u - d)
    S = np.triu(
        S0
        * np.power(u, range(0, N + 1))[None].repeat(N + 1, 0)
        * np.power(d, range(0, 2 * N + 1, 2))[None].T
    )
    I = {"call": np.maximum(S - K, 0), "put": np.maximum(K - S, 0)}

    P = np.zeros((N + 1, N + 1))
    PN = I[type][:, -1]
    P[:, -1] = PN

    for j in range(N, 0, -1):
        E = (p * PN + (1 - p) * np.roll(PN, -1)) / a
        PN = {"european": E, "american": np.maximum(E, I[type][:, j])}[AoE]
        P[:, j - 1] = PN

    P = np.triu(P)
    return S, P


def price_dynamic_replication(
    S0: Float,
    K: Float,
    r: Float,
    T: Float,
    u: Float,
    N: int,
    AoE: Union[str, int],
    type: Union[str, int],
) -> tuple[NPF64, NPF64]:
    """
    Args:
        S0: initial stock price
        K: strike price
        r: interest rate
        T: time to maturity (in years)
        u: up-movement (a constent number of the increasing stock per t)
        N: number of time steps
        AoE: type of the option (european(1) / american(0))
        type: call(1) or put(0)

    Returns:
        price of the stock and option
    """
    if isinstance(AoE, int):
        AoE = AoE == 1 and "european" or "american"
    if isinstance(type, int):
        type = type == 1 and "call" or "put"

    d = 1 / u
    dt = T / N
    # S显示每期的各节点股票价格
    # P显示每期各节点的期权价格
    # V显示每期各节点的支付

    S = np.triu(
        S0
        * np.power(u, -sub(*np.mgrid[: N + 1, : N + 1]))
        * np.power(d, range(N + 1))[None].T
    )
    V = {"call": S - K, "put": K - S}
    P = np.zeros((N + 1, N + 1))
    PN = np.maximum(V[type], 0)[:, -1]
    P[:, -1] = PN

    a = np.exp(r * dt) * (u - d)

    dS = np.subtract(S, np.roll(S, -1, axis=0))

    for j in range(N, 0, -1):
        Pf = P[:, j]
        Pb = np.roll(P[:, j], -1)
        ds = dS[:, j]
        dlt = np.divide(Pf - Pb, ds, out=np.zeros_like(Pf), where=ds != 0)
        L = (u * Pb - d * Pf) / a

        P[:, j - 1] = dlt * S[:, j - 1] + L

    P = np.maximum(V[type], P)

    return S, P


def price_bsm(
    S0: Float, K: Float, r: Float, sigma: Float, T: Float, type: Union[str, int]
) -> Float:
    """BSM price."""
    if isinstance(type, int):
        type = type == 1 and "call" or "put"
    d1_v = d1(S0, K, r, sigma, T)
    sym = {"call": 1, "put": -1}[type]

    return sym * S0 * norm.cdf(sym * d1_v, 0, 1) - K * np.exp(-r * T) * norm.cdf(
        sym * d2(d1_v, sigma, T), 0, 1
    )


if __name__ == "__main__":
    S0 = 30
    K = 30
    T = 0.75
    r = 0.025
    sigma = 0.44628710
    u = 1.25
    N = 4
    AoE = 1
    type = 1
    print(price_risk_neutral(S0, K, r, T, u, N, AoE, type)[1][0, 0])
    print(price_dynamic_replication(S0, K, r, T, u, N, AoE, type)[1][0, 0])
    print(price_bsm(S0, K, r, sigma, T, type))
