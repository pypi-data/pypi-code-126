import numpy as np
from scipy.integrate import odeint

class Kuramoto:

    def __init__(self, n, k, timeseries, omega_n = None, theta_n = None, adjacency_nxn = None):
        self.n = n #number of neurons
        self.k = k #coupling constant
        self.normalised_coupling = k / n 
        self.timeseries = timeseries #timepoints at which to plot results
        if omega_n is not None: 
            self.omega_n = omega_n #intrinsic frequencies
        else:
            self.omega_n = abs(np.random.normal(loc = 1, scale = 0.1, size = n))
        if theta_n is not None:
            self.theta_n = theta_n #starting phase
        else:
            self.theta_n = np.random.random(n) * 2 * np.pi
        if adjacency_nxn is not None:
            self.adjacency_nxn = adjacency_nxn #adjacency matrix
        else:
            adjacency_nxn = np.ones([n,n])
            np.fill_diagonal(adjacency_nxn, 0)
            self.adjacency_nxn = adjacency_nxn
    
    def derivative(self, theta_n, t=None): #t is included for compatibility with odeint
        theta_n1, theta_n2 = np.meshgrid(theta_n, theta_n) #creates co-ordinate matrices of current phases
        phase_diff = theta_n2 - theta_n1 #calculates phase differences between all pairs of neurons by subtracting co-ordinate matrices
        d_theta_n = self.omega_n + self.normalised_coupling * np.sum(self.adjacency_nxn * np.sin(phase_diff), axis = 0)
        return d_theta_n
    
    def phase_timeseries(self):
        theta_nxt = odeint(self.derivative, self.theta_n, self.timeseries) #numerically obtains phase at the given timepoints
        return theta_nxt
    
    def coherence_timeseries(self):
        theta_nxt = self.phase_timeseries()
        average_x_t = np.mean(np.cos(theta_nxt), axis = 1)
        average_y_t = np.mean(np.sin(theta_nxt), axis = 1)
        coherence_t = (average_x_t ** 2 + average_y_t ** 2) ** 0.5 #calcuates coherence as the magnitude of the resultant vector at a given time
        return coherence_t
    
    def mean_frequency_timeseries(self):
        theta_nxt = self.phase_timeseries()
        derivative_t = np.apply_along_axis(self.derivative, axis = 1, arr = theta_nxt)
        omega_avg_t = np.mean(derivative_t, axis = 1)
        return omega_avg_t