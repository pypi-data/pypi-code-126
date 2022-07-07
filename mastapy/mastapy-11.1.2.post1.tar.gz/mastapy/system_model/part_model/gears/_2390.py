'''_2390.py

Gear
'''


from mastapy._internal import constructor
from mastapy.gears.gear_designs import _909
from mastapy.gears.gear_designs.zerol_bevel import _914
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _918, _919, _922
from mastapy.gears.gear_designs.straight_bevel_diff import _923
from mastapy.gears.gear_designs.straight_bevel import _927
from mastapy.gears.gear_designs.spiral_bevel import _931
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _935
from mastapy.gears.gear_designs.klingelnberg_hypoid import _939
from mastapy.gears.gear_designs.klingelnberg_conical import _943
from mastapy.gears.gear_designs.hypoid import _947
from mastapy.gears.gear_designs.face import _951, _956, _959
from mastapy.gears.gear_designs.cylindrical import _974, _1001
from mastapy.gears.gear_designs.conical import _1106
from mastapy.gears.gear_designs.concept import _1128
from mastapy.gears.gear_designs.bevel import _1132
from mastapy.gears.gear_designs.agma_gleason_conical import _1145
from mastapy.system_model.part_model.gears import (
    _2392, _2374, _2376, _2380,
    _2382, _2384, _2386, _2389,
    _2395, _2397, _2399, _2401,
    _2402, _2404, _2406, _2408,
    _2412, _2414
)
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model import _2325
from mastapy._internal.python_net import python_net_import

_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')


__docformat__ = 'restructuredtext en'
__all__ = ('Gear',)


class Gear(_2325.MountableComponent):
    '''Gear

    This is a mastapy class.
    '''

    TYPE = _GEAR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Gear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_clone_gear(self) -> 'bool':
        '''bool: 'IsCloneGear' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.IsCloneGear

    @property
    def cloned_from(self) -> 'str':
        '''str: 'ClonedFrom' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ClonedFrom

    @property
    def length(self) -> 'float':
        '''float: 'Length' is the original name of this property.'''

        return self.wrapped.Length

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def maximum_number_of_teeth(self) -> 'int':
        '''int: 'MaximumNumberOfTeeth' is the original name of this property.'''

        return self.wrapped.MaximumNumberOfTeeth

    @maximum_number_of_teeth.setter
    def maximum_number_of_teeth(self, value: 'int'):
        self.wrapped.MaximumNumberOfTeeth = int(value) if value else 0

    @property
    def minimum_number_of_teeth(self) -> 'int':
        '''int: 'MinimumNumberOfTeeth' is the original name of this property.'''

        return self.wrapped.MinimumNumberOfTeeth

    @minimum_number_of_teeth.setter
    def minimum_number_of_teeth(self, value: 'int'):
        self.wrapped.MinimumNumberOfTeeth = int(value) if value else 0

    @property
    def active_gear_design(self) -> '_909.GearDesign':
        '''GearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _909.GearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to GearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

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
    def active_gear_design_of_type_worm_design(self) -> '_918.WormDesign':
        '''WormDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _918.WormDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_worm_gear_design(self) -> '_919.WormGearDesign':
        '''WormGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _919.WormGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_worm_wheel_design(self) -> '_922.WormWheelDesign':
        '''WormWheelDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _922.WormWheelDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormWheelDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

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
    def active_gear_design_of_type_face_gear_design(self) -> '_951.FaceGearDesign':
        '''FaceGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _951.FaceGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_face_gear_pinion_design(self) -> '_956.FaceGearPinionDesign':
        '''FaceGearPinionDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _956.FaceGearPinionDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearPinionDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_face_gear_wheel_design(self) -> '_959.FaceGearWheelDesign':
        '''FaceGearWheelDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _959.FaceGearWheelDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearWheelDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_cylindrical_gear_design(self) -> '_974.CylindricalGearDesign':
        '''CylindricalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _974.CylindricalGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to CylindricalGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_cylindrical_planet_gear_design(self) -> '_1001.CylindricalPlanetGearDesign':
        '''CylindricalPlanetGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1001.CylindricalPlanetGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to CylindricalPlanetGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_conical_gear_design(self) -> '_1106.ConicalGearDesign':
        '''ConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1106.ConicalGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConicalGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ActiveGearDesign.__class__)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign is not None else None

    @property
    def active_gear_design_of_type_concept_gear_design(self) -> '_1128.ConceptGearDesign':
        '''ConceptGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1128.ConceptGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConceptGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

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
    def gear_set(self) -> '_2392.GearSet':
        '''GearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2392.GearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to GearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_agma_gleason_conical_gear_set(self) -> '_2374.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2374.AGMAGleasonConicalGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to AGMAGleasonConicalGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_bevel_differential_gear_set(self) -> '_2376.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2376.BevelDifferentialGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelDifferentialGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_bevel_gear_set(self) -> '_2380.BevelGearSet':
        '''BevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2380.BevelGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_concept_gear_set(self) -> '_2382.ConceptGearSet':
        '''ConceptGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2382.ConceptGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConceptGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_conical_gear_set(self) -> '_2384.ConicalGearSet':
        '''ConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2384.ConicalGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConicalGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_cylindrical_gear_set(self) -> '_2386.CylindricalGearSet':
        '''CylindricalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2386.CylindricalGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to CylindricalGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_face_gear_set(self) -> '_2389.FaceGearSet':
        '''FaceGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2389.FaceGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to FaceGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_hypoid_gear_set(self) -> '_2395.HypoidGearSet':
        '''HypoidGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2395.HypoidGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to HypoidGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2397.KlingelnbergCycloPalloidConicalGearSet':
        '''KlingelnbergCycloPalloidConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2397.KlingelnbergCycloPalloidConicalGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2399.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2399.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2401.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2401.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_planetary_gear_set(self) -> '_2402.PlanetaryGearSet':
        '''PlanetaryGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2402.PlanetaryGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to PlanetaryGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_spiral_bevel_gear_set(self) -> '_2404.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2404.SpiralBevelGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to SpiralBevelGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_straight_bevel_diff_gear_set(self) -> '_2406.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2406.StraightBevelDiffGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelDiffGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_straight_bevel_gear_set(self) -> '_2408.StraightBevelGearSet':
        '''StraightBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2408.StraightBevelGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_worm_gear_set(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2412.WormGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to WormGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def gear_set_of_type_zerol_bevel_gear_set(self) -> '_2414.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2414.ZerolBevelGearSet.TYPE not in self.wrapped.GearSet.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ZerolBevelGearSet. Expected: {}.'.format(self.wrapped.GearSet.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSet.__class__)(self.wrapped.GearSet) if self.wrapped.GearSet is not None else None

    @property
    def face_width(self) -> 'float':
        '''float: 'FaceWidth' is the original name of this property.'''

        return self.wrapped.FaceWidth

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def number_of_teeth(self) -> 'int':
        '''int: 'NumberOfTeeth' is the original name of this property.'''

        return self.wrapped.NumberOfTeeth

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'int'):
        self.wrapped.NumberOfTeeth = int(value) if value else 0

    @property
    def shaft(self) -> '_2343.Shaft':
        '''Shaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2343.Shaft)(self.wrapped.Shaft) if self.wrapped.Shaft is not None else None

    def connect_to(self, other_gear: 'Gear'):
        ''' 'ConnectTo' is the original name of this method.

        Args:
            other_gear (mastapy.system_model.part_model.gears.Gear)
        '''

        self.wrapped.ConnectTo(other_gear.wrapped if other_gear else None)
