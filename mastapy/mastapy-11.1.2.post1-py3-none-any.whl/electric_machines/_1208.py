'''_1208.py

ElectricMachineDQModel
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DQ_MODEL = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineDQModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineDQModel',)


class ElectricMachineDQModel(_0.APIBase):
    '''ElectricMachineDQModel

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_DQ_MODEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineDQModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def phase_resistance(self) -> 'float':
        '''float: 'PhaseResistance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistance

    @property
    def rated_inverter_current(self) -> 'float':
        '''float: 'RatedInverterCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RatedInverterCurrent

    @property
    def maximum_voltage(self) -> 'float':
        '''float: 'MaximumVoltage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumVoltage

    @property
    def number_of_phases(self) -> 'int':
        '''int: 'NumberOfPhases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfPhases

    @property
    def number_of_pole_pairs(self) -> 'int':
        '''int: 'NumberOfPolePairs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfPolePairs

    @property
    def permanent_magnet_flux_linkage(self) -> 'float':
        '''float: 'PermanentMagnetFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PermanentMagnetFluxLinkage

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def current_angle_to_maximise_torque_at_rated_inverter_current(self) -> 'float':
        '''float: 'CurrentAngleToMaximiseTorqueAtRatedInverterCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CurrentAngleToMaximiseTorqueAtRatedInverterCurrent

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
