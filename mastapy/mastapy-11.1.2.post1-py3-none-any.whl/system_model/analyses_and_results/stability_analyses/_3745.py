'''_3745.py

WormGearSetStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2412
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6817
from mastapy.system_model.analyses_and_results.stability_analyses import _3746, _3744, _3678
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'WormGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetStabilityAnalysis',)


class WormGearSetStabilityAnalysis(_3678.GearSetStabilityAnalysis):
    '''WormGearSetStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2412.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6817.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6817.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def worm_gears_stability_analysis(self) -> 'List[_3746.WormGearStabilityAnalysis]':
        '''List[WormGearStabilityAnalysis]: 'WormGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsStabilityAnalysis, constructor.new(_3746.WormGearStabilityAnalysis))
        return value

    @property
    def worm_meshes_stability_analysis(self) -> 'List[_3744.WormGearMeshStabilityAnalysis]':
        '''List[WormGearMeshStabilityAnalysis]: 'WormMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesStabilityAnalysis, constructor.new(_3744.WormGearMeshStabilityAnalysis))
        return value
