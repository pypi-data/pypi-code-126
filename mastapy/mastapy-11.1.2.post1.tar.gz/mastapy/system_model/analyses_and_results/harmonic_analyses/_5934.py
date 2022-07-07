'''_5934.py

WormGearHarmonicAnalysis
'''


from mastapy.system_model.part_model.gears import _2411
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6815
from mastapy.system_model.analyses_and_results.system_deflections import _2693
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5855
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'WormGearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearHarmonicAnalysis',)


class WormGearHarmonicAnalysis(_5855.GearHarmonicAnalysis):
    '''WormGearHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2411.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2411.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6815.WormGearLoadCase':
        '''WormGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6815.WormGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2693.WormGearSystemDeflection':
        '''WormGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2693.WormGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
