'''_1238.py

NonLinearDQModelSettings
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL_SETTINGS = python_net_import('SMT.MastaAPI.ElectricMachines', 'NonLinearDQModelSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModelSettings',)


class NonLinearDQModelSettings(_0.APIBase):
    '''NonLinearDQModelSettings

    This is a mastapy class.
    '''

    TYPE = _NON_LINEAR_DQ_MODEL_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'NonLinearDQModelSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_current_magnitude_points(self) -> 'int':
        '''int: 'NumberOfCurrentMagnitudePoints' is the original name of this property.'''

        return self.wrapped.NumberOfCurrentMagnitudePoints

    @number_of_current_magnitude_points.setter
    def number_of_current_magnitude_points(self, value: 'int'):
        self.wrapped.NumberOfCurrentMagnitudePoints = int(value) if value else 0

    @property
    def number_of_current_angle_points(self) -> 'int':
        '''int: 'NumberOfCurrentAnglePoints' is the original name of this property.'''

        return self.wrapped.NumberOfCurrentAnglePoints

    @number_of_current_angle_points.setter
    def number_of_current_angle_points(self, value: 'int'):
        self.wrapped.NumberOfCurrentAnglePoints = int(value) if value else 0

    @property
    def number_of_time_steps(self) -> 'int':
        '''int: 'NumberOfTimeSteps' is the original name of this property.'''

        return self.wrapped.NumberOfTimeSteps

    @number_of_time_steps.setter
    def number_of_time_steps(self, value: 'int'):
        self.wrapped.NumberOfTimeSteps = int(value) if value else 0

    @property
    def include_efficiency(self) -> 'bool':
        '''bool: 'IncludeEfficiency' is the original name of this property.'''

        return self.wrapped.IncludeEfficiency

    @include_efficiency.setter
    def include_efficiency(self, value: 'bool'):
        self.wrapped.IncludeEfficiency = bool(value) if value else False

    @property
    def reference_speed(self) -> 'float':
        '''float: 'ReferenceSpeed' is the original name of this property.'''

        return self.wrapped.ReferenceSpeed

    @reference_speed.setter
    def reference_speed(self, value: 'float'):
        self.wrapped.ReferenceSpeed = float(value) if value else 0.0

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
