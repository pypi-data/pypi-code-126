import numpy
from scipy.interpolate import interp1d

class Engine(object):
    '''
    Class engine offers support for engine calculation and estimation.
    '''
    def __init__(self):
        super().__init__()
        self.n=[600,1000,2000,4000,6000]
        self.t=[100,500,1000,800,100]
        self.p= [self.n[i]*self.t[i]/ 60 * 2 * numpy.pi for i in range(len(self.n))]
        self.trq= interp1d(self.n,self.t)
        self.np = interp1d(self.p, self.n)

    def max_torque(self):
        '''
        Get the maximum torque for the engine torque curve
        :return: max torque in Nm
        '''
        return max(self.t)

    def npower(self,power):
        return self.np(power)

    def power(self,speed,limit=100):
        '''
        Return the Power at a given engine speed and a percentage torque
        :param speed: engine speed in rpm
        :param limit: max percentage torque
        :return: engie power in watts
        '''
        return self.torque(speed,limit)*speed/60*2*numpy.pi

    def torque(self,speed,limit=100):
        '''
        Return the torque at an engine speed with a max percentage torque ( 100% is full torque)
        :param speed: engine speed in rpm
        :param limit: maximum percent torque from curve
        :return: engine torque in Nm
        '''
        return self.trq(speed)*limit/100

