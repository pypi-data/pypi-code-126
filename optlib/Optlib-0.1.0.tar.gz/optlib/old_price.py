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
import numpy as np
from optlib.common import NPF64
from typing import Union


def price_risk_neutral(
    S0: float,
    K: float,
    r: float,
    T: float,
    u: float,
    N: int,
    AoE: Union[str, int],
    type: Union[str, int],
) -> tuple[NPF64, NPF64]:
    """Price an option via Cox-Ross-Rubenstein tree.

    Args:
        S0: initial stock price
        K: strike price
        r: interest rate
        T: time to maturity
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
    S = np.zeros([N + 1, N + 1])
    P = np.zeros([N + 1, N + 1])

    S[:, N] = S0 * np.power(u, N) * np.power(d, range(0, 2 * N + 1, 2))
    p[:, N] = {"call": np.maximum(S[:, N] - K, 0), "put": np.maximum(K - S[:, N], 0)}[
        type
    ]

    # nodes on the tree
    for j in range(N, 0, -1):
        for i in range(0, j):
            S[i][j - 1] = S0 * np.power(u, j - 1) * np.power(d, 2 * i)
            E = (p * P[i][j] + (1 - p) * P[i + 1][j]) / a

            I = {"call": max(S[i][j - 1] - K, 0), "put": max(K - S[i][j - 1], 0)}[type]

            P[i][j - 1] = {"european": E, "american": max(E, I)}[AoE]
    return S, P


def crr2_price(
    S0: float,
    K: float,
    r: float,
    T: float,
    u: float,
    N: int,
    AoE: Union[str, int],
    type: Union[str, int],
) -> tuple[NPF64, NPF64]:
    """
    Args:
        S0: initial stock price
        K: strike price
        r: interest rate
        T: time to maturity
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
    S = np.zeros([N + 1, N + 1])
    P = np.zeros([N + 1, N + 1])

    # Create final Returns on the tree
    # V显示每期各节点的支付
    for i in range(0, N + 1):
        for j in range(i, N + 1):
            S[i, j] = S0 * pow(u, j - i) * pow(d, i)

    if type == "call":
        V = S - K
        P[:, N] = np.maximum(S[:, N] - K, 0)
    elif type == "put":
        V = K - S
        P[:, N] = np.maximum(K - S[:, N], 0)
    else:
        raise ValueError("type must be 'call' or 'put'")

    if AoE == "european":
        # j控制列，i控制行
        for j in range(N - 1, -1, -1):
            for i in range(0, j + 1):
                delta = (P[i, j + 1] - P[i + 1, j + 1]) / (
                    S[i, j + 1] - S[i + 1, j + 1]
                )
                L = (u * P[i + 1, j + 1] - d * P[i, j + 1]) / np.exp(r * dt) / (u - d)
                P[i, j] = delta * S[i, j] + L
    elif AoE == "american":
        for j in range(N - 1, -1, -1):
            for i in range(0, j + 1):
                delta = (P[i, j + 1] - P[i + 1, j + 1]) / (
                    S[i, j + 1] - S[i + 1, j + 1]
                )
                L = (u * P[i + 1, j + 1] - d * P[i, j + 1]) / np.exp(r * dt) / (u - d)
                P[i, j] = max(V[i, j], delta * S[i, j] + L)
    else:
        raise ValueError("AoE must be 'european' or 'american'")

    return S, P
