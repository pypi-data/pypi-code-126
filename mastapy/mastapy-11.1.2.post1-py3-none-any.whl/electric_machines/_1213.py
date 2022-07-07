'''_1213.py

ElectricMachineResultsForOpenCircuitAndOnLoad
'''


from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import (
    _1745, _1736, _1741, _1742
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines import _1242, _1241
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_OPEN_CIRCUIT_AND_ON_LOAD = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineResultsForOpenCircuitAndOnLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsForOpenCircuitAndOnLoad',)


class ElectricMachineResultsForOpenCircuitAndOnLoad(_0.APIBase):
    '''ElectricMachineResultsForOpenCircuitAndOnLoad

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_OPEN_CIRCUIT_AND_ON_LOAD

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsForOpenCircuitAndOnLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def line_line_inductance(self) -> 'float':
        '''float: 'LineLineInductance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineLineInductance

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
    def apparent_inductance_multiplied_by_current_d_axis(self) -> 'float':
        '''float: 'ApparentInductanceMultipliedByCurrentDAxis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ApparentInductanceMultipliedByCurrentDAxis

    @property
    def apparent_inductance_multiplied_by_current_q_axis(self) -> 'float':
        '''float: 'ApparentInductanceMultipliedByCurrentQAxis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ApparentInductanceMultipliedByCurrentQAxis

    @property
    def electrical_constant(self) -> 'float':
        '''float: 'ElectricalConstant' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ElectricalConstant

    @property
    def mechanical_time_constant(self) -> 'float':
        '''float: 'MechanicalTimeConstant' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MechanicalTimeConstant

    @property
    def average_reluctance_torque_dq(self) -> 'float':
        '''float: 'AverageReluctanceTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageReluctanceTorqueDQ

    @property
    def average_alignment_torque_dq(self) -> 'float':
        '''float: 'AverageAlignmentTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageAlignmentTorqueDQ

    @property
    def current_angle_for_maximum_torque_dq(self) -> 'float':
        '''float: 'CurrentAngleForMaximumTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CurrentAngleForMaximumTorqueDQ

    @property
    def maximum_torque_achievable_dq(self) -> 'float':
        '''float: 'MaximumTorqueAchievableDQ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumTorqueAchievableDQ

    @property
    def base_speed_dq(self) -> 'float':
        '''float: 'BaseSpeedDQ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.BaseSpeedDQ

    @property
    def maximum_speed_dq(self) -> 'float':
        '''float: 'MaximumSpeedDQ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumSpeedDQ

    @property
    def steady_state_short_circuit_current(self) -> 'float':
        '''float: 'SteadyStateShortCircuitCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SteadyStateShortCircuitCurrent

    @property
    def phase_terminal_voltage_from_phasor_rms(self) -> 'float':
        '''float: 'PhaseTerminalVoltageFromPhasorRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseTerminalVoltageFromPhasorRMS

    @property
    def phase_reactive_voltage_drms(self) -> 'float':
        '''float: 'PhaseReactiveVoltageDRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseReactiveVoltageDRMS

    @property
    def phase_reactive_voltage_qrms(self) -> 'float':
        '''float: 'PhaseReactiveVoltageQRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseReactiveVoltageQRMS

    @property
    def load_angle_from_phasor(self) -> 'float':
        '''float: 'LoadAngleFromPhasor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LoadAngleFromPhasor

    @property
    def power_factor_angle_from_phasor(self) -> 'float':
        '''float: 'PowerFactorAngleFromPhasor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PowerFactorAngleFromPhasor

    @property
    def dq_model_chart(self) -> '_1745.TwoDChartDefinition':
        '''TwoDChartDefinition: 'DQModelChart' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1745.TwoDChartDefinition.TYPE not in self.wrapped.DQModelChart.__class__.__mro__:
            raise CastException('Failed to cast dq_model_chart to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.DQModelChart.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DQModelChart.__class__)(self.wrapped.DQModelChart) if self.wrapped.DQModelChart is not None else None

    @property
    def phasor_diagram(self) -> 'Image':
        '''Image: 'PhasorDiagram' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_smt_bitmap(self.wrapped.PhasorDiagram)
        return value

    @property
    def open_circuit_results(self) -> '_1242.OpenCircuitElectricMachineResults':
        '''OpenCircuitElectricMachineResults: 'OpenCircuitResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1242.OpenCircuitElectricMachineResults)(self.wrapped.OpenCircuitResults) if self.wrapped.OpenCircuitResults is not None else None

    @property
    def on_load_results(self) -> '_1241.OnLoadElectricMachineResults':
        '''OnLoadElectricMachineResults: 'OnLoadResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1241.OnLoadElectricMachineResults)(self.wrapped.OnLoadResults) if self.wrapped.OnLoadResults is not None else None

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
