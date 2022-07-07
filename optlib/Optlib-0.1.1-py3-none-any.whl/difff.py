import numpy as np
from math import floor, ceil

def explicit_diff(S, K, r, sigma, T, AoE, type, N=200, M=20):
    """
    功能：有限差分方法（显性）计算期权价格，先构造边界，之后向前延申
    参数：
        S :股票的期初价格
        K :期权的执行价格
        r :无风险利率
        sigma:股票价格波动率
        T ：有效期
        AoE：A表示美式期权，E表示欧式期权
        type:1表示看涨，0表示看跌
        N:时间步骤数
        M:价格步骤数
    """
    smax = 200
    ds = smax / M
    dt = T / N
    diffmat = np.zeros((M+1, N+1))
    ss = np.arange(0, smax+ds, ds)

    # 填充边界
    if type:
        diffmat[:, N] = np.maximum(ss - K, 0)
    else:
        diffmat[:, N] = np.maximum(K - ss, 0)
    diffmat[0, :] = diffmat[0, N]
    diffmat[M, :] = diffmat[M, N]

    # 计算a,b,c
    a = np.fromfunction(lambda x, y: (-0.5*r*(x+1)*dt + 0.5*pow(sigma, 2)*pow(x+1, 2)*dt) \
                                     / (1+r*dt), (M-1, 1))
    b = np.fromfunction(lambda x, y: (1 - pow(sigma, 2)*pow(x+1, 2)*dt) \
                                     / (1+r*dt), (M-1, 1))
    c = np.fromfunction(lambda x, y: (0.5*r*(x+1)*dt + 0.5*pow(sigma, 2)*pow(x+1, 2)*dt) \
                                     / (1+r*dt), (M-1, 1))
    if type:
        payvec = -K + ss[1:M-1]
    else:
        payvec = K - ss[1:M-1]

    # 填补中间元素
    for j in range(N-1, -1, -1):
        for i in range(0, M-1):
            if AoE == "E":
                diffmat[i+1, j] = a[i]*diffmat[i, j+1] + b[i]*diffmat[i+1, j+1] \
                                  + c[i]*diffmat[i+2, j+1]
            elif AoE == "A":
                diffmat[i+1, j] = max(payvec[i], a[i]*diffmat[i, j+1] + \
                                      b[i]*diffmat[i+1, j+1] + c[i]*diffmat[i+2, j+1])
            else:
                print("AoE must be A or E")
                return
    price = diffmat[np.where(ss==S), 0]
    print("explicit diff %s：the price of the option is %.4f" %(AoE, price))
    return price


def implict_diff(S, K, r, sigma, T, type, N=200, M=20):
    """
    功能：有限差分方法（隐性）
    参数：
        N:时间步骤数
        M:价格步骤数
    """
    smin = 0
    smax = 200
    ds = (smax-smin) / M
    dt = T / N
    diffmat = np.zeros((M+1, N+1))
    ss = np.arange(smin, smax+ds, ds)

    # 填充边界
    if type:
        diffmat[:, N] = np.maximum(ss - K, 0)
    else:
        diffmat[:, N] = np.maximum(K - ss, 0)
    diffmat[0, :] = diffmat[0, N]
    diffmat[M, :] = diffmat[M, N]

    # 计算a,b,c，并构造MI
    a = np.fromfunction(lambda x,y: 0.5*r*(x+1)*dt - 0.5*pow(sigma*(x+1), 2)*dt, (M-1, 1))
    b = np.fromfunction(lambda x,y: 1 + pow(sigma*(x+1), 2)*dt + r*dt, (M-1, 1))
    ds = (smax-smin) / M
    dt = T / N
    diffmat = np.zeros((M+1, N+1))
    ss = np.arange(smin, smax+ds, ds)

    # 填充边界
    if type:
        diffmat[:, N] = np.maximum(ss - K, 0)
    else:
        diffmat[:, N] = np.maximum(K - ss, 0)
    diffmat[0, :] = diffmat[0, N]
    diffmat[M, :] = diffmat[M, N]

    # 计算a,b,c，并构造MI
    a = np.fromfunction(lambda x,y: 0.5*r*(x+1)*dt - 0.5*pow(sigma*(x+1), 2)*dt, (M-1, 1))
    b = np.fromfunction(lambda x,y: 1 + pow(sigma*(x+1), 2)*dt + r*dt, (M-1, 1))
    c = np.fromfunction(lambda x,y: -0.5*r*(x+1)*dt - 0.5*pow(sigma*(x+1), 2)*dt, (M-1, 1))

    MI = np.zeros((M-1, M-1))
    for i in range(M-1):
        k = i
        if i == 0:
            MI[i, i] = b[k]
            MI[i, i+1] = c[k]
        elif i == M-2:
            MI[i, i-1] = a[k]
            MI[i, i] = b[k]
        else:
            MI[i, i-1] = a[k]
            MI[i, i] = b[k]
            MI[i, i+1] = c[k]

    # 进行求解
    invMI = np.linalg.inv(MI)
    adjustmat = np.zeros(M-1)
    for j in range(N-1, -1, -1):
        adjustmat[0] = a[0] * diffmat[0, j]
        adjustmat[M-2] = c[M-2] * diffmat[M, j]
        diffmat[1:M, j] = np.dot(invMI, diffmat[1:M, j+1]-adjustmat)

    # 寻找目标价格
    DS = S - smin
    indexdown = floor(DS/ds)
    indexup = ceil(DS/ds)
    if indexdown == indexup:
        price = diffmat[indexdown, 0]
    else:
        price = diffmat[indexdown, 0] + (S-ss[indexdown])/(ss[indexup]-ss[indexdown]) \
                *(diffmat[indexup, 0] - diffmat[indexdown, 0])

    print("implict diff：the price of the option is %.4f" % price)
    return price
