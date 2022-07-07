'''_1220.py

ElectricMachineSetup
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1210, _1204
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_SETUP = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineSetup')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineSetup',)


class ElectricMachineSetup(_0.APIBase):
    '''ElectricMachineSetup

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_SETUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineSetup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.'''

        return self.wrapped.Name

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def slot_area(self) -> 'float':
        '''float: 'SlotArea' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SlotArea

    @property
    def winding_material_area(self) -> 'float':
        '''float: 'WindingMaterialArea' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WindingMaterialArea

    @property
    def estimated_material_cost(self) -> 'float':
        '''float: 'EstimatedMaterialCost' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EstimatedMaterialCost

    @property
    def number_of_elements(self) -> 'int':
        '''int: 'NumberOfElements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfElements

    @property
    def number_of_nodes(self) -> 'int':
        '''int: 'NumberOfNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfNodes

    @property
    def meshing_options(self) -> '_1210.ElectricMachineMeshingOptions':
        '''ElectricMachineMeshingOptions: 'MeshingOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1210.ElectricMachineMeshingOptions)(self.wrapped.MeshingOptions) if self.wrapped.MeshingOptions is not None else None

    @property
    def eccentricity(self) -> '_1204.Eccentricity':
        '''Eccentricity: 'Eccentricity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1204.Eccentricity)(self.wrapped.Eccentricity) if self.wrapped.Eccentricity is not None else None

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReportNames, str)
        return value

    def generate_mesh(self):
        ''' 'GenerateMesh' is the original name of this method.'''

        self.wrapped.GenerateMesh()

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
