'''_6144.py

ConceptGearSetDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2382
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6677
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6142, _6143, _6174
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConceptGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetDynamicAnalysis',)


class ConceptGearSetDynamicAnalysis(_6174.GearSetDynamicAnalysis):
    '''ConceptGearSetDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2382.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2382.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6677.ConceptGearSetLoadCase':
        '''ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6677.ConceptGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def concept_gears_dynamic_analysis(self) -> 'List[_6142.ConceptGearDynamicAnalysis]':
        '''List[ConceptGearDynamicAnalysis]: 'ConceptGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsDynamicAnalysis, constructor.new(_6142.ConceptGearDynamicAnalysis))
        return value

    @property
    def concept_meshes_dynamic_analysis(self) -> 'List[_6143.ConceptGearMeshDynamicAnalysis]':
        '''List[ConceptGearMeshDynamicAnalysis]: 'ConceptMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesDynamicAnalysis, constructor.new(_6143.ConceptGearMeshDynamicAnalysis))
        return value
