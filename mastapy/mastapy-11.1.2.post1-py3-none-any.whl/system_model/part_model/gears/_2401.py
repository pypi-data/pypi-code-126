'''_2401.py

KlingelnbergCycloPalloidSpiralBevelGearSet
'''


from typing import List

from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _937
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2400, _2397
from mastapy.system_model.connections_and_sockets.gears import _2182
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSet',)


class KlingelnbergCycloPalloidSpiralBevelGearSet(_2397.KlingelnbergCycloPalloidConicalGearSet):
    '''KlingelnbergCycloPalloidSpiralBevelGearSet

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_conical_gear_set_design(self) -> '_937.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_937.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.wrapped.KlingelnbergConicalGearSetDesign) if self.wrapped.KlingelnbergConicalGearSetDesign is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_937.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergCycloPalloidSpiralBevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_937.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSetDesign) if self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSetDesign is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears(self) -> 'List[_2400.KlingelnbergCycloPalloidSpiralBevelGear]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGear]: 'KlingelnbergCycloPalloidSpiralBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGears, constructor.new(_2400.KlingelnbergCycloPalloidSpiralBevelGear))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes(self) -> 'List[_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearMesh]: 'KlingelnbergCycloPalloidSpiralBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshes, constructor.new(_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh))
        return value
