'''_1255.py

Temperatures
'''


from mastapy._internal import constructor
from mastapy.utility import _1484
from mastapy._internal.python_net import python_net_import

_TEMPERATURES = python_net_import('SMT.MastaAPI.ElectricMachines', 'Temperatures')


__docformat__ = 'restructuredtext en'
__all__ = ('Temperatures',)


class Temperatures(_1484.IndependentReportablePropertiesBase['Temperatures']):
    '''Temperatures

    This is a mastapy class.
    '''

    TYPE = _TEMPERATURES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Temperatures.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnet_temperature(self) -> 'float':
        '''float: 'MagnetTemperature' is the original name of this property.'''

        return self.wrapped.MagnetTemperature

    @magnet_temperature.setter
    def magnet_temperature(self, value: 'float'):
        self.wrapped.MagnetTemperature = float(value) if value else 0.0

    @property
    def windings_temperature(self) -> 'float':
        '''float: 'WindingsTemperature' is the original name of this property.'''

        return self.wrapped.WindingsTemperature

    @windings_temperature.setter
    def windings_temperature(self, value: 'float'):
        self.wrapped.WindingsTemperature = float(value) if value else 0.0
