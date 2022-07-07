'''_1237.py

NonLinearDQModel
'''


from mastapy._internal import constructor
from mastapy.utility_gui.charts import (
    _1743, _1745, _1736, _1741,
    _1742
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines import _1209, _1208
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL = python_net_import('SMT.MastaAPI.ElectricMachines', 'NonLinearDQModel')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModel',)


class NonLinearDQModel(_1208.ElectricMachineDQModel):
    '''NonLinearDQModel

    This is a mastapy class.
    '''

    TYPE = _NON_LINEAR_DQ_MODEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'NonLinearDQModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_current_values(self) -> 'int':
        '''int: 'NumberOfCurrentValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfCurrentValues

    @property
    def number_of_current_angle_values(self) -> 'int':
        '''int: 'NumberOfCurrentAngleValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfCurrentAngleValues

    @property
    def d_axis_armature_flux_linkage_map(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'DAxisArmatureFluxLinkageMap' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.DAxisArmatureFluxLinkageMap) if self.wrapped.DAxisArmatureFluxLinkageMap is not None else None

    @property
    def q_axis_armature_flux_linkage_map(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'QAxisArmatureFluxLinkageMap' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.QAxisArmatureFluxLinkageMap) if self.wrapped.QAxisArmatureFluxLinkageMap is not None else None

    @property
    def maximum_torque_at_rated_inverter_current(self) -> 'float':
        '''float: 'MaximumTorqueAtRatedInverterCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumTorqueAtRatedInverterCurrent

    @property
    def efficiency_map(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'EfficiencyMap' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.EfficiencyMap) if self.wrapped.EfficiencyMap is not None else None

    @property
    def rotor_hysteresis_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'RotorHysteresisLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.RotorHysteresisLoss) if self.wrapped.RotorHysteresisLoss is not None else None

    @property
    def stator_hysteresis_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'StatorHysteresisLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.StatorHysteresisLoss) if self.wrapped.StatorHysteresisLoss is not None else None

    @property
    def rotor_eddy_current_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'RotorEddyCurrentLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.RotorEddyCurrentLoss) if self.wrapped.RotorEddyCurrentLoss is not None else None

    @property
    def stator_eddy_current_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'StatorEddyCurrentLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.StatorEddyCurrentLoss) if self.wrapped.StatorEddyCurrentLoss is not None else None

    @property
    def rotor_excess_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'RotorExcessLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.RotorExcessLoss) if self.wrapped.RotorExcessLoss is not None else None

    @property
    def stator_excess_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'StatorExcessLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.StatorExcessLoss) if self.wrapped.StatorExcessLoss is not None else None

    @property
    def magnet_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'MagnetLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.MagnetLoss) if self.wrapped.MagnetLoss is not None else None

    @property
    def total_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'TotalLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.TotalLoss) if self.wrapped.TotalLoss is not None else None

    @property
    def dc_winding_loss(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'DCWindingLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.DCWindingLoss) if self.wrapped.DCWindingLoss is not None else None

    @property
    def current_magnitude(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'CurrentMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.CurrentMagnitude) if self.wrapped.CurrentMagnitude is not None else None

    @property
    def current_angle(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'CurrentAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.CurrentAngle) if self.wrapped.CurrentAngle is not None else None

    @property
    def d_axis_current(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'DAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.DAxisCurrent) if self.wrapped.DAxisCurrent is not None else None

    @property
    def q_axis_current(self) -> '_1743.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'QAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1743.ThreeDChartDefinition)(self.wrapped.QAxisCurrent) if self.wrapped.QAxisCurrent is not None else None

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def steady_state_short_circuit_current(self) -> 'float':
        '''float: 'SteadyStateShortCircuitCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SteadyStateShortCircuitCurrent

    @property
    def base_speed(self) -> 'float':
        '''float: 'BaseSpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.BaseSpeed

    @property
    def speed_torque_curve(self) -> '_1745.TwoDChartDefinition':
        '''TwoDChartDefinition: 'SpeedTorqueCurve' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1745.TwoDChartDefinition.TYPE not in self.wrapped.SpeedTorqueCurve.__class__.__mro__:
            raise CastException('Failed to cast speed_torque_curve to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.SpeedTorqueCurve.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SpeedTorqueCurve.__class__)(self.wrapped.SpeedTorqueCurve) if self.wrapped.SpeedTorqueCurve is not None else None

    @property
    def efficiency_map_settings(self) -> '_1209.ElectricMachineEfficiencyMapSettings':
        '''ElectricMachineEfficiencyMapSettings: 'EfficiencyMapSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1209.ElectricMachineEfficiencyMapSettings)(self.wrapped.EfficiencyMapSettings) if self.wrapped.EfficiencyMapSettings is not None else None
