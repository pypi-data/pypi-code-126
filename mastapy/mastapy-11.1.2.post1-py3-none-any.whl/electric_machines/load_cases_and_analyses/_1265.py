'''_1265.py

DynamicForceLoadCase
'''


from typing import List

from mastapy.electric_machines.load_cases_and_analyses import (
    _1277, _1280, _1276, _1282,
    _1275
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis.elmer import _153
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import

_DOUBLE = python_net_import('System', 'Double')
_DYNAMIC_FORCE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'DynamicForceLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceLoadCase',)


class DynamicForceLoadCase(_1275.NonLinearDQModelMultipleOperatingPointsLoadCase):
    '''DynamicForceLoadCase

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_FORCE_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicForceLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def operating_points_specification_method(self) -> '_1277.OperatingPointsSpecificationMethod':
        '''OperatingPointsSpecificationMethod: 'OperatingPointsSpecificationMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.OperatingPointsSpecificationMethod)
        return constructor.new(_1277.OperatingPointsSpecificationMethod)(value) if value is not None else None

    @operating_points_specification_method.setter
    def operating_points_specification_method(self, value: '_1277.OperatingPointsSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.OperatingPointsSpecificationMethod = value

    @property
    def number_of_operating_points(self) -> 'int':
        '''int: 'NumberOfOperatingPoints' is the original name of this property.'''

        return self.wrapped.NumberOfOperatingPoints

    @number_of_operating_points.setter
    def number_of_operating_points(self, value: 'int'):
        self.wrapped.NumberOfOperatingPoints = int(value) if value else 0

    @property
    def minimum_speed(self) -> 'float':
        '''float: 'MinimumSpeed' is the original name of this property.'''

        return self.wrapped.MinimumSpeed

    @minimum_speed.setter
    def minimum_speed(self, value: 'float'):
        self.wrapped.MinimumSpeed = float(value) if value else 0.0

    @property
    def maximum_speed(self) -> 'float':
        '''float: 'MaximumSpeed' is the original name of this property.'''

        return self.wrapped.MaximumSpeed

    @maximum_speed.setter
    def maximum_speed(self, value: 'float'):
        self.wrapped.MaximumSpeed = float(value) if value else 0.0

    @property
    def speed_points_distribution(self) -> '_1280.SpeedPointsDistribution':
        '''SpeedPointsDistribution: 'SpeedPointsDistribution' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.SpeedPointsDistribution)
        return constructor.new(_1280.SpeedPointsDistribution)(value) if value is not None else None

    @speed_points_distribution.setter
    def speed_points_distribution(self, value: '_1280.SpeedPointsDistribution'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SpeedPointsDistribution = value

    @property
    def number_of_steps_per_operating_point_specification_method(self) -> '_1276.NumberOfStepsPerOperatingPointSpecificationMethod':
        '''NumberOfStepsPerOperatingPointSpecificationMethod: 'NumberOfStepsPerOperatingPointSpecificationMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.NumberOfStepsPerOperatingPointSpecificationMethod)
        return constructor.new(_1276.NumberOfStepsPerOperatingPointSpecificationMethod)(value) if value is not None else None

    @number_of_steps_per_operating_point_specification_method.setter
    def number_of_steps_per_operating_point_specification_method(self, value: '_1276.NumberOfStepsPerOperatingPointSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.NumberOfStepsPerOperatingPointSpecificationMethod = value

    @property
    def number_of_steps_for_the_analysis_period(self) -> 'int':
        '''int: 'NumberOfStepsForTheAnalysisPeriod' is the original name of this property.'''

        return self.wrapped.NumberOfStepsForTheAnalysisPeriod

    @number_of_steps_for_the_analysis_period.setter
    def number_of_steps_for_the_analysis_period(self, value: 'int'):
        self.wrapped.NumberOfStepsForTheAnalysisPeriod = int(value) if value else 0

    @property
    def analysis_period(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod':
        '''enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod: 'AnalysisPeriod' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.AnalysisPeriod, value) if self.wrapped.AnalysisPeriod is not None else None

    @analysis_period.setter
    def analysis_period(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.AnalysisPeriod = value

    @property
    def operating_points(self) -> 'List[_1282.TorqueSpeedOperatingPoint]':
        '''List[TorqueSpeedOperatingPoint]: 'OperatingPoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OperatingPoints, constructor.new(_1282.TorqueSpeedOperatingPoint))
        return value

    def add_operating_point(self):
        ''' 'AddOperatingPoint' is the original name of this method.'''

        self.wrapped.AddOperatingPoint()

    def set_speeds(self, values: 'List[float]'):
        ''' 'SetSpeeds' is the original name of this method.

        Args:
            values (List[float])
        '''

        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetSpeeds(values)

    def set_speeds_in_si_units(self, values: 'List[float]'):
        ''' 'SetSpeedsInSIUnits' is the original name of this method.

        Args:
            values (List[float])
        '''

        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetSpeedsInSIUnits(values)

    def add_operating_point_with_torque_and_speed(self, torque: 'float', speed: 'float') -> '_1282.TorqueSpeedOperatingPoint':
        ''' 'AddOperatingPoint' is the original name of this method.

        Args:
            torque (float)
            speed (float)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.TorqueSpeedOperatingPoint
        '''

        torque = float(torque)
        speed = float(speed)
        method_result = self.wrapped.AddOperatingPoint.Overloads[_DOUBLE, _DOUBLE](torque if torque else 0.0, speed if speed else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def remove_operating_point(self, operating_point: '_1282.TorqueSpeedOperatingPoint'):
        ''' 'RemoveOperatingPoint' is the original name of this method.

        Args:
            operating_point (mastapy.electric_machines.load_cases_and_analyses.TorqueSpeedOperatingPoint)
        '''

        self.wrapped.RemoveOperatingPoint(operating_point.wrapped if operating_point else None)
