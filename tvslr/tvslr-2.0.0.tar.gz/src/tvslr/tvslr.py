"""
    Implementation of time-varying SLR using OLS estimates
    Link to paper: https://www.researchgate.net/publication/348422809_TIME_VARYING_ESTIMATION_OF_REGRESSION_MODEL_USING_OLS_ESTIMATES
    Author: Arka
"""

import numpy as np
import pandas as pd

class TVSLR:
    def __init__(self, X, y, subsetSize, intercept=True):
        """
            Inputs:
                X: a numpy array containing the feature vectors
                y: a numpy array containing target variables
        """

        if type(X) == pd.DataFrame:
            X = X.to_numpy()
        if type(y) == pd.DataFrame:
            y = y.to_numpy()

        if intercept:
            # add column of 1's to design matrix (for intercept parameter)
            X = np.c_[np.ones(self.N), X]

        self.N, self.k = X.shape
        self.subsetSize = subsetSize     # size of each subset
        self.X = X
        self.y = y
        
        if self.N < self.subsetSize:
            raise Exception("subset cannot be larger than the original dataset itself")

        # regression requires more feature vectors (n) than number of features (k)
        if self.subsetSize <= self.k:
            raise Exception("regression requires more feature vectors (n) in each subset than number of features (k)")
        
    def _linear_regression(self, X, y):
        """
            Inputs:
                X: a subset of dataset containing consecutive (subsetSize) feature vectors
                y: a subset of dataset containing consecutive (subsetSize) target values
            Returns:
                regression parameters
        """
        
        # form the gram matrix
        gm = np.dot(X.T, X)
        
        # form cofactor matrix of beta
        cm = np.linalg.inv(gm)
        
        # form moore-penrose pseudoinverse matrix
        mppm = np.dot(cm, np.transpose(X))
        
        # finally calculate beta
        beta = np.dot(mppm, y)
        
        return beta
    
    def pred(self):
        self.y_pred = [np.dot(self.betas[i], self.X[i]) for i in range(self.N)]
        return self.y_pred
    
    def _cod(self):
        """
            calculates coefficient of determination (r-squared)
        """
        if not hasattr(self, 'y_pred'):
            self.pred()
        
        y_mean = np.mean(self.y)
        # total sum of squares
        SS_tot = np.sum((self.y - y_mean) ** 2)
        
        # residual sum of squares
        SS_res = np.sum((self.y - self.y_pred) ** 2)
        
        self.cod = 1 - SS_res / SS_tot
        
    def _adj_cod(self):
        """
            calculates adjusted coefficient of determination (r-squared)
        """
        if not hasattr(self, "cod"):
            self._cod()
            
        self.adj_cod = 1 - (1 - self.cod) * (self.N - 1) / (self.N - self.k)

    def run(self): 
        # divide into subsets and perform OLS on each of them to get params
        # N - (subsetSize - 1) ordinary linear regressions        
        
        # s := number of subsets to form
        s = self.N - (self.subsetSize - 1)
        
        # OLS parameter estimates for all subsets
        alphas = []
        
        for i in range(s):
            print('subset', i)
            alphas.append(self._linear_regression(self.X[i:i+self.subsetSize], self.y[i:i+self.subsetSize]))
            
        alphas = np.array(alphas)
        betas = np.zeros((self.N, self.k))
        
        for i in range(self.N):
            for j in range(self.k):
                l, u = max(0, i - self.subsetSize + 1), min(i+1, s)
                betas[i, j] = sum(alphas[l:u, j]) / (u - l)
                
        self.betas = betas
        
        self._cod()
        self._adj_cod()
        
        return betas
