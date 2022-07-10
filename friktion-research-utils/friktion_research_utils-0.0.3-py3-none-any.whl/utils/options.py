import matplotlib.pyplot as plt
import numpy as np

from math import log, sqrt, pi, exp
from scipy.stats import norm

from datetime import datetime
from itertools import chain
from matplotlib import cm
import matplotlib.tri as mtri
import pandas as pd
import dill
import plotly.express as px


class Surface:
    def __init__(self, df):
        self.df = df.sort_values("delta")
        self.day = df.datestr.iloc[1]
        self.putCall = df.putCall.iloc[1]
        self.symbol = df.currency.iloc[1]
        self.curves = []
        self.parse_curves()

    def parse_curves(self):
        for dte in self.df.dte.unique():
            temp = self.df.query("dte == @dte")
            desc = f"{self.symbol} {self.putCall} \n Date: {self.day} \n dte: {dte}"
            curve = Curve(temp.markIv.values, temp.delta.values, temp.dte, desc)
            self.curves.append(curve)

    def getIvFromDeltaAndDte(self, delta, dte):
        curves = sorted(self.curves, key=lambda x: x.dte)
        lowestIv = lowestDte = highestIv = highestDte = 0
        for idx in range(len(curves)):
            if dte < curves[idx].dte:
                lowestIv = curves[idx].getIvFromDelta(delta)
                lowestDte = curves[idx].dte
                break
            if dte >= curves[idx].dte:
                highestIv = curves[idx].getIvFromDelta(delta)
                highestDte = curves[idx].dte

        if lowestDte == 0:
            return curves[idx].getIvFromDelta(delta)
        elif highestDte == 0:
            return curves[idx - 1].getIvFromDelta(delta)
        else:
            return lowestIv + (highestIv - lowestIv) * (dte - lowestDte) / (
                highestDte - lowestDte
            )


class Curve:
    def __init__(self, markIvs, deltas, dte, desc):
        # Assumes deltas are sorted
        self.markIvs = markIvs
        self.deltas = deltas
        self.dte = dte.min()
        self.desc = desc
        assert len(markIvs) == len(deltas), "length mismatch"

    def encode_delta(self, delta):
        if delta > 0:
            return 0.5 - delta
        if delta <= 0:
            return -0.5 - delta

    def decode_delta(self, delta):
        if delta > 0:
            return 0.5 - delta
        if delta <= 0:
            return -0.5 - delta

    def details(self):
        print(self.desc if self.desc else "No Description")

    def plot(self):
        # Don't show ITM options
        plt.figure()
        plt.scatter(self.deltas, self.markIvs)
        plt.grid(True)
        plt.title(self.desc)
        plt.xlabel("Delta")
        plt.ylabel("Implied Volatility")

    def getIvFromDelta(self, delta):
        assert 0 < delta <= 0.5
        lowestIv = lowestDelta = highestIv = highestDelta = 0
        for idx in range(len(self.markIvs)):
            if delta < self.deltas[idx]:
                lowestIv = self.markIvs[idx]
                lowestDelta = self.deltas[idx]
                break
            if delta >= self.deltas[idx]:
                highestIv = self.markIvs[idx]
                highestDelta = self.deltas[idx]

        #         print(highestIv, highestDelta, lowestIv, lowestDelta)
        if lowestDelta == 0:
            return self.markIvs[idx]
        elif highestDelta == 0:
            return self.markIvs[idx - 1]
        else:
            #             print(lowestIv + (highestIv-lowestIv)*(delta-lowestDelta)/(highestDelta-lowestDelta))
            return lowestIv + (highestIv - lowestIv) * (delta - lowestDelta) / (
                highestDelta - lowestDelta
            )
