'''_1206.py

ElectricMachineDetail
'''


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import (
    _1221, _1220, _1245, _1196,
    _1225, _1244, _1253, _1192,
    _1197, _1249, _1237, _1238
)
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy.math_utility import _1422
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineDetail',)


class ElectricMachineDetail(_0.APIBase):
    '''ElectricMachineDetail

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineDetail.TYPE'):
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
    def electric_machine_type(self) -> '_1221.ElectricMachineType':
        '''ElectricMachineType: 'ElectricMachineType' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.ElectricMachineType)
        return constructor.new(_1221.ElectricMachineType)(value) if value is not None else None

    @property
    def dc_bus_voltage(self) -> 'float':
        '''float: 'DCBusVoltage' is the original name of this property.'''

        return self.wrapped.DCBusVoltage

    @dc_bus_voltage.setter
    def dc_bus_voltage(self, value: 'float'):
        self.wrapped.DCBusVoltage = float(value) if value else 0.0

    @property
    def rated_inverter_current_peak(self) -> 'float':
        '''float: 'RatedInverterCurrentPeak' is the original name of this property.'''

        return self.wrapped.RatedInverterCurrentPeak

    @rated_inverter_current_peak.setter
    def rated_inverter_current_peak(self, value: 'float'):
        self.wrapped.RatedInverterCurrentPeak = float(value) if value else 0.0

    @property
    def line_line_supply_voltage_rms(self) -> 'float':
        '''float: 'LineLineSupplyVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineLineSupplyVoltageRMS

    @property
    def phase_supply_voltage_peak(self) -> 'float':
        '''float: 'PhaseSupplyVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseSupplyVoltagePeak

    @property
    def phase_supply_voltage_rms(self) -> 'float':
        '''float: 'PhaseSupplyVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseSupplyVoltageRMS

    @property
    def enclosing_volume(self) -> 'float':
        '''float: 'EnclosingVolume' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EnclosingVolume

    @property
    def select_setup(self) -> 'list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup':
        '''list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup: 'SelectSetup' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup)(self.wrapped.SelectSetup) if self.wrapped.SelectSetup is not None else None

    @select_setup.setter
    def select_setup(self, value: 'list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectSetup = value

    @property
    def radial_air_gap(self) -> 'float':
        '''float: 'RadialAirGap' is the original name of this property.'''

        return self.wrapped.RadialAirGap

    @radial_air_gap.setter
    def radial_air_gap(self, value: 'float'):
        self.wrapped.RadialAirGap = float(value) if value else 0.0

    @property
    def number_of_slots_per_pole_per_phase(self) -> 'float':
        '''float: 'NumberOfSlotsPerPolePerPhase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfSlotsPerPolePerPhase

    @property
    def number_of_phases(self) -> 'int':
        '''int: 'NumberOfPhases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfPhases

    @property
    def has_non_linear_dq_model(self) -> 'bool':
        '''bool: 'HasNonLinearDQModel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasNonLinearDQModel

    @property
    def rotor(self) -> '_1245.Rotor':
        '''Rotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1245.Rotor.TYPE not in self.wrapped.Rotor.__class__.__mro__:
            raise CastException('Failed to cast rotor to Rotor. Expected: {}.'.format(self.wrapped.Rotor.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Rotor.__class__)(self.wrapped.Rotor) if self.wrapped.Rotor is not None else None

    @property
    def rotor_of_type_cad_rotor(self) -> '_1196.CADRotor':
        '''CADRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1196.CADRotor.TYPE not in self.wrapped.Rotor.__class__.__mro__:
            raise CastException('Failed to cast rotor to CADRotor. Expected: {}.'.format(self.wrapped.Rotor.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Rotor.__class__)(self.wrapped.Rotor) if self.wrapped.Rotor is not None else None

    @property
    def rotor_of_type_interior_permanent_magnet_and_synchronous_reluctance_rotor(self) -> '_1225.InteriorPermanentMagnetAndSynchronousReluctanceRotor':
        '''InteriorPermanentMagnetAndSynchronousReluctanceRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1225.InteriorPermanentMagnetAndSynchronousReluctanceRotor.TYPE not in self.wrapped.Rotor.__class__.__mro__:
            raise CastException('Failed to cast rotor to InteriorPermanentMagnetAndSynchronousReluctanceRotor. Expected: {}.'.format(self.wrapped.Rotor.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Rotor.__class__)(self.wrapped.Rotor) if self.wrapped.Rotor is not None else None

    @property
    def rotor_of_type_permanent_magnet_rotor(self) -> '_1244.PermanentMagnetRotor':
        '''PermanentMagnetRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1244.PermanentMagnetRotor.TYPE not in self.wrapped.Rotor.__class__.__mro__:
            raise CastException('Failed to cast rotor to PermanentMagnetRotor. Expected: {}.'.format(self.wrapped.Rotor.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Rotor.__class__)(self.wrapped.Rotor) if self.wrapped.Rotor is not None else None

    @property
    def rotor_of_type_surface_permanent_magnet_rotor(self) -> '_1253.SurfacePermanentMagnetRotor':
        '''SurfacePermanentMagnetRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1253.SurfacePermanentMagnetRotor.TYPE not in self.wrapped.Rotor.__class__.__mro__:
            raise CastException('Failed to cast rotor to SurfacePermanentMagnetRotor. Expected: {}.'.format(self.wrapped.Rotor.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Rotor.__class__)(self.wrapped.Rotor) if self.wrapped.Rotor is not None else None

    @property
    def stator(self) -> '_1192.AbstractStator':
        '''AbstractStator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1192.AbstractStator.TYPE not in self.wrapped.Stator.__class__.__mro__:
            raise CastException('Failed to cast stator to AbstractStator. Expected: {}.'.format(self.wrapped.Stator.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Stator.__class__)(self.wrapped.Stator) if self.wrapped.Stator is not None else None

    @property
    def stator_of_type_cad_stator(self) -> '_1197.CADStator':
        '''CADStator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1197.CADStator.TYPE not in self.wrapped.Stator.__class__.__mro__:
            raise CastException('Failed to cast stator to CADStator. Expected: {}.'.format(self.wrapped.Stator.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Stator.__class__)(self.wrapped.Stator) if self.wrapped.Stator is not None else None

    @property
    def stator_of_type_stator(self) -> '_1249.Stator':
        '''Stator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1249.Stator.TYPE not in self.wrapped.Stator.__class__.__mro__:
            raise CastException('Failed to cast stator to Stator. Expected: {}.'.format(self.wrapped.Stator.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Stator.__class__)(self.wrapped.Stator) if self.wrapped.Stator is not None else None

    @property
    def selected_setup(self) -> '_1220.ElectricMachineSetup':
        '''ElectricMachineSetup: 'SelectedSetup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1220.ElectricMachineSetup)(self.wrapped.SelectedSetup) if self.wrapped.SelectedSetup is not None else None

    @property
    def non_linear_dq_model(self) -> '_1237.NonLinearDQModel':
        '''NonLinearDQModel: 'NonLinearDQModel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1237.NonLinearDQModel)(self.wrapped.NonLinearDQModel) if self.wrapped.NonLinearDQModel is not None else None

    @property
    def non_linear_dq_model_generator_settings(self) -> '_1238.NonLinearDQModelSettings':
        '''NonLinearDQModelSettings: 'NonLinearDQModelGeneratorSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1238.NonLinearDQModelSettings)(self.wrapped.NonLinearDQModelGeneratorSettings) if self.wrapped.NonLinearDQModelGeneratorSettings is not None else None

    @property
    def setups(self) -> 'List[_1220.ElectricMachineSetup]':
        '''List[ElectricMachineSetup]: 'Setups' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Setups, constructor.new(_1220.ElectricMachineSetup))
        return value

    @property
    def results_locations(self) -> 'List[_1422.Named2DLocation]':
        '''List[Named2DLocation]: 'ResultsLocations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsLocations, constructor.new(_1422.Named2DLocation))
        return value

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReportNames, str)
        return value

    def generate_non_linear_dq_model(self):
        ''' 'GenerateNonLinearDQModel' is the original name of this method.'''

        self.wrapped.GenerateNonLinearDQModel()

    def duplicate_setup(self, setup: '_1220.ElectricMachineSetup') -> '_1220.ElectricMachineSetup':
        ''' 'DuplicateSetup' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.ElectricMachineSetup
        '''

        method_result = self.wrapped.DuplicateSetup(setup.wrapped if setup else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_results_location(self, name: 'str'):
        ''' 'AddResultsLocation' is the original name of this method.

        Args:
            name (str)
        '''

        name = str(name)
        self.wrapped.AddResultsLocation(name if name else '')

    def remove_results_location(self, name: 'str'):
        ''' 'RemoveResultsLocation' is the original name of this method.

        Args:
            name (str)
        '''

        name = str(name)
        self.wrapped.RemoveResultsLocation(name if name else '')

    def export_to_smt_format(self, file_name: 'str'):
        ''' 'ExportToSMTFormat' is the original name of this method.

        Args:
            file_name (str)
        '''

        file_name = str(file_name)
        self.wrapped.ExportToSMTFormat(file_name if file_name else '')

    def write_dxf_to(self, file_name: 'str'):
        ''' 'WriteDxfTo' is the original name of this method.

        Args:
            file_name (str)
        '''

        file_name = str(file_name)
        self.wrapped.WriteDxfTo(file_name if file_name else '')

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
