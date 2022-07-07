'''_1275.py

NonLinearDQModelMultipleOperatingPointsLoadCase
'''


from mastapy.electric_machines import _1205
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1271
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'NonLinearDQModelMultipleOperatingPointsLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModelMultipleOperatingPointsLoadCase',)


class NonLinearDQModelMultipleOperatingPointsLoadCase(_1271.ElectricMachineLoadCaseBase):
    '''NonLinearDQModelMultipleOperatingPointsLoadCase

    This is a mastapy class.
    '''

    TYPE = _NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'NonLinearDQModelMultipleOperatingPointsLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
