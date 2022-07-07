'''_1214.py

ElectricMachineResultsForPhase
'''


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1228
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_PHASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineResultsForPhase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsForPhase',)


class ElectricMachineResultsForPhase(_0.APIBase):
    '''ElectricMachineResultsForPhase

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_PHASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsForPhase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def phase(self) -> 'int':
        '''int: 'Phase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Phase

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def power_factor_angle(self) -> 'float':
        '''float: 'PowerFactorAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PowerFactorAngle

    @property
    def power_factor_direction(self) -> '_1228.LeadingOrLagging':
        '''LeadingOrLagging: 'PowerFactorDirection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.PowerFactorDirection)
        return constructor.new(_1228.LeadingOrLagging)(value) if value is not None else None

    @property
    def power_factor(self) -> 'float':
        '''float: 'PowerFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PowerFactor

    @property
    def power_factor_with_harmonic_distortion_adjustment(self) -> 'float':
        '''float: 'PowerFactorWithHarmonicDistortionAdjustment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PowerFactorWithHarmonicDistortionAdjustment

    @property
    def phase_reactive_voltage_rms(self) -> 'float':
        '''float: 'PhaseReactiveVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseReactiveVoltageRMS

    @property
    def phase_resistive_voltage_rms(self) -> 'float':
        '''float: 'PhaseResistiveVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistiveVoltageRMS

    @property
    def phase_resistive_voltage_peak(self) -> 'float':
        '''float: 'PhaseResistiveVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistiveVoltagePeak

    @property
    def phase_terminal_voltage_peak(self) -> 'float':
        '''float: 'PhaseTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseTerminalVoltagePeak

    @property
    def phase_terminal_voltage_rms(self) -> 'float':
        '''float: 'PhaseTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseTerminalVoltageRMS

    @property
    def terminal_voltage_harmonic_distortion(self) -> 'float':
        '''float: 'TerminalVoltageHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TerminalVoltageHarmonicDistortion

    @property
    def phase_current_peak(self) -> 'float':
        '''float: 'PhaseCurrentPeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseCurrentPeak

    @property
    def phase_current_rms(self) -> 'float':
        '''float: 'PhaseCurrentRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseCurrentRMS

    @property
    def phase_current_harmonic_distortion(self) -> 'float':
        '''float: 'PhaseCurrentHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseCurrentHarmonicDistortion

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
