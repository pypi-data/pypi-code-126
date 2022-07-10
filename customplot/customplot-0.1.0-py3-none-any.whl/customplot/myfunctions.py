import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def fit(fitFunction, x, y):
    param, cov = sp.optimize.curve_fit(fitFunction, x, y)
    return param

def f_linear(x, a, b):
    return a*x + b

def f_power(x, a, b):
    return a*x**b

def f_exponential(x, a, b):
    return a*np.exp(b*x)

fitFunctions = {'linear'     : f_linear,
                'power'      : f_power,
                'exponential': f_exponential}


def simple_plot(y, x=None, labels=None, lineStyle=None, fitStyle=None, axis=None, color=None, legend=None):
    sns.set_theme(style="darkgrid")
    if x is None:
        x = np.arange(len(y))

    # if fitStyle == None:
    #     df = {'x':x, 'y':y}
    # else:
    if fitStyle is not None:
        fitFunction = fitFunctions[fitStyle]
        param = fit(fitFunction, x, y)
        xfit = np.linspace(1.1*x.min()-.1*x.max(), 1.1*x.max()-.1*x.min(), 200)
        yfit = fitFunction(xfit, *param)
        # df   = {'x':x, 'y':y, 'xfit':xfit, 'yfit':yfit}

    if axis == None:
        fig, ax = plt.subplots(figsize=(8,6))
    else:
        ax = axis

    if color == None:
        color = 'C0'

    if lineStyle == None:
        ax.plot(x, y, color=color, label=legend)
    elif lineStyle != None:
        ax.plot(x, y, lineStyle, color=color, label=legend)

    if fitStyle != None:
        ax.plot(xfit, yfit, color='C1')

    if labels != None:
        ax.set_xlabel(labels[0])
        ax.set_ylabel(labels[1])

    if fitStyle == None:
        if axis == None:
            return fig, ax
        else:
            return None
    else:
        if axis == None:
            return (fig, ax), param
        else:
            return param
