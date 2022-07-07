'''_1211.py

ElectricMachineResults
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import (
    _1745, _1736, _1741, _1742
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines import (
    _1206, _1195, _1226, _1236,
    _1243, _1252, _1254, _1220,
    _1218, _1214, _1212
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResults',)


class ElectricMachineResults(_0.APIBase):
    '''ElectricMachineResults

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_flux_linkage(self) -> 'float':
        '''float: 'AverageFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageFluxLinkage

    @property
    def average_d_axis_flux_linkage(self) -> 'float':
        '''float: 'AverageDAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageDAxisFluxLinkage

    @property
    def average_q_axis_flux_linkage(self) -> 'float':
        '''float: 'AverageQAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageQAxisFluxLinkage

    @property
    def average_torque_mst(self) -> 'float':
        '''float: 'AverageTorqueMST' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageTorqueMST

    @property
    def average_torque_elmer(self) -> 'float':
        '''float: 'AverageTorqueElmer' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageTorqueElmer

    @property
    def torque_ripple_mst(self) -> 'float':
        '''float: 'TorqueRippleMST' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueRippleMST

    @property
    def excess_loss_stator(self) -> 'float':
        '''float: 'ExcessLossStator' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExcessLossStator

    @property
    def excess_loss_rotor(self) -> 'float':
        '''float: 'ExcessLossRotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExcessLossRotor

    @property
    def excess_loss_total(self) -> 'float':
        '''float: 'ExcessLossTotal' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExcessLossTotal

    @property
    def hysteresis_loss_stator(self) -> 'float':
        '''float: 'HysteresisLossStator' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HysteresisLossStator

    @property
    def hysteresis_loss_rotor(self) -> 'float':
        '''float: 'HysteresisLossRotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HysteresisLossRotor

    @property
    def hysteresis_loss_total(self) -> 'float':
        '''float: 'HysteresisLossTotal' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HysteresisLossTotal

    @property
    def eddy_current_loss_stator(self) -> 'float':
        '''float: 'EddyCurrentLossStator' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EddyCurrentLossStator

    @property
    def eddy_current_loss_rotor(self) -> 'float':
        '''float: 'EddyCurrentLossRotor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EddyCurrentLossRotor

    @property
    def eddy_current_loss_total(self) -> 'float':
        '''float: 'EddyCurrentLossTotal' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EddyCurrentLossTotal

    @property
    def total_stator_iron_losses(self) -> 'float':
        '''float: 'TotalStatorIronLosses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalStatorIronLosses

    @property
    def total_rotor_iron_losses(self) -> 'float':
        '''float: 'TotalRotorIronLosses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalRotorIronLosses

    @property
    def total_iron_losses(self) -> 'float':
        '''float: 'TotalIronLosses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalIronLosses

    @property
    def total_magnet_losses(self) -> 'float':
        '''float: 'TotalMagnetLosses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalMagnetLosses

    @property
    def total_power_loss(self) -> 'float':
        '''float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalPowerLoss

    @property
    def flux_density_in_air_gap_chart_at_time_0(self) -> '_1745.TwoDChartDefinition':
        '''TwoDChartDefinition: 'FluxDensityInAirGapChartAtTime0' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1745.TwoDChartDefinition.TYPE not in self.wrapped.FluxDensityInAirGapChartAtTime0.__class__.__mro__:
            raise CastException('Failed to cast flux_density_in_air_gap_chart_at_time_0 to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.FluxDensityInAirGapChartAtTime0.__class__.__qualname__))

        return constructor.new_override(self.wrapped.FluxDensityInAirGapChartAtTime0.__class__)(self.wrapped.FluxDensityInAirGapChartAtTime0) if self.wrapped.FluxDensityInAirGapChartAtTime0 is not None else None

    @property
    def force_density_in_air_gap_mst_at_time_0(self) -> '_1745.TwoDChartDefinition':
        '''TwoDChartDefinition: 'ForceDensityInAirGapMSTAtTime0' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1745.TwoDChartDefinition.TYPE not in self.wrapped.ForceDensityInAirGapMSTAtTime0.__class__.__mro__:
            raise CastException('Failed to cast force_density_in_air_gap_mst_at_time_0 to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.ForceDensityInAirGapMSTAtTime0.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ForceDensityInAirGapMSTAtTime0.__class__)(self.wrapped.ForceDensityInAirGapMSTAtTime0) if self.wrapped.ForceDensityInAirGapMSTAtTime0 is not None else None

    @property
    def electric_machine_detail(self) -> '_1206.ElectricMachineDetail':
        '''ElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1206.ElectricMachineDetail.TYPE not in self.wrapped.ElectricMachineDetail.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to ElectricMachineDetail. Expected: {}.'.format(self.wrapped.ElectricMachineDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ElectricMachineDetail.__class__)(self.wrapped.ElectricMachineDetail) if self.wrapped.ElectricMachineDetail is not None else None

    @property
    def electric_machine_detail_of_type_cad_electric_machine_detail(self) -> '_1195.CADElectricMachineDetail':
        '''CADElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1195.CADElectricMachineDetail.TYPE not in self.wrapped.ElectricMachineDetail.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to CADElectricMachineDetail. Expected: {}.'.format(self.wrapped.ElectricMachineDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ElectricMachineDetail.__class__)(self.wrapped.ElectricMachineDetail) if self.wrapped.ElectricMachineDetail is not None else None

    @property
    def electric_machine_detail_of_type_interior_permanent_magnet_machine(self) -> '_1226.InteriorPermanentMagnetMachine':
        '''InteriorPermanentMagnetMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1226.InteriorPermanentMagnetMachine.TYPE not in self.wrapped.ElectricMachineDetail.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to InteriorPermanentMagnetMachine. Expected: {}.'.format(self.wrapped.ElectricMachineDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ElectricMachineDetail.__class__)(self.wrapped.ElectricMachineDetail) if self.wrapped.ElectricMachineDetail is not None else None

    @property
    def electric_machine_detail_of_type_non_cad_electric_machine_detail(self) -> '_1236.NonCADElectricMachineDetail':
        '''NonCADElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1236.NonCADElectricMachineDetail.TYPE not in self.wrapped.ElectricMachineDetail.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to NonCADElectricMachineDetail. Expected: {}.'.format(self.wrapped.ElectricMachineDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ElectricMachineDetail.__class__)(self.wrapped.ElectricMachineDetail) if self.wrapped.ElectricMachineDetail is not None else None

    @property
    def electric_machine_detail_of_type_permanent_magnet_assisted_synchronous_reluctance_machine(self) -> '_1243.PermanentMagnetAssistedSynchronousReluctanceMachine':
        '''PermanentMagnetAssistedSynchronousReluctanceMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1243.PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE not in self.wrapped.ElectricMachineDetail.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to PermanentMagnetAssistedSynchronousReluctanceMachine. Expected: {}.'.format(self.wrapped.ElectricMachineDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ElectricMachineDetail.__class__)(self.wrapped.ElectricMachineDetail) if self.wrapped.ElectricMachineDetail is not None else None

    @property
    def electric_machine_detail_of_type_surface_permanent_magnet_machine(self) -> '_1252.SurfacePermanentMagnetMachine':
        '''SurfacePermanentMagnetMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1252.SurfacePermanentMagnetMachine.TYPE not in self.wrapped.ElectricMachineDetail.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to SurfacePermanentMagnetMachine. Expected: {}.'.format(self.wrapped.ElectricMachineDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ElectricMachineDetail.__class__)(self.wrapped.ElectricMachineDetail) if self.wrapped.ElectricMachineDetail is not None else None

    @property
    def electric_machine_detail_of_type_synchronous_reluctance_machine(self) -> '_1254.SynchronousReluctanceMachine':
        '''SynchronousReluctanceMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1254.SynchronousReluctanceMachine.TYPE not in self.wrapped.ElectricMachineDetail.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to SynchronousReluctanceMachine. Expected: {}.'.format(self.wrapped.ElectricMachineDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ElectricMachineDetail.__class__)(self.wrapped.ElectricMachineDetail) if self.wrapped.ElectricMachineDetail is not None else None

    @property
    def setup(self) -> '_1220.ElectricMachineSetup':
        '''ElectricMachineSetup: 'Setup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1220.ElectricMachineSetup)(self.wrapped.Setup) if self.wrapped.Setup is not None else None

    @property
    def results_timesteps(self) -> 'List[_1218.ElectricMachineResultsTimeStep]':
        '''List[ElectricMachineResultsTimeStep]: 'ResultsTimesteps' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsTimesteps, constructor.new(_1218.ElectricMachineResultsTimeStep))
        return value

    @property
    def results_for_phases(self) -> 'List[_1214.ElectricMachineResultsForPhase]':
        '''List[ElectricMachineResultsForPhase]: 'ResultsForPhases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsForPhases, constructor.new(_1214.ElectricMachineResultsForPhase))
        return value

    @property
    def results_for_line_to_line(self) -> 'List[_1212.ElectricMachineResultsForLineToLine]':
        '''List[ElectricMachineResultsForLineToLine]: 'ResultsForLineToLine' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsForLineToLine, constructor.new(_1212.ElectricMachineResultsForLineToLine))
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
