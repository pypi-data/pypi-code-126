'''_1283.py

ElectricMachineHarmonicLoadDataBase
'''


from PIL.Image import Image

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.electric_machines.harmonic_load_data import _1286, _1287
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility_gui.charts import _1744
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_BASE = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'ElectricMachineHarmonicLoadDataBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataBase',)


class ElectricMachineHarmonicLoadDataBase(_1287.SpeedDependentHarmonicLoadData):
    '''ElectricMachineHarmonicLoadDataBase

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_BASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display_interpolated_data(self) -> 'bool':
        '''bool: 'DisplayInterpolatedData' is the original name of this property.'''

        return self.wrapped.DisplayInterpolatedData

    @display_interpolated_data.setter
    def display_interpolated_data(self, value: 'bool'):
        self.wrapped.DisplayInterpolatedData = bool(value) if value else False

    @property
    def sum_over_all_nodes(self) -> 'bool':
        '''bool: 'SumOverAllNodes' is the original name of this property.'''

        return self.wrapped.SumOverAllNodes

    @sum_over_all_nodes.setter
    def sum_over_all_nodes(self, value: 'bool'):
        self.wrapped.SumOverAllNodes = bool(value) if value else False

    @property
    def speed_to_view(self) -> 'float':
        '''float: 'SpeedToView' is the original name of this property.'''

        return self.wrapped.SpeedToView

    @speed_to_view.setter
    def speed_to_view(self, value: 'float'):
        self.wrapped.SpeedToView = float(value) if value else 0.0

    @property
    def show_all_teeth(self) -> 'bool':
        '''bool: 'ShowAllTeeth' is the original name of this property.'''

        return self.wrapped.ShowAllTeeth

    @show_all_teeth.setter
    def show_all_teeth(self, value: 'bool'):
        self.wrapped.ShowAllTeeth = bool(value) if value else False

    @property
    def compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads(self) -> 'bool':
        '''bool: 'CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads' is the original name of this property.'''

        return self.wrapped.CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads

    @compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads.setter
    def compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads(self, value: 'bool'):
        self.wrapped.CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads = bool(value) if value else False

    @property
    def data_type_for_force_distribution_and_temporal_spatial_harmonics_charts(self) -> 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType':
        '''enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType: 'DataTypeForForceDistributionAndTemporalSpatialHarmonicsCharts' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.DataTypeForForceDistributionAndTemporalSpatialHarmonicsCharts, value) if self.wrapped.DataTypeForForceDistributionAndTemporalSpatialHarmonicsCharts is not None else None

    @data_type_for_force_distribution_and_temporal_spatial_harmonics_charts.setter
    def data_type_for_force_distribution_and_temporal_spatial_harmonics_charts(self, value: 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataTypeForForceDistributionAndTemporalSpatialHarmonicsCharts = value

    @property
    def force_distribution(self) -> 'Image':
        '''Image: 'ForceDistribution' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_smt_bitmap(self.wrapped.ForceDistribution)
        return value

    @property
    def force_distribution_3d(self) -> '_1744.ThreeDVectorChartDefinition':
        '''ThreeDVectorChartDefinition: 'ForceDistribution3D' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1744.ThreeDVectorChartDefinition)(self.wrapped.ForceDistribution3D) if self.wrapped.ForceDistribution3D is not None else None

    @property
    def plot_as_vectors(self) -> 'bool':
        '''bool: 'PlotAsVectors' is the original name of this property.'''

        return self.wrapped.PlotAsVectors

    @plot_as_vectors.setter
    def plot_as_vectors(self, value: 'bool'):
        self.wrapped.PlotAsVectors = bool(value) if value else False

    @property
    def show_all_forces(self) -> 'bool':
        '''bool: 'ShowAllForces' is the original name of this property.'''

        return self.wrapped.ShowAllForces

    @show_all_forces.setter
    def show_all_forces(self, value: 'bool'):
        self.wrapped.ShowAllForces = bool(value) if value else False

    @property
    def invert_axis(self) -> 'bool':
        '''bool: 'InvertAxis' is the original name of this property.'''

        return self.wrapped.InvertAxis

    @invert_axis.setter
    def invert_axis(self, value: 'bool'):
        self.wrapped.InvertAxis = bool(value) if value else False
