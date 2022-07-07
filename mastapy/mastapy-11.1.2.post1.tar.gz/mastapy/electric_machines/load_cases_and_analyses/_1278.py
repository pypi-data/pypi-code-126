'''_1278.py

SingleOperatingPointAnalysis
'''


from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1270, _1281, _1268
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines import _1213
from mastapy._internal.python_net import python_net_import

_SINGLE_OPERATING_POINT_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SingleOperatingPointAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleOperatingPointAnalysis',)


class SingleOperatingPointAnalysis(_1268.ElectricMachineAnalysis):
    '''SingleOperatingPointAnalysis

    This is a mastapy class.
    '''

    TYPE = _SINGLE_OPERATING_POINT_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SingleOperatingPointAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def peak_current_density_conductors(self) -> 'float':
        '''float: 'PeakCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PeakCurrentDensityConductors

    @property
    def rms_current_density_conductors(self) -> 'float':
        '''float: 'RMSCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RMSCurrentDensityConductors

    @property
    def d_axis_current_density_conductors(self) -> 'float':
        '''float: 'DAxisCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisCurrentDensityConductors

    @property
    def q_axis_current_density_conductors(self) -> 'float':
        '''float: 'QAxisCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisCurrentDensityConductors

    @property
    def peak_current_density_slot(self) -> 'float':
        '''float: 'PeakCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PeakCurrentDensitySlot

    @property
    def rms_current_density_slot(self) -> 'float':
        '''float: 'RMSCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RMSCurrentDensitySlot

    @property
    def d_axis_current_density_slot(self) -> 'float':
        '''float: 'DAxisCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisCurrentDensitySlot

    @property
    def q_axis_current_density_slot(self) -> 'float':
        '''float: 'QAxisCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisCurrentDensitySlot

    @property
    def d_axis_current(self) -> 'float':
        '''float: 'DAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DAxisCurrent

    @property
    def q_axis_current(self) -> 'float':
        '''float: 'QAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.QAxisCurrent

    @property
    def peak_phase_current(self) -> 'float':
        '''float: 'PeakPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PeakPhaseCurrent

    @property
    def rms_phase_current(self) -> 'float':
        '''float: 'RMSPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RMSPhaseCurrent

    @property
    def phase_current_drms(self) -> 'float':
        '''float: 'PhaseCurrentDRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseCurrentDRMS

    @property
    def phase_current_qrms(self) -> 'float':
        '''float: 'PhaseCurrentQRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseCurrentQRMS

    @property
    def electrical_frequency(self) -> 'float':
        '''float: 'ElectricalFrequency' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ElectricalFrequency

    @property
    def mechanical_period(self) -> 'float':
        '''float: 'MechanicalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MechanicalPeriod

    @property
    def slot_passing_period(self) -> 'float':
        '''float: 'SlotPassingPeriod' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SlotPassingPeriod

    @property
    def electrical_period(self) -> 'float':
        '''float: 'ElectricalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ElectricalPeriod

    @property
    def time_step_increment(self) -> 'float':
        '''float: 'TimeStepIncrement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TimeStepIncrement

    @property
    def load_case(self) -> '_1270.ElectricMachineLoadCase':
        '''ElectricMachineLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1270.ElectricMachineLoadCase.TYPE not in self.wrapped.LoadCase.__class__.__mro__:
            raise CastException('Failed to cast load_case to ElectricMachineLoadCase. Expected: {}.'.format(self.wrapped.LoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadCase.__class__)(self.wrapped.LoadCase) if self.wrapped.LoadCase is not None else None

    @property
    def electric_machine_results(self) -> '_1213.ElectricMachineResultsForOpenCircuitAndOnLoad':
        '''ElectricMachineResultsForOpenCircuitAndOnLoad: 'ElectricMachineResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1213.ElectricMachineResultsForOpenCircuitAndOnLoad)(self.wrapped.ElectricMachineResults) if self.wrapped.ElectricMachineResults is not None else None
