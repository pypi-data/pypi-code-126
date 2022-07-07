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
date     : Jun  6, 2022
email    : Nasy <nasyxx+python@gmail.com>
filename : impvol.py
project  : Optlib
license  : GPL-3.0+

BSM impvol
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from prices import price_bsm as bsm_price

def bsm_vega(S0, K, r, sigma, T):
    '''
    功能：计算vega
    '''
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / sigma*np.sqrt(T)
    vega = np.exp(-r*T) * stats.norm.pdf(d1, 0, 1) * np.sqrt(T)
    return vega


def imp_vol_newton(P, S0, K, r, sigma_est, T, type):
    '''
    功能：利用牛顿-拉弗森方法计算期权的隐含波动率
    参数：
        P：期权的实际价格
        S0:股票的期初价格
        K :期权的执行价格
        r :无风险利率
        sigma_est:估计的波动率，作为迭代初始值
        T ：有效期
        type:1表示看涨，0表示看跌
    '''
    minimum = 1e-5
    while True:
        sigma = sigma_est
        sigma_est -= (bsm_price(S0, K, r, sigma_est, T, type)-P) \
                     / bsm_vega(S0, K, r, sigma_est, T)
        if abs(sigma-sigma_est) < minimum:
            break
    return sigma_est


## 二分法
def bsm_imp_dichotomy(P, S0, K, r, T, type):
    '''
    功能：利用二分法计算期权的隐含波动率
    '''
    volUpper = 3
    volLower = 0
    minimum = 1e-8
    volMid = (volLower + volUpper) / 2
    while volUpper - volLower > minimum:
        volMid = (volLower+volUpper) / 2
        if abs(bsm_price(S0, K, r, volMid, T, type) - P) <= minimum:
            break
        elif (bsm_price(S0, K, r, volLower, T, type) - P) \
                * (bsm_price(S0, K, r, volMid, T, type) - P) < 0:
            volUpper = volMid
        else:
            volLower = volMid
    imp_vol = volMid
    return imp_vol


def plot_imp_vol(P, K, S0, r, T, type):
    '''
    功能：基于二分法绘制波动率微笑图形
    参数：
        P：期权的实际价格，数据类型为list
        K :期权的执行价格，数据类型为list
        S0:股票的期初价格
        r :无风险利率
        T ：有效期
        type:1表示看涨，0表示看跌
    '''
    imp_vol = [bsm_imp_dichotomy(p, S0, k, r, T, type) for (p, k) in zip(P, K)]
    # imp_vol = []
    # for i in range(len(P)):
    #     imp_vol_temp = bsm_imp_dichotomy(P[i], S0, K[i], r, T, type)
    #     imp_vol.append(imp_vol_temp)
    plt.figure()
    plt.ylim(0, 2.5)
    plt.title("Volality Smile of Apple")
    plt.xlabel("Strike Price")
    plt.ylabel("Implied Volality")
    plt.scatter(K, imp_vol, s=3)
    plt.show()
