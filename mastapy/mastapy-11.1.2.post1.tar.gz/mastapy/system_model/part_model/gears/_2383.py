'''_2383.py

ConicalGear
'''


from mastapy.system_model.part_model.gears import _2391, _2390
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.conical import _1106
from mastapy.gears.gear_designs.zerol_bevel import _914
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel_diff import _923
from mastapy.gears.gear_designs.straight_bevel import _927
from mastapy.gears.gear_designs.spiral_bevel import _931
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _935
from mastapy.gears.gear_designs.klingelnberg_hypoid import _939
from mastapy.gears.gear_designs.klingelnberg_conical import _943
from mastapy.gears.gear_designs.hypoid import _947
from mastapy.gears.gear_designs.bevel import _1132
from mastapy.gears.gear_designs.agma_gleason_conical import _1145
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGear',)


class ConicalGear(_2390.Gear):
    '''ConicalGear

    This is a mastapy class.
    '''

    TYPE = _CONICAL_GEAR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self) -> '_2391.GearOrientations':
        '''GearOrientations: 'Orientation' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.Orientation)
        return constructor.new(_2391.GearOrientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_2391.GearOrientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def length(self) -> 'float':
        '''float: 'Length' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Length

    @property
    def active_gear_design(self) -> '_1106.ConicalGearDesign':
        '''ConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1106.ConicalGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConicalGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_zerol_bevel_gear_design(self) -> '_914.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _914.ZerolBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_923.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _923.StraightBevelDiffGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_gear_design(self) -> '_927.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _927.StraightBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_spiral_bevel_gear_design(self) -> '_931.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _931.SpiralBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_935.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _935.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_939.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _939.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_943.KlingelnbergConicalGearDesign':
        '''KlingelnbergConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _943.KlingelnbergConicalGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_hypoid_gear_design(self) -> '_947.HypoidGearDesign':
        '''HypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _947.HypoidGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to HypoidGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_bevel_gear_design(self) -> '_1132.BevelGearDesign':
        '''BevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1132.BevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to BevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_1145.AGMAGleasonConicalGearDesign':
        '''AGMAGleasonConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1145.AGMAGleasonConicalGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def conical_gear_design(self) -> '_1106.ConicalGearDesign':
        '''ConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1106.ConicalGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to ConicalGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_zerol_bevel_gear_design(self) -> '_914.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _914.ZerolBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_923.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _923.StraightBevelDiffGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_straight_bevel_gear_design(self) -> '_927.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _927.StraightBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_spiral_bevel_gear_design(self) -> '_931.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _931.SpiralBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_935.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _935.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_939.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _939.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_943.KlingelnbergConicalGearDesign':
        '''KlingelnbergConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _943.KlingelnbergConicalGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_hypoid_gear_design(self) -> '_947.HypoidGearDesign':
        '''HypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _947.HypoidGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to HypoidGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_bevel_gear_design(self) -> '_1132.BevelGearDesign':
        '''BevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1132.BevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to BevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None

    @property
    def conical_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_1145.AGMAGleasonConicalGearDesign':
        '''AGMAGleasonConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1145.AGMAGleasonConicalGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearDesign.__class__)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign is not None else None
