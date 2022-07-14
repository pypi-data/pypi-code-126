import json
from scipy.interpolate import interp1d, interp2d

# TODO add to next release ( test + doc)
class Value(object):
    '''
    Value class represent the informations stored in a parameter. Each value can be a single value, a curve or a map. All points are interpolated
    '''
    def __init__(self,x,y=None,z=None):
        '''
        Initialisation of the value
        :param val: values in string json format
        '''
        self._x=json.loads(X)
        self._y=None
        self._z=None
        if y is None:
            if z is None:
                self._f = lambda x: None
        else:
            self._y = json.loads(y)
            if z is None:
                self.f = interp1d(self._x, self._y)
            else:
                self._z=json.loads(z)
                self._f = interp2d(self._x, self._y, self._z)

    def x(self):
        '''
        Get the X value(s)
        :return: X values
        '''
        return self._x

    def x(self,pos):
        '''
        Return the X value at a position ( interpolated from the array)
        :param pos: position in the array
        :return: X value
        '''
        return self._x[pos]

    def y(self,x):
        '''
        Return the Y value at a X position ( interpolated from the array)
        :param pos: position in the array
        :return: Y value
        '''
        return self._f(x)

    def z(self,x,y):
        '''
        Return the Z value at a X,Y position ( interpolated from the array)
        :param pos: position in the array
        :return: Z value
        '''
        return self._f(x,y)
