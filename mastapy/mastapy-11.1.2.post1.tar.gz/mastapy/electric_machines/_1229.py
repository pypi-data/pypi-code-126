'''_1229.py

LinearDQModel
'''


from mastapy._internal import constructor
from mastapy.electric_machines import _1208
from mastapy._internal.python_net import python_net_import

_LINEAR_DQ_MODEL = python_net_import('SMT.MastaAPI.ElectricMachines', 'LinearDQModel')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearDQModel',)


class LinearDQModel(_1208.ElectricMachineDQModel):
    '''LinearDQModel

    This is a mastapy class.
    '''

    TYPE = _LINEAR_DQ_MODEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LinearDQModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apparent_d_axis_inductance(self) -> 'float':
        '''float: 'ApparentDAxisInductance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ApparentDAxisInductance

    @property
    def apparent_q_axis_inductance(self) -> 'float':
        '''float: 'ApparentQAxisInductance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ApparentQAxisInductance

    @property
    def base_speed_from_mtpa(self) -> 'float':
        '''float: 'BaseSpeedFromMTPA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.BaseSpeedFromMTPA

    @property
    def max_speed(self) -> 'float':
        '''float: 'MaxSpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaxSpeed

    @property
    def steady_state_short_circuit_current(self) -> 'float':
        '''float: 'SteadyStateShortCircuitCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SteadyStateShortCircuitCurrent

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name
