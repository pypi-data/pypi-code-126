'''_1218.py

ElectricMachineResultsTimeStep
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines import (
    _1216, _1215, _1217, _1219
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_TIME_STEP = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineResultsTimeStep')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsTimeStep',)


class ElectricMachineResultsTimeStep(_0.APIBase):
    '''ElectricMachineResultsTimeStep

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_RESULTS_TIME_STEP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsTimeStep.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def time(self) -> 'float':
        '''float: 'Time' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Time

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
    def d_axis_armature_flux_linkage(self) -> 'float':
        '''float: 'DAxisArmatureFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisArmatureFluxLinkage

    @property
    def q_axis_armature_flux_linkage(self) -> 'float':
        '''float: 'QAxisArmatureFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisArmatureFluxLinkage

    @property
    def electrical_angle(self) -> 'float':
        '''float: 'ElectricalAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ElectricalAngle

    @property
    def mechanical_angle(self) -> 'float':
        '''float: 'MechanicalAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MechanicalAngle

    @property
    def torque_mst_single_contour(self) -> 'float':
        '''float: 'TorqueMSTSingleContour' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueMSTSingleContour

    @property
    def torque_from_stator_tooth_tangential_forces(self) -> 'float':
        '''float: 'TorqueFromStatorToothTangentialForces' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueFromStatorToothTangentialForces

    @property
    def torque_mst(self) -> 'float':
        '''float: 'TorqueMST' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueMST

    @property
    def torque_elmer(self) -> 'float':
        '''float: 'TorqueElmer' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueElmer

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def d_axis_reactive_voltages(self) -> 'float':
        '''float: 'DAxisReactiveVoltages' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisReactiveVoltages

    @property
    def q_axis_reactive_voltages(self) -> 'float':
        '''float: 'QAxisReactiveVoltages' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisReactiveVoltages

    @property
    def d_axis_resistive_voltage(self) -> 'float':
        '''float: 'DAxisResistiveVoltage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisResistiveVoltage

    @property
    def q_axis_resistive_voltage(self) -> 'float':
        '''float: 'QAxisResistiveVoltage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisResistiveVoltage

    @property
    def d_axis_flux_linkage(self) -> 'float':
        '''float: 'DAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisFluxLinkage

    @property
    def d_axis_terminal_voltages(self) -> 'float':
        '''float: 'DAxisTerminalVoltages' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisTerminalVoltages

    @property
    def q_axis_flux_linkage(self) -> 'float':
        '''float: 'QAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisFluxLinkage

    @property
    def q_axis_terminal_voltages(self) -> 'float':
        '''float: 'QAxisTerminalVoltages' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisTerminalVoltages

    @property
    def results_for_stator_teeth(self) -> 'List[_1216.ElectricMachineResultsForStatorToothAtTimeStep]':
        '''List[ElectricMachineResultsForStatorToothAtTimeStep]: 'ResultsForStatorTeeth' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsForStatorTeeth, constructor.new(_1216.ElectricMachineResultsForStatorToothAtTimeStep))
        return value

    @property
    def results_for_phases(self) -> 'List[_1215.ElectricMachineResultsForPhaseAtTimeStep]':
        '''List[ElectricMachineResultsForPhaseAtTimeStep]: 'ResultsForPhases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsForPhases, constructor.new(_1215.ElectricMachineResultsForPhaseAtTimeStep))
        return value

    @property
    def results_for_phase_to_phase(self) -> 'List[_1217.ElectricMachineResultsLineToLineAtTimeStep]':
        '''List[ElectricMachineResultsLineToLineAtTimeStep]: 'ResultsForPhaseToPhase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsForPhaseToPhase, constructor.new(_1217.ElectricMachineResultsLineToLineAtTimeStep))
        return value

    @property
    def results_at_locations(self) -> 'List[_1219.ElectricMachineResultsTimeStepAtLocation]':
        '''List[ElectricMachineResultsTimeStepAtLocation]: 'ResultsAtLocations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsAtLocations, constructor.new(_1219.ElectricMachineResultsTimeStepAtLocation))
        return value

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
