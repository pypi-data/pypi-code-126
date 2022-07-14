import numpy
from scipy.interpolate import interp1d

class Gearbox(object):

    def __init__(self):
        super().__init__()
        self.ratio=interp1d([1,2,3,4,5],[10,9,8,7,6])

    def ratio(self,gear):
        '''
        Return the gear ratio for a given gear
        :param gear: gear number
        :return: gear ratio
        '''
        return self.ratio(gear)

    
