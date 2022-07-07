'''_1201.py

CoolingDuctLayerSpecification
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_COOLING_DUCT_LAYER_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'CoolingDuctLayerSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('CoolingDuctLayerSpecification',)


class CoolingDuctLayerSpecification(_0.APIBase):
    '''CoolingDuctLayerSpecification

    This is a mastapy class.
    '''

    TYPE = _COOLING_DUCT_LAYER_SPECIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoolingDuctLayerSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_ducts(self) -> 'int':
        '''int: 'NumberOfDucts' is the original name of this property.'''

        return self.wrapped.NumberOfDucts

    @number_of_ducts.setter
    def number_of_ducts(self, value: 'int'):
        self.wrapped.NumberOfDucts = int(value) if value else 0

    @property
    def duct_diameter(self) -> 'float':
        '''float: 'DuctDiameter' is the original name of this property.'''

        return self.wrapped.DuctDiameter

    @duct_diameter.setter
    def duct_diameter(self, value: 'float'):
        self.wrapped.DuctDiameter = float(value) if value else 0.0

    @property
    def radial_offset(self) -> 'float':
        '''float: 'RadialOffset' is the original name of this property.'''

        return self.wrapped.RadialOffset

    @radial_offset.setter
    def radial_offset(self, value: 'float'):
        self.wrapped.RadialOffset = float(value) if value else 0.0

    @property
    def first_duct_angle(self) -> 'float':
        '''float: 'FirstDuctAngle' is the original name of this property.'''

        return self.wrapped.FirstDuctAngle

    @first_duct_angle.setter
    def first_duct_angle(self, value: 'float'):
        self.wrapped.FirstDuctAngle = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

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
