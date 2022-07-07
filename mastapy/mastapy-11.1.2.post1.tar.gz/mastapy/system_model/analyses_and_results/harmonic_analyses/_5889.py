'''_5889.py

PartToPartShearCouplingHarmonicAnalysis
'''


from mastapy.system_model.part_model.couplings import _2448
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6764
from mastapy.system_model.analyses_and_results.system_deflections import _2643
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5823
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'PartToPartShearCouplingHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHarmonicAnalysis',)


class PartToPartShearCouplingHarmonicAnalysis(_5823.CouplingHarmonicAnalysis):
    '''PartToPartShearCouplingHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2448.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2448.PartToPartShearCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6764.PartToPartShearCouplingLoadCase':
        '''PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6764.PartToPartShearCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2643.PartToPartShearCouplingSystemDeflection':
        '''PartToPartShearCouplingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2643.PartToPartShearCouplingSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
