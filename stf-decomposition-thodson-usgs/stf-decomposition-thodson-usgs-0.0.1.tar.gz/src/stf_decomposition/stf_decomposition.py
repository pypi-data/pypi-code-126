import pandas as pd
import numpy as np
from scipy import signal
from scipy.signal import get_window
from statsmodels.tsa.tsatools import freq_to_period
import copy


class stf_decomposition:

    # init method or constructor 
    def __init__(self, data, window, period = None, seasonal = None):
        if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
            self.data = data
        else:
            raise ValueError("data input must be of type pd.DataFrame or pd.Series")
        self.observed = pd.Series(self.data.squeeze(), self.data.index)
        try:
            get_window(window, len(data))
        except(ValueError):
            raise ValueError("Unknown window type: window input must be compatible with scipy.signal.get_window")
        self.window = window
        if period is None:
            freq = None
            if isinstance(data, (pd.Series, pd.DataFrame)):
                freq = getattr(data.index, 'inferred_freq', None)
            if freq is None:
                raise ValueError("Unable to determine period from data")
            period = freq_to_period(freq)
        self.period = period
        self._observed = data
        self.seasonal = seasonal
     
    def fit(self):        
        dt = 1 / (self.period)
        t = np.array(self.data.index)

        f = np.array(self.data.squeeze())
        half = int(np.floor(len(t)/2))
        
        # Reflect half of f on both tails 
        reflected = np.append(np.flip(f[0:half]), f)
        reflected = np.append(reflected, np.flip(f[half:len(f)]))
        
        n = len(reflected) 
        # Compute FFT
        # fhat contains complex fourier coefficients with magnitude and phase components
        # The magnitude tells you how important the term is to the signal
        # The phase tells you if the terms is more cosine or sine
        self.fhat = np.fft.fft(reflected, n)
        self.fhat_seasonal = copy.copy(self.fhat)

        window = get_window(self.window, n)
        
        # X axis of freqs
        self.freq = (1 / (dt*n)) * np.arange(n)

        # Apply window to freqs
        self.freq = self.freq*window

        # Filter freqs for trend (low pass filter from Celevaland 1990) 
        filter_cutoff = 1.5*(1/self.seasonal)*(1/self.period)

        self.fhat[self.freq >= filter_cutoff] = 0
        # Filter freqs for seasonal (high pass filter)
        self.fhat_seasonal[self.freq < filter_cutoff] = 0

        # Inverse FFT for filtered time signal
        ffilt = np.fft.ifft(self.fhat)
        ffilt_seasonal = np.fft.ifft(self.fhat_seasonal)

        # Remove reflected padding
        ffilt = ffilt[half:(len(f)+half)]
        ffilt_seasonal = ffilt_seasonal[half:(len(f)+half)]

        # Create trend series that can be called after fitting
        trend = pd.Series(ffilt.real, self.data.index, name='trend')
    
        # Create season series that can be called after fitting 
        season = pd.Series(ffilt_seasonal.real, self.data.index, name = 'season')
    
        # Find the residuals 
        resid = pd.Series(self.observed - ffilt_seasonal.real - ffilt.real, self.data.index, name = "resid")
        
        import statsmodels.tsa.seasonal 
        return statsmodels.tsa.seasonal.DecomposeResult(self._observed, season, trend, resid)

