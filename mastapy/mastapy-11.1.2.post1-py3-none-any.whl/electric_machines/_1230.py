'''_1230.py

Magnet
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.electric_machines import _1232
from mastapy import _0

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_MAGNET = python_net_import('SMT.MastaAPI.ElectricMachines', 'Magnet')


__docformat__ = 'restructuredtext en'
__all__ = ('Magnet',)


class Magnet(_0.APIBase):
    '''Magnet

    This is a mastapy class.
    '''

    TYPE = _MAGNET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Magnet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def width(self) -> 'float':
        '''float: 'Width' is the original name of this property.'''

        return self.wrapped.Width

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

    @property
    def thickness(self) -> 'float':
        '''float: 'Thickness' is the original name of this property.'''

        return self.wrapped.Thickness

    @thickness.setter
    def thickness(self, value: 'float'):
        self.wrapped.Thickness = float(value) if value else 0.0

    @property
    def number_of_segments_in_axial_direction(self) -> 'overridable.Overridable_int':
        '''overridable.Overridable_int: 'NumberOfSegmentsInAxialDirection' is the original name of this property.'''

        return constructor.new(overridable.Overridable_int)(self.wrapped.NumberOfSegmentsInAxialDirection) if self.wrapped.NumberOfSegmentsInAxialDirection is not None else None

    @number_of_segments_in_axial_direction.setter
    def number_of_segments_in_axial_direction(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfSegmentsInAxialDirection = value

    @property
    def number_of_segments_along_width(self) -> 'int':
        '''int: 'NumberOfSegmentsAlongWidth' is the original name of this property.'''

        return self.wrapped.NumberOfSegmentsAlongWidth

    @number_of_segments_along_width.setter
    def number_of_segments_along_width(self, value: 'int'):
        self.wrapped.NumberOfSegmentsAlongWidth = int(value) if value else 0

    @property
    def magnet_material_database(self) -> 'str':
        '''str: 'MagnetMaterialDatabase' is the original name of this property.'''

        return self.wrapped.MagnetMaterialDatabase.SelectedItemName

    @magnet_material_database.setter
    def magnet_material_database(self, value: 'str'):
        self.wrapped.MagnetMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def length_of_each_segment(self) -> 'float':
        '''float: 'LengthOfEachSegment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LengthOfEachSegment

    @property
    def width_of_each_segment(self) -> 'float':
        '''float: 'WidthOfEachSegment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WidthOfEachSegment

    @property
    def two_d3d_magnet_loss_factor(self) -> 'float':
        '''float: 'TwoD3DMagnetLossFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TwoD3DMagnetLossFactor

    @property
    def magnet_material(self) -> '_1232.MagnetMaterial':
        '''MagnetMaterial: 'MagnetMaterial' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1232.MagnetMaterial)(self.wrapped.MagnetMaterial) if self.wrapped.MagnetMaterial is not None else None

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
