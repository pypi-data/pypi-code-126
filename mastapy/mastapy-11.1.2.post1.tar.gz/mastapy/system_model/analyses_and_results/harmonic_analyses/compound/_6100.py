'''_6100.py

WormGearSetCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2412
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6098, _6099, _6035
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5936
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'WormGearSetCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundHarmonicAnalysis',)


class WormGearSetCompoundHarmonicAnalysis(_6035.GearSetCompoundHarmonicAnalysis):
    '''WormGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def worm_gears_compound_harmonic_analysis(self) -> 'List[_6098.WormGearCompoundHarmonicAnalysis]':
        '''List[WormGearCompoundHarmonicAnalysis]: 'WormGearsCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsCompoundHarmonicAnalysis, constructor.new(_6098.WormGearCompoundHarmonicAnalysis))
        return value

    @property
    def worm_meshes_compound_harmonic_analysis(self) -> 'List[_6099.WormGearMeshCompoundHarmonicAnalysis]':
        '''List[WormGearMeshCompoundHarmonicAnalysis]: 'WormMeshesCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesCompoundHarmonicAnalysis, constructor.new(_6099.WormGearMeshCompoundHarmonicAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5936.WormGearSetHarmonicAnalysis]':
        '''List[WormGearSetHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5936.WormGearSetHarmonicAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5936.WormGearSetHarmonicAnalysis]':
        '''List[WormGearSetHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5936.WormGearSetHarmonicAnalysis))
        return value
