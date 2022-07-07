'''_5588.py

HypoidGearSetHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2395
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6740
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5586, _5587, _5529
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'HypoidGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetHarmonicAnalysisOfSingleExcitation',)


class HypoidGearSetHarmonicAnalysisOfSingleExcitation(_5529.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation):
    '''HypoidGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2395.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2395.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6740.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6740.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def hypoid_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_5586.HypoidGearHarmonicAnalysisOfSingleExcitation]':
        '''List[HypoidGearHarmonicAnalysisOfSingleExcitation]: 'HypoidGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsHarmonicAnalysisOfSingleExcitation, constructor.new(_5586.HypoidGearHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def hypoid_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_5587.HypoidGearMeshHarmonicAnalysisOfSingleExcitation]':
        '''List[HypoidGearMeshHarmonicAnalysisOfSingleExcitation]: 'HypoidMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesHarmonicAnalysisOfSingleExcitation, constructor.new(_5587.HypoidGearMeshHarmonicAnalysisOfSingleExcitation))
        return value
