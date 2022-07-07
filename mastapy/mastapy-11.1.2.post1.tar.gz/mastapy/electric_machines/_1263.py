'''_1263.py

Windings
'''


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import (
    _1260, _1248, _1202, _1261,
    _1199
)
from mastapy._internal.python_net import python_net_import
from mastapy import _0

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_WINDINGS = python_net_import('SMT.MastaAPI.ElectricMachines', 'Windings')


__docformat__ = 'restructuredtext en'
__all__ = ('Windings',)


class Windings(_0.APIBase):
    '''Windings

    This is a mastapy class.
    '''

    TYPE = _WINDINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Windings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_parallel_paths(self) -> 'int':
        '''int: 'NumberOfParallelPaths' is the original name of this property.'''

        return self.wrapped.NumberOfParallelPaths

    @number_of_parallel_paths.setter
    def number_of_parallel_paths(self, value: 'int'):
        self.wrapped.NumberOfParallelPaths = int(value) if value else 0

    @property
    def fill_factor_windings(self) -> 'float':
        '''float: 'FillFactorWindings' is the original name of this property.'''

        return self.wrapped.FillFactorWindings

    @fill_factor_windings.setter
    def fill_factor_windings(self, value: 'float'):
        self.wrapped.FillFactorWindings = float(value) if value else 0.0

    @property
    def winding_connection(self) -> '_1260.WindingConnection':
        '''WindingConnection: 'WindingConnection' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.WindingConnection)
        return constructor.new(_1260.WindingConnection)(value) if value is not None else None

    @winding_connection.setter
    def winding_connection(self, value: '_1260.WindingConnection'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.WindingConnection = value

    @property
    def number_of_turns(self) -> 'int':
        '''int: 'NumberOfTurns' is the original name of this property.'''

        return self.wrapped.NumberOfTurns

    @number_of_turns.setter
    def number_of_turns(self, value: 'int'):
        self.wrapped.NumberOfTurns = int(value) if value else 0

    @property
    def number_of_turns_per_phase(self) -> 'int':
        '''int: 'NumberOfTurnsPerPhase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfTurnsPerPhase

    @property
    def mean_length_per_turn(self) -> 'float':
        '''float: 'MeanLengthPerTurn' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeanLengthPerTurn

    @property
    def total_length_of_conductors_in_phase(self) -> 'float':
        '''float: 'TotalLengthOfConductorsInPhase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalLengthOfConductorsInPhase

    @property
    def end_winding_pole_pitch_factor(self) -> 'float':
        '''float: 'EndWindingPolePitchFactor' is the original name of this property.'''

        return self.wrapped.EndWindingPolePitchFactor

    @end_winding_pole_pitch_factor.setter
    def end_winding_pole_pitch_factor(self, value: 'float'):
        self.wrapped.EndWindingPolePitchFactor = float(value) if value else 0.0

    @property
    def single_double_layer_windings(self) -> '_1248.SingleOrDoubleLayerWindings':
        '''SingleOrDoubleLayerWindings: 'SingleDoubleLayerWindings' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.SingleDoubleLayerWindings)
        return constructor.new(_1248.SingleOrDoubleLayerWindings)(value) if value is not None else None

    @single_double_layer_windings.setter
    def single_double_layer_windings(self, value: '_1248.SingleOrDoubleLayerWindings'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SingleDoubleLayerWindings = value

    @property
    def double_layer_winding_slot_positions(self) -> '_1202.DoubleLayerWindingSlotPositions':
        '''DoubleLayerWindingSlotPositions: 'DoubleLayerWindingSlotPositions' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.DoubleLayerWindingSlotPositions)
        return constructor.new(_1202.DoubleLayerWindingSlotPositions)(value) if value is not None else None

    @double_layer_winding_slot_positions.setter
    def double_layer_winding_slot_positions(self, value: '_1202.DoubleLayerWindingSlotPositions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DoubleLayerWindingSlotPositions = value

    @property
    def winding_material_database(self) -> 'str':
        '''str: 'WindingMaterialDatabase' is the original name of this property.'''

        return self.wrapped.WindingMaterialDatabase.SelectedItemName

    @winding_material_database.setter
    def winding_material_database(self, value: 'str'):
        self.wrapped.WindingMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def winding_material(self) -> '_1261.WindingMaterial':
        '''WindingMaterial: 'WindingMaterial' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1261.WindingMaterial)(self.wrapped.WindingMaterial) if self.wrapped.WindingMaterial is not None else None

    @property
    def coils(self) -> 'List[_1199.Coil]':
        '''List[Coil]: 'Coils' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Coils, constructor.new(_1199.Coil))
        return value

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReportNames, str)
        return value

    def generate_default_winding_configuration_coils(self):
        ''' 'GenerateDefaultWindingConfigurationCoils' is the original name of this method.'''

        self.wrapped.GenerateDefaultWindingConfigurationCoils()

    def copy_phase_1_coils_to_other_phases(self):
        ''' 'CopyPhase1CoilsToOtherPhases' is the original name of this method.'''

        self.wrapped.CopyPhase1CoilsToOtherPhases()

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
