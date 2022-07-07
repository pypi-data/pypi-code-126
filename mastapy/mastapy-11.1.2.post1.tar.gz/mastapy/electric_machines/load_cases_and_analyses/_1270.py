'''_1270.py

ElectricMachineLoadCase
'''


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1234, _1255
from mastapy.nodal_analysis.elmer import _154, _153
from mastapy.electric_machines.load_cases_and_analyses import _1271
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineLoadCase',)


class ElectricMachineLoadCase(_1271.ElectricMachineLoadCaseBase):
    '''ElectricMachineLoadCase

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_number_of_steps_for_voltages_and_losses_calculation(self) -> 'int':
        '''int: 'MinimumNumberOfStepsForVoltagesAndLossesCalculation' is the original name of this property.'''

        return self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation

    @minimum_number_of_steps_for_voltages_and_losses_calculation.setter
    def minimum_number_of_steps_for_voltages_and_losses_calculation(self, value: 'int'):
        self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation = int(value) if value else 0

    @property
    def motoring_or_generating(self) -> '_1234.MotoringOrGenerating':
        '''MotoringOrGenerating: 'MotoringOrGenerating' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.MotoringOrGenerating)
        return constructor.new(_1234.MotoringOrGenerating)(value) if value is not None else None

    @motoring_or_generating.setter
    def motoring_or_generating(self, value: '_1234.MotoringOrGenerating'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MotoringOrGenerating = value

    @property
    def speed(self) -> 'float':
        '''float: 'Speed' is the original name of this property.'''

        return self.wrapped.Speed

    @speed.setter
    def speed(self, value: 'float'):
        self.wrapped.Speed = float(value) if value else 0.0

    @property
    def peak_line_current(self) -> 'float':
        '''float: 'PeakLineCurrent' is the original name of this property.'''

        return self.wrapped.PeakLineCurrent

    @peak_line_current.setter
    def peak_line_current(self, value: 'float'):
        self.wrapped.PeakLineCurrent = float(value) if value else 0.0

    @property
    def rms_line_current(self) -> 'float':
        '''float: 'RMSLineCurrent' is the original name of this property.'''

        return self.wrapped.RMSLineCurrent

    @rms_line_current.setter
    def rms_line_current(self, value: 'float'):
        self.wrapped.RMSLineCurrent = float(value) if value else 0.0

    @property
    def current_angle(self) -> 'float':
        '''float: 'CurrentAngle' is the original name of this property.'''

        return self.wrapped.CurrentAngle

    @current_angle.setter
    def current_angle(self, value: 'float'):
        self.wrapped.CurrentAngle = float(value) if value else 0.0

    @property
    def total_number_of_time_steps(self) -> 'int':
        '''int: 'TotalNumberOfTimeSteps' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalNumberOfTimeSteps

    @property
    def number_of_steps_per_cycle(self) -> 'int':
        '''int: 'NumberOfStepsPerCycle' is the original name of this property.'''

        return self.wrapped.NumberOfStepsPerCycle

    @number_of_steps_per_cycle.setter
    def number_of_steps_per_cycle(self, value: 'int'):
        self.wrapped.NumberOfStepsPerCycle = int(value) if value else 0

    @property
    def number_of_cycles(self) -> 'int':
        '''int: 'NumberOfCycles' is the original name of this property.'''

        return self.wrapped.NumberOfCycles

    @number_of_cycles.setter
    def number_of_cycles(self, value: 'int'):
        self.wrapped.NumberOfCycles = int(value) if value else 0

    @property
    def include_losses(self) -> 'bool':
        '''bool: 'IncludeLosses' is the original name of this property.'''

        return self.wrapped.IncludeLosses

    @include_losses.setter
    def include_losses(self, value: 'bool'):
        self.wrapped.IncludeLosses = bool(value) if value else False

    @property
    def include_magnet_losses(self) -> 'bool':
        '''bool: 'IncludeMagnetLosses' is the original name of this property.'''

        return self.wrapped.IncludeMagnetLosses

    @include_magnet_losses.setter
    def include_magnet_losses(self, value: 'bool'):
        self.wrapped.IncludeMagnetLosses = bool(value) if value else False

    @property
    def include_open_circuit_calculation(self) -> 'bool':
        '''bool: 'IncludeOpenCircuitCalculation' is the original name of this property.'''

        return self.wrapped.IncludeOpenCircuitCalculation

    @include_open_circuit_calculation.setter
    def include_open_circuit_calculation(self, value: 'bool'):
        self.wrapped.IncludeOpenCircuitCalculation = bool(value) if value else False

    @property
    def simulation_type(self) -> '_154.ElmerSimulationType':
        '''ElmerSimulationType: 'SimulationType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.SimulationType)
        return constructor.new(_154.ElmerSimulationType)(value) if value is not None else None

    @simulation_type.setter
    def simulation_type(self, value: '_154.ElmerSimulationType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SimulationType = value

    @property
    def analysis_period(self) -> '_153.ElectricMachineAnalysisPeriod':
        '''ElectricMachineAnalysisPeriod: 'AnalysisPeriod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AnalysisPeriod)
        return constructor.new(_153.ElectricMachineAnalysisPeriod)(value) if value is not None else None

    @analysis_period.setter
    def analysis_period(self, value: '_153.ElectricMachineAnalysisPeriod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AnalysisPeriod = value

    @property
    def temperatures(self) -> '_1255.Temperatures':
        '''Temperatures: 'Temperatures' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1255.Temperatures)(self.wrapped.Temperatures) if self.wrapped.Temperatures is not None else None
