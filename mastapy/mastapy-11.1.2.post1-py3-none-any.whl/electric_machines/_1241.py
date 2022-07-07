'''_1241.py

OnLoadElectricMachineResults
'''


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1228, _1263, _1211
from mastapy._internal.python_net import python_net_import

_ON_LOAD_ELECTRIC_MACHINE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines', 'OnLoadElectricMachineResults')


__docformat__ = 'restructuredtext en'
__all__ = ('OnLoadElectricMachineResults',)


class OnLoadElectricMachineResults(_1211.ElectricMachineResults):
    '''OnLoadElectricMachineResults

    This is a mastapy class.
    '''

    TYPE = _ON_LOAD_ELECTRIC_MACHINE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OnLoadElectricMachineResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def torque_ripple_percentage_mst(self) -> 'float':
        '''float: 'TorqueRipplePercentageMST' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueRipplePercentageMST

    @property
    def average_torque_dq(self) -> 'float':
        '''float: 'AverageTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AverageTorqueDQ

    @property
    def torque_constant(self) -> 'float':
        '''float: 'TorqueConstant' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueConstant

    @property
    def motor_constant(self) -> 'float':
        '''float: 'MotorConstant' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MotorConstant

    @property
    def electrical_loading(self) -> 'float':
        '''float: 'ElectricalLoading' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ElectricalLoading

    @property
    def dc_winding_losses(self) -> 'float':
        '''float: 'DCWindingLosses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DCWindingLosses

    @property
    def winding_material_resistivity(self) -> 'float':
        '''float: 'WindingMaterialResistivity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WindingMaterialResistivity

    @property
    def phase_resistance(self) -> 'float':
        '''float: 'PhaseResistance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistance

    @property
    def line_resistance(self) -> 'float':
        '''float: 'LineResistance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineResistance

    @property
    def stall_current(self) -> 'float':
        '''float: 'StallCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.StallCurrent

    @property
    def stall_torque(self) -> 'float':
        '''float: 'StallTorque' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.StallTorque

    @property
    def line_to_line_terminal_voltage_peak(self) -> 'float':
        '''float: 'LineToLineTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineToLineTerminalVoltagePeak

    @property
    def line_to_line_terminal_voltage_rms(self) -> 'float':
        '''float: 'LineToLineTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineToLineTerminalVoltageRMS

    @property
    def phase_resistive_voltage_peak(self) -> 'float':
        '''float: 'PhaseResistiveVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistiveVoltagePeak

    @property
    def phase_resistive_voltage_rms(self) -> 'float':
        '''float: 'PhaseResistiveVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistiveVoltageRMS

    @property
    def phase_resistive_voltage_drms(self) -> 'float':
        '''float: 'PhaseResistiveVoltageDRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistiveVoltageDRMS

    @property
    def phase_resistive_voltage_qrms(self) -> 'float':
        '''float: 'PhaseResistiveVoltageQRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseResistiveVoltageQRMS

    @property
    def phase_terminal_voltage_peak(self) -> 'float':
        '''float: 'PhaseTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseTerminalVoltagePeak

    @property
    def phase_terminal_voltage_rms(self) -> 'float':
        '''float: 'PhaseTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseTerminalVoltageRMS

    @property
    def line_to_line_terminal_voltage_total_harmonic_distortion(self) -> 'float':
        '''float: 'LineToLineTerminalVoltageTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineToLineTerminalVoltageTotalHarmonicDistortion

    @property
    def phase_terminal_voltage_total_harmonic_distortion(self) -> 'float':
        '''float: 'PhaseTerminalVoltageTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseTerminalVoltageTotalHarmonicDistortion

    @property
    def total_power_loss(self) -> 'float':
        '''float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalPowerLoss

    @property
    def output_power(self) -> 'float':
        '''float: 'OutputPower' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OutputPower

    @property
    def input_power(self) -> 'float':
        '''float: 'InputPower' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InputPower

    @property
    def efficiency(self) -> 'float':
        '''float: 'Efficiency' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Efficiency

    @property
    def average_power_factor_angle(self) -> 'float':
        '''float: 'AveragePowerFactorAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AveragePowerFactorAngle

    @property
    def average_power_factor(self) -> 'float':
        '''float: 'AveragePowerFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AveragePowerFactor

    @property
    def power_factor_direction(self) -> '_1228.LeadingOrLagging':
        '''LeadingOrLagging: 'PowerFactorDirection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.PowerFactorDirection)
        return constructor.new(_1228.LeadingOrLagging)(value) if value is not None else None

    @property
    def average_power_factor_with_harmonic_distortion_adjustment(self) -> 'float':
        '''float: 'AveragePowerFactorWithHarmonicDistortionAdjustment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AveragePowerFactorWithHarmonicDistortionAdjustment

    @property
    def windings(self) -> '_1263.Windings':
        '''Windings: 'Windings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1263.Windings)(self.wrapped.Windings) if self.wrapped.Windings is not None else None
