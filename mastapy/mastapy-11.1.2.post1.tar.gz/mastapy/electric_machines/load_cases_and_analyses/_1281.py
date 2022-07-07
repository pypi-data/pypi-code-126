'''_1281.py

TorqueSpeedLoadCase
'''


from mastapy.electric_machines.load_cases_and_analyses import _1279, _1270
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.electric_machines import _1205
from mastapy._internal.python_net import python_net_import

_TORQUE_SPEED_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'TorqueSpeedLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueSpeedLoadCase',)


class TorqueSpeedLoadCase(_1270.ElectricMachineLoadCase):
    '''TorqueSpeedLoadCase

    This is a mastapy class.
    '''

    TYPE = _TORQUE_SPEED_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueSpeedLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_specification(self) -> '_1279.SpecifyTorqueOrCurrent':
        '''SpecifyTorqueOrCurrent: 'LoadSpecification' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.LoadSpecification)
        return constructor.new(_1279.SpecifyTorqueOrCurrent)(value) if value is not None else None

    @load_specification.setter
    def load_specification(self, value: '_1279.SpecifyTorqueOrCurrent'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.LoadSpecification = value

    @property
    def target_torque(self) -> 'float':
        '''float: 'TargetTorque' is the original name of this property.'''

        return self.wrapped.TargetTorque

    @target_torque.setter
    def target_torque(self, value: 'float'):
        self.wrapped.TargetTorque = float(value) if value else 0.0

    @property
    def control_strategy(self) -> '_1205.ElectricMachineControlStrategy':
        '''ElectricMachineControlStrategy: 'ControlStrategy' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ControlStrategy)
        return constructor.new(_1205.ElectricMachineControlStrategy)(value) if value is not None else None

    @control_strategy.setter
    def control_strategy(self, value: '_1205.ElectricMachineControlStrategy'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ControlStrategy = value
