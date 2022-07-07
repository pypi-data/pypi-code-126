'''_1209.py

ElectricMachineEfficiencyMapSettings
'''


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1205
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_EFFICIENCY_MAP_SETTINGS = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineEfficiencyMapSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineEfficiencyMapSettings',)


class ElectricMachineEfficiencyMapSettings(_0.APIBase):
    '''ElectricMachineEfficiencyMapSettings

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_EFFICIENCY_MAP_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineEfficiencyMapSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_speed(self) -> 'float':
        '''float: 'MaximumSpeed' is the original name of this property.'''

        return self.wrapped.MaximumSpeed

    @maximum_speed.setter
    def maximum_speed(self, value: 'float'):
        self.wrapped.MaximumSpeed = float(value) if value else 0.0

    @property
    def minimum_speed(self) -> 'float':
        '''float: 'MinimumSpeed' is the original name of this property.'''

        return self.wrapped.MinimumSpeed

    @minimum_speed.setter
    def minimum_speed(self, value: 'float'):
        self.wrapped.MinimumSpeed = float(value) if value else 0.0

    @property
    def minimum_torque(self) -> 'float':
        '''float: 'MinimumTorque' is the original name of this property.'''

        return self.wrapped.MinimumTorque

    @minimum_torque.setter
    def minimum_torque(self, value: 'float'):
        self.wrapped.MinimumTorque = float(value) if value else 0.0

    @property
    def number_of_torque_values(self) -> 'int':
        '''int: 'NumberOfTorqueValues' is the original name of this property.'''

        return self.wrapped.NumberOfTorqueValues

    @number_of_torque_values.setter
    def number_of_torque_values(self, value: 'int'):
        self.wrapped.NumberOfTorqueValues = int(value) if value else 0

    @property
    def number_of_speed_values(self) -> 'int':
        '''int: 'NumberOfSpeedValues' is the original name of this property.'''

        return self.wrapped.NumberOfSpeedValues

    @number_of_speed_values.setter
    def number_of_speed_values(self, value: 'int'):
        self.wrapped.NumberOfSpeedValues = int(value) if value else 0

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

    @property
    def include_basic_mechanical_losses_calculation(self) -> 'bool':
        '''bool: 'IncludeBasicMechanicalLossesCalculation' is the original name of this property.'''

        return self.wrapped.IncludeBasicMechanicalLossesCalculation

    @include_basic_mechanical_losses_calculation.setter
    def include_basic_mechanical_losses_calculation(self, value: 'bool'):
        self.wrapped.IncludeBasicMechanicalLossesCalculation = bool(value) if value else False

    @property
    def reference_speed_for_mechanical_losses(self) -> 'float':
        '''float: 'ReferenceSpeedForMechanicalLosses' is the original name of this property.'''

        return self.wrapped.ReferenceSpeedForMechanicalLosses

    @reference_speed_for_mechanical_losses.setter
    def reference_speed_for_mechanical_losses(self, value: 'float'):
        self.wrapped.ReferenceSpeedForMechanicalLosses = float(value) if value else 0.0

    @property
    def friction_losses_at_reference_speed(self) -> 'float':
        '''float: 'FrictionLossesAtReferenceSpeed' is the original name of this property.'''

        return self.wrapped.FrictionLossesAtReferenceSpeed

    @friction_losses_at_reference_speed.setter
    def friction_losses_at_reference_speed(self, value: 'float'):
        self.wrapped.FrictionLossesAtReferenceSpeed = float(value) if value else 0.0

    @property
    def friction_loss_exponent(self) -> 'float':
        '''float: 'FrictionLossExponent' is the original name of this property.'''

        return self.wrapped.FrictionLossExponent

    @friction_loss_exponent.setter
    def friction_loss_exponent(self, value: 'float'):
        self.wrapped.FrictionLossExponent = float(value) if value else 0.0

    @property
    def windage_loss_at_reference_speed(self) -> 'float':
        '''float: 'WindageLossAtReferenceSpeed' is the original name of this property.'''

        return self.wrapped.WindageLossAtReferenceSpeed

    @windage_loss_at_reference_speed.setter
    def windage_loss_at_reference_speed(self, value: 'float'):
        self.wrapped.WindageLossAtReferenceSpeed = float(value) if value else 0.0

    @property
    def windage_loss_exponent(self) -> 'float':
        '''float: 'WindageLossExponent' is the original name of this property.'''

        return self.wrapped.WindageLossExponent

    @windage_loss_exponent.setter
    def windage_loss_exponent(self, value: 'float'):
        self.wrapped.WindageLossExponent = float(value) if value else 0.0

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReportNames, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        ''' 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        ''' 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        ''' 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        ''' 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        ''' 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        ''' 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        '''

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
