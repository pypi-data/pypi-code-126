'''_5521.py

GearSetStaticLoadCaseGroup
'''


from typing import List, Generic, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5518, _5519, _5522
from mastapy.system_model.part_model.gears import _2392, _2390
from mastapy.system_model.analyses_and_results.static_loads import _6723, _6725, _6728
from mastapy.system_model.connections_and_sockets.gears import _2175
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'GearSetStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetStaticLoadCaseGroup',)


TGearSet = TypeVar('TGearSet', bound='_2392.GearSet')
TGear = TypeVar('TGear', bound='_2390.Gear')
TGearStaticLoad = TypeVar('TGearStaticLoad', bound='_6723.GearLoadCase')
TGearMesh = TypeVar('TGearMesh', bound='_2175.GearMesh')
TGearMeshStaticLoad = TypeVar('TGearMeshStaticLoad', bound='_6725.GearMeshLoadCase')
TGearSetStaticLoad = TypeVar('TGearSetStaticLoad', bound='_6728.GearSetLoadCase')


class GearSetStaticLoadCaseGroup(_5522.PartStaticLoadCaseGroup, Generic[TGearSet, TGear, TGearStaticLoad, TGearMesh, TGearMeshStaticLoad, TGearSetStaticLoad]):
    '''GearSetStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TGearSet
        TGear
        TGearStaticLoad
        TGearMesh
        TGearMeshStaticLoad
        TGearSetStaticLoad
    '''

    TYPE = _GEAR_SET_STATIC_LOAD_CASE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> 'TGearSet':
        '''TGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Part

    @property
    def gear_set(self) -> 'TGearSet':
        '''TGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.GearSet

    @property
    def gears_load_cases(self) -> 'List[_5518.ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]':
        '''List[ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]: 'GearsLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsLoadCases, constructor.new(_5518.ComponentStaticLoadCaseGroup)[TGear, TGearStaticLoad])
        return value

    @property
    def meshes_load_cases(self) -> 'List[_5519.ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]':
        '''List[ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]: 'MeshesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesLoadCases, constructor.new(_5519.ConnectionStaticLoadCaseGroup)[TGearMesh, TGearMeshStaticLoad])
        return value

    @property
    def part_load_cases(self) -> 'List[TGearSetStaticLoad]':
        '''List[TGearSetStaticLoad]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartLoadCases)
        return value

    @property
    def gear_set_load_cases(self) -> 'List[TGearSetStaticLoad]':
        '''List[TGearSetStaticLoad]: 'GearSetLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearSetLoadCases)
        return value
