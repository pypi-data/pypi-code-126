'''_5536.py

BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2376
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6659
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5534, _5535, _5541
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation',)


class BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation(_5541.BevelGearSetHarmonicAnalysisOfSingleExcitation):
    '''BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2376.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2376.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6659.BevelDifferentialGearSetLoadCase':
        '''BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6659.BevelDifferentialGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def bevel_differential_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_5534.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]':
        '''List[BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]: 'BevelDifferentialGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsHarmonicAnalysisOfSingleExcitation, constructor.new(_5534.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bevel_differential_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_5535.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation]':
        '''List[BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation]: 'BevelDifferentialMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesHarmonicAnalysisOfSingleExcitation, constructor.new(_5535.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation))
        return value
