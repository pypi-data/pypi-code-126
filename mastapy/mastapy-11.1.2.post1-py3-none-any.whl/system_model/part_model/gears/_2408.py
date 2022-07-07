'''_2408.py

StraightBevelGearSet
'''


from typing import List

from mastapy.gears.gear_designs.straight_bevel import _929
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2407, _2380
from mastapy.system_model.connections_and_sockets.gears import _2189
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSet',)


class StraightBevelGearSet(_2380.BevelGearSet):
    '''StraightBevelGearSet

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_929.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_929.StraightBevelGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign is not None else None

    @property
    def straight_bevel_gear_set_design(self) -> '_929.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'StraightBevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_929.StraightBevelGearSetDesign)(self.wrapped.StraightBevelGearSetDesign) if self.wrapped.StraightBevelGearSetDesign is not None else None

    @property
    def straight_bevel_gears(self) -> 'List[_2407.StraightBevelGear]':
        '''List[StraightBevelGear]: 'StraightBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGears, constructor.new(_2407.StraightBevelGear))
        return value

    @property
    def straight_bevel_meshes(self) -> 'List[_2189.StraightBevelGearMesh]':
        '''List[StraightBevelGearMesh]: 'StraightBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelMeshes, constructor.new(_2189.StraightBevelGearMesh))
        return value
