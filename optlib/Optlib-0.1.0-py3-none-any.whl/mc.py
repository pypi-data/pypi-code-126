import numpy as np
import chaospy as cp
from scipy.stats import norm
from scipy import stats

from .prices import price_bsm as bsm_price

def mc_price(S, K, r, sigma, T, type, nSims=10000):
    '''
    功能：利用标准蒙特卡罗方法计算期权理论价格
    参数：
        S：股票初始价格
        K :期权的执行价格
        r :无风险利率
        sigma:股票价格波动率
        T ：有效期
        type:1表示看涨，0表示看跌
        nSims:模拟的次数，默认为 10,000
    '''
    randnum = np.random.randn(nSims)
    mat = S * np.exp((r-0.5*pow(sigma, 2))*T + sigma*np.sqrt(T)*randnum)
    if type:
        V = np.exp(-r*T) * np.maximum(mat-K, 0)
    else:
        V = np.exp(-r*T) * np.maximum(K-mat, 0)
    price = np.mean(V)
    print("mc: the price of the option is %.4f" % price)
    return price


def mc_antithetic_variable(S, K, r, sigma, T, type, nSims=10000):
    '''
    功能：利用对偶变量法减少方差，标准蒙特卡罗的方差减小技术
    '''
    randnum = np.random.randn(nSims)
    mat1 = S*np.exp((r-0.5*pow(sigma,2))*T + sigma*np.sqrt(T)*randnum)
    mat2 = S*np.exp((r-0.5*pow(sigma,2))*T - sigma*np.sqrt(T)*randnum)
    if type:
        V = np.exp(-r*T) * (np.maximum(mat1-K, 0) + np.maximum(mat2-K, 0)) / 2
    else:
        V = np.exp(-r*T) * (np.maximum(K-mat1, 0) + np.maximum(K-mat2, 0)) / 2
    price = np.mean(V)
    print("antithetic variable: the price of the option is %.4f" % price)
    return price


def mc_low_discrepancy(S, K, r, sigma, T, type, kind, nSims=10000):
    '''
    功能：准蒙特卡罗方法，基于低偏差序列
    参数：
        kind：低偏差序列类型，sobol or halton
    '''
    uniform_cube = cp.J(cp.Uniform(0, 1))
    if kind == "sobol":
        samples = uniform_cube.sample(nSims, rule='sobol')
    elif kind == "halton":
        samples = uniform_cube.sample(nSims, rule='halton')
    else:
        print("kind must be sobol or halton")
        return
    randnum = norm.ppf(samples)
    mat = S * np.exp((r-0.5*pow(sigma, 2))*T + sigma*np.sqrt(T)*randnum)

    if type:
        V = np.exp(-r*T) * np.maximum(mat-K, 0)
    else:
        V = np.exp(-r*T) * np.maximum(K-mat, 0)
    price = np.mean(V)
        samples = uniform_cube.sample(nSims, rule='halton')
    else:
        print("kind must be sobol or halton")
        return
    randnum = norm.ppf(samples)
    mat = S * np.exp((r-0.5*pow(sigma, 2))*T + sigma*np.sqrt(T)*randnum)

    if type:
        V = np.exp(-r*T) * np.maximum(mat-K, 0)
    else:
        V = np.exp(-r*T) * np.maximum(K-mat, 0)
    price = np.mean(V)
    print("low discrepancy %s: the price of the option is %.4f" %(kind, price))
    return price


def mc_least_square(S0, K, r, sigma, T, type, N=50, M=10000):
    '''
    功能：最小二乘蒙特卡罗方法，求解美式期权的价格
    参数：
        N：每条价格路径上的价格点数量，默认为 50
        M：标的资产价格路径条数，默认为 10000
    '''
    dt = T/N
    df = np.exp(-r*dt)
    randnum = np.random.randn(N, M)
    R = np.exp((r-0.5*pow(sigma, 2))*dt + sigma*np.sqrt(dt)*randnum)
    S = np.row_stack((S0*np.ones((1, M)), R)).cumprod(axis=0)

    if type:
        H = np.maximum(S-K, 0)
    else:
        H = np.maximum(K-S, 0)

    CF = np.copy(H)
    for i in range(N-1, 0, -1):
        reg = np.polyfit(S[i], CF[i+1]*df, 7)
        C = np.polyval(reg, S[i])
        CF[i] = np.where(C > H[i], CF[i+1]*df, H[i])

    price = np.mean(CF[1])*df
    print("least square: the price of the option is %.4f" % price)
    return price
