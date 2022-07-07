'''_1268.py

ElectricMachineAnalysis
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines import (
    _1206, _1195, _1226, _1236,
    _1243, _1252, _1254
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines.load_cases_and_analyses import (
    _1271, _1265, _1267, _1270,
    _1275, _1281
)
from mastapy import _7389, _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineAnalysis',)


class ElectricMachineAnalysis(_0.APIBase):
    '''ElectricMachineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_time(self) -> 'float':
        '''float: 'AnalysisTime' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AnalysisTime

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
    def load_case(self) -> '_1271.ElectricMachineLoadCaseBase':
        '''ElectricMachineLoadCaseBase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1271.ElectricMachineLoadCaseBase.TYPE not in self.wrapped.LoadCase.__class__.__mro__:
            raise CastException('Failed to cast load_case to ElectricMachineLoadCaseBase. Expected: {}.'.format(self.wrapped.LoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadCase.__class__)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def load_case_of_type_dynamic_force_load_case(self) -> '_1265.DynamicForceLoadCase':
        '''DynamicForceLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1265.DynamicForceLoadCase.TYPE not in self.wrapped.LoadCase.__class__.__mro__:
            raise CastException('Failed to cast load_case to DynamicForceLoadCase. Expected: {}.'.format(self.wrapped.LoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadCase.__class__)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def load_case_of_type_efficiency_map_load_case(self) -> '_1267.EfficiencyMapLoadCase':
        '''EfficiencyMapLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1267.EfficiencyMapLoadCase.TYPE not in self.wrapped.LoadCase.__class__.__mro__:
            raise CastException('Failed to cast load_case to EfficiencyMapLoadCase. Expected: {}.'.format(self.wrapped.LoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadCase.__class__)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def load_case_of_type_electric_machine_load_case(self) -> '_1270.ElectricMachineLoadCase':
        '''ElectricMachineLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1270.ElectricMachineLoadCase.TYPE not in self.wrapped.LoadCase.__class__.__mro__:
            raise CastException('Failed to cast load_case to ElectricMachineLoadCase. Expected: {}.'.format(self.wrapped.LoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadCase.__class__)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def load_case_of_type_non_linear_dq_model_multiple_operating_points_load_case(self) -> '_1275.NonLinearDQModelMultipleOperatingPointsLoadCase':
        '''NonLinearDQModelMultipleOperatingPointsLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1275.NonLinearDQModelMultipleOperatingPointsLoadCase.TYPE not in self.wrapped.LoadCase.__class__.__mro__:
            raise CastException('Failed to cast load_case to NonLinearDQModelMultipleOperatingPointsLoadCase. Expected: {}.'.format(self.wrapped.LoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadCase.__class__)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def load_case_of_type_torque_speed_load_case(self) -> '_1281.TorqueSpeedLoadCase':
        '''TorqueSpeedLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1281.TorqueSpeedLoadCase.TYPE not in self.wrapped.LoadCase.__class__.__mro__:
            raise CastException('Failed to cast load_case to TorqueSpeedLoadCase. Expected: {}.'.format(self.wrapped.LoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadCase.__class__)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReportNames, str)
        return value

    def perform_analysis(self, token: '_7389.TaskProgress'):
        ''' 'PerformAnalysis' is the original name of this method.

        Args:
            token (mastapy.TaskProgress)
        '''

        self.wrapped.PerformAnalysis(token.wrapped if token else None)

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
