'''_6750.py

KlingelnbergCycloPalloidHypoidGearSetLoadCase
'''


from typing import List

from mastapy.system_model.part_model.gears import _2399
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6748, _6749, _6747
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetLoadCase',)


class KlingelnbergCycloPalloidHypoidGearSetLoadCase(_6747.KlingelnbergCycloPalloidConicalGearSetLoadCase):
    '''KlingelnbergCycloPalloidHypoidGearSetLoadCase

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2399.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2399.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def gears(self) -> 'List[_6748.KlingelnbergCycloPalloidHypoidGearLoadCase]':
        '''List[KlingelnbergCycloPalloidHypoidGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_6748.KlingelnbergCycloPalloidHypoidGearLoadCase))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_load_case(self) -> 'List[_6748.KlingelnbergCycloPalloidHypoidGearLoadCase]':
        '''List[KlingelnbergCycloPalloidHypoidGearLoadCase]: 'KlingelnbergCycloPalloidHypoidGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsLoadCase, constructor.new(_6748.KlingelnbergCycloPalloidHypoidGearLoadCase))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_load_case(self) -> 'List[_6749.KlingelnbergCycloPalloidHypoidGearMeshLoadCase]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshLoadCase]: 'KlingelnbergCycloPalloidHypoidMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesLoadCase, constructor.new(_6749.KlingelnbergCycloPalloidHypoidGearMeshLoadCase))
        return value
