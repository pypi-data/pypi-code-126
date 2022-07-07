'''_1242.py

OpenCircuitElectricMachineResults
'''


from mastapy._internal import constructor
from mastapy.electric_machines import _1211
from mastapy._internal.python_net import python_net_import

_OPEN_CIRCUIT_ELECTRIC_MACHINE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines', 'OpenCircuitElectricMachineResults')


__docformat__ = 'restructuredtext en'
__all__ = ('OpenCircuitElectricMachineResults',)


class OpenCircuitElectricMachineResults(_1211.ElectricMachineResults):
    '''OpenCircuitElectricMachineResults

    This is a mastapy class.
    '''

    TYPE = _OPEN_CIRCUIT_ELECTRIC_MACHINE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OpenCircuitElectricMachineResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def line_to_line_back_emf_peak(self) -> 'float':
        '''float: 'LineToLineBackEMFPeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineToLineBackEMFPeak

    @property
    def line_to_line_back_emfrms(self) -> 'float':
        '''float: 'LineToLineBackEMFRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineToLineBackEMFRMS

    @property
    def phase_back_emf_peak(self) -> 'float':
        '''float: 'PhaseBackEMFPeak' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseBackEMFPeak

    @property
    def phase_back_emfrms(self) -> 'float':
        '''float: 'PhaseBackEMFRMS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseBackEMFRMS

    @property
    def line_to_line_back_emf_total_harmonic_distortion(self) -> 'float':
        '''float: 'LineToLineBackEMFTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LineToLineBackEMFTotalHarmonicDistortion

    @property
    def phase_back_emf_total_harmonic_distortion(self) -> 'float':
        '''float: 'PhaseBackEMFTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PhaseBackEMFTotalHarmonicDistortion

    @property
    def back_emf_constant(self) -> 'float':
        '''float: 'BackEMFConstant' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.BackEMFConstant
