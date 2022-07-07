'''_1227.py

IronLossCoefficients
'''


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_IRON_LOSS_COEFFICIENTS = python_net_import('SMT.MastaAPI.ElectricMachines', 'IronLossCoefficients')


__docformat__ = 'restructuredtext en'
__all__ = ('IronLossCoefficients',)


class IronLossCoefficients(_0.APIBase):
    '''IronLossCoefficients

    This is a mastapy class.
    '''

    TYPE = _IRON_LOSS_COEFFICIENTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'IronLossCoefficients.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def c_coefficient_hysteresis(self) -> 'float':
        '''float: 'CCoefficientHysteresis' is the original name of this property.'''

        return self.wrapped.CCoefficientHysteresis

    @c_coefficient_hysteresis.setter
    def c_coefficient_hysteresis(self, value: 'float'):
        self.wrapped.CCoefficientHysteresis = float(value) if value else 0.0

    @property
    def c_coefficient_eddy(self) -> 'float':
        '''float: 'CCoefficientEddy' is the original name of this property.'''

        return self.wrapped.CCoefficientEddy

    @c_coefficient_eddy.setter
    def c_coefficient_eddy(self, value: 'float'):
        self.wrapped.CCoefficientEddy = float(value) if value else 0.0

    @property
    def c_coefficient_excess(self) -> 'float':
        '''float: 'CCoefficientExcess' is the original name of this property.'''

        return self.wrapped.CCoefficientExcess

    @c_coefficient_excess.setter
    def c_coefficient_excess(self, value: 'float'):
        self.wrapped.CCoefficientExcess = float(value) if value else 0.0

    @property
    def frequency_exponent_eddy(self) -> 'float':
        '''float: 'FrequencyExponentEddy' is the original name of this property.'''

        return self.wrapped.FrequencyExponentEddy

    @frequency_exponent_eddy.setter
    def frequency_exponent_eddy(self, value: 'float'):
        self.wrapped.FrequencyExponentEddy = float(value) if value else 0.0

    @property
    def frequency_exponent_hysteresis(self) -> 'float':
        '''float: 'FrequencyExponentHysteresis' is the original name of this property.'''

        return self.wrapped.FrequencyExponentHysteresis

    @frequency_exponent_hysteresis.setter
    def frequency_exponent_hysteresis(self, value: 'float'):
        self.wrapped.FrequencyExponentHysteresis = float(value) if value else 0.0

    @property
    def frequency_exponent_excess(self) -> 'float':
        '''float: 'FrequencyExponentExcess' is the original name of this property.'''

        return self.wrapped.FrequencyExponentExcess

    @frequency_exponent_excess.setter
    def frequency_exponent_excess(self, value: 'float'):
        self.wrapped.FrequencyExponentExcess = float(value) if value else 0.0

    @property
    def field_exponent_eddy(self) -> 'float':
        '''float: 'FieldExponentEddy' is the original name of this property.'''

        return self.wrapped.FieldExponentEddy

    @field_exponent_eddy.setter
    def field_exponent_eddy(self, value: 'float'):
        self.wrapped.FieldExponentEddy = float(value) if value else 0.0

    @property
    def field_exponent_hysteresis(self) -> 'float':
        '''float: 'FieldExponentHysteresis' is the original name of this property.'''

        return self.wrapped.FieldExponentHysteresis

    @field_exponent_hysteresis.setter
    def field_exponent_hysteresis(self, value: 'float'):
        self.wrapped.FieldExponentHysteresis = float(value) if value else 0.0

    @property
    def field_exponent_excess(self) -> 'float':
        '''float: 'FieldExponentExcess' is the original name of this property.'''

        return self.wrapped.FieldExponentExcess

    @field_exponent_excess.setter
    def field_exponent_excess(self, value: 'float'):
        self.wrapped.FieldExponentExcess = float(value) if value else 0.0
